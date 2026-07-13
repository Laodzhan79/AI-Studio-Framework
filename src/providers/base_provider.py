from __future__ import annotations

from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Базовый интерфейс для всех LLM-провайдеров.

    Провайдер отвечает только за взаимодействие
    с языковой моделью (GigaChat, OpenAI, Ollama и т.д.).
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Название провайдера."""
        pass

    @abstractmethod
    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
    ) -> str:
        """
        Отправляет запрос в языковую модель.

        Args:
            system_prompt: Системный промпт.
            user_prompt: Пользовательский запрос.
            temperature: Температура генерации.

        Returns:
            Ответ модели.
        """
        raise NotImplementedError
