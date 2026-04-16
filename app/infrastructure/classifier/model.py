from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForSequenceClassification
import numpy as np

class ClassifierModel:
    def __init__(self):
        self.model = ORTModelForSequenceClassification.from_pretrained(
            "gravitee-io/distilbert-multilingual-toxicity-classifier",
            file_name="model.quant.onnx"
        )
        self.tokenizer = AutoTokenizer.from_pretrained("gravitee-io/distilbert-multilingual-toxicity-classifier")

    def predict_toxic_prob(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)

        outputs = self.model(**inputs)
        logits = outputs.logits

        probs = 1 / (1 + np.exp(-logits))
        toxic_prob = probs[0][1].item()

        return toxic_prob
