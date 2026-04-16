from app.factory.pipeline_factory import build_pipeline
from app.pipeline.context import Context
from app.pipeline.pipeline import run_pipeline
from app.settings.config import config, deps

pipeline = build_pipeline(config, deps)


async def handle_request(text):
    ctx = Context(text=text)

    ctx = await run_pipeline(ctx, pipeline)

    return ctx