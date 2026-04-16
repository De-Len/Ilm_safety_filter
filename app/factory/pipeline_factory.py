from app.pipeline.steps.regex_step import regex_step
from app.pipeline.steps.classifier_step import classifier_step
from app.pipeline.steps.llm_step import llm_step

def build_pipeline(config, deps):
    steps = []

    if config['use_regex']:
        steps.append(regex_step(deps['regex']))

    if config["use_classifier"]:
        steps.append(classifier_step(deps['classifier']))

    if config["use_llm"]:
        steps.append(llm_step(deps['llm']))

    return steps