def classifier_step(model):
    def step(ctx):
        result = model.predict_toxic_prob(ctx.text)
        ctx.scores["classifier"] = result
        return ctx
    return step