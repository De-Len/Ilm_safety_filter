from app.infrastructure.classifier.model import ClassifierModel
from app.infrastructure.llm.client import LLMClient
from app.infrastructure.regex.matcher import RegexMatcher
from app.settings.settings import Settings

config = {
    "use_regex": True,
    "use_classifier": True,
    "use_llm": True,
    "thresholds": {
        "block": 0.5,
        "review": 0.3
    }
}

deps = {
    "regex": RegexMatcher(),
    "classifier": ClassifierModel(),
    "llm": LLMClient(Settings.EXTERNAL_LLM_URL, Settings.EXTERNAL_LLM_MODEL_NAME)
}