from __future__ import annotations

import requests

from src.core.config import Config
from src.providers.base_provider import BaseProvider


class GigaChatProvider(BaseProvider):
    """
    Провайдер для работы с API GigaChat.
    """

    def __init__(self) -> None:
        self._access_token: str | None = None

    @property
    def name(self) -> str:
        return "GigaChat"

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
    ) -> str:
        """
        Пока заглушка.
        Проверяем, что инфраструктура работает.
        """
        return (
            f"[{self.name}] "
            f"System: {system_prompt[:30]}... "
            f"User: {user_prompt[:50]}..."
        )
