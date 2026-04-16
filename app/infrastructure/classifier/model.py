import asyncio
import numpy as np
from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForSequenceClassification


class ClassifierModel:
    def __init__(self):
        self.model = ORTModelForSequenceClassification.from_pretrained(
            "gravitee-io/distilbert-multilingual-toxicity-classifier",
            file_name="model.quant.onnx"
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            "gravitee-io/distilbert-multilingual-toxicity-classifier"
        )

    async def predict_toxic_prob(self, text: str) -> float:
        """Асинхронная обёртка над синхронным методом"""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._sync_predict, text)

    def _sync_predict(self, text: str) -> float:
        """Синхронный метод с реальной логикой"""
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        outputs = self.model(**inputs)
        logits = outputs.logits
        probs = 1 / (1 + np.exp(-logits))
        return probs[0][1].item()