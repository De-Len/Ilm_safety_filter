from app.api.handler import handle_request
from app.settings.config import config
from app.factory.pipeline_factory import build_pipeline
from app.infrastructure.classifier.model import ClassifierModel
from app.infrastructure.llm.client import LLMClient
from app.infrastructure.regex.matcher import RegexMatcher
from app.settings.settings import Settings

deps = {
    "regex": RegexMatcher(),
    "classifier": ClassifierModel(),
    "llm": LLMClient(Settings.EXTERNAL_LLM_URL, Settings.EXTERNAL_LLM_MODEL_NAME)
}

pipeline = build_pipeline(config, deps)

def process(text):
    return handle_request(text, pipeline, config)

print(process("Иди-ка ты нахуй?"))
