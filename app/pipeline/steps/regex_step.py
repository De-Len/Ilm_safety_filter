def regex_step(matcher):
    def step(ctx):
        matches = matcher.is_toxic(ctx.text)
        if matches:
            ctx.scores["regex"] = 0.6
        return ctx
    return step