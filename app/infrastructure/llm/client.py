import json

import httpx
from app.logs import logger


class LLMClient:
    def __init__(self, url: str, model: str):
        self.client = httpx.AsyncClient(timeout=120)
        self.url = url
        self.model = model

    def _get_headers(self) -> dict:
        headers = {"Content-Type": "application/json"}
        return headers

    def _extract_message(self, result: dict) -> str:
        """Универсальное извлечение message из разных форматов API"""
        # Ollama: {"message": {"content": "..."}}
        if "message" in result and result["message"].get("content"):
            return result["message"]["content"]
        # OpenAI: {"choices": [{"message": {"content": "..."}}]}
        if result.get("choices") and result["choices"][0].get("message", {}).get("content"):
            return result["choices"][0]["message"]["content"]
        # OpenAI stream chunk: {"choices": [{"delta": {"content": "..."}}]}
        if result.get("choices") and result["choices"][0].get("delta", {}).get("content"):
            return result["choices"][0]["delta"]["content"]
        # Простые форматы
        for key in ["response", "text", "output"]:
            if key in result:
                return result[key]
        return ""

    async def check_llm(self, text):
        try:
            request_body = {
                "model": self.model,
                "stream": False,
                "messages": [
                    {
                        "role": "system",
                        "content": "Ты классификатор токсичности. Отвечай только JSON форматом."
                    },
                    {
                        "role": "user",
                        "content": f"""Оцени токсичность текста от 0 до 1, где:
            0 - полностью безопасно
            1 - максимально токсично/запрещено

            Текст: "{text}"

            Ответь строго в формате JSON: {{"toxic_prob": 0.5}}"""
                    }
                ]
            }

            response = await self.client.post(
                self.url,
                json=request_body,
                headers=self._get_headers()
            )
            if response.status_code == 200:
                message = self._extract_message(response.json())
                return message
        except Exception as e:
            logger.error(f"LLM error: {e}")
            return e