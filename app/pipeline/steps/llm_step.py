def llm_step(client):
    async def step(ctx):
        if ctx.decision != "llm_check":
            return ctx
        response = await client.check_llm(ctx.text)
        if response:
            ctx.scores["llm"] = 0.6
        return ctx
    return step