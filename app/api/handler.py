from app.pipeline.context import Context
from app.pipeline.pipeline import run_pipeline


def handle_request(text, pipeline, config):
    ctx = Context(text=text)

    ctx = run_pipeline(ctx, pipeline)

    return ctx