from app.core.decision import make_decision
from app.settings.config import config


async def run_pipeline(ctx, steps):
    for step in steps:
        ctx = await step(ctx)
        ctx.decision = make_decision(ctx.scores, config["thresholds"])
    return ctx