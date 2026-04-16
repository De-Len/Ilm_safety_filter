def classifier_step(model):
    async def step(ctx):
        result = await model.predict_toxic_prob(ctx.text)
        ctx.scores["classifier"] = result
        return ctx
    return step