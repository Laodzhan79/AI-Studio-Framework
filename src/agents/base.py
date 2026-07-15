from __future__ import annotations

from abc import ABC
from typing import Any


class BaseAgent(ABC):
    """
    Базовый класс для всех агентов AI Studio Framework.

    Вызов LLM реализован здесь один раз.
    Наследники должны определить только system_prompt.
    """

    def __init__(self, name: str, role: str, provider: Any):
        self.name = name
        self.role = role
        self.provider = provider

    @property
    def system_prompt(self) -> str:
        """
        Системный промпт агента.
        Должен быть переопределён наследником.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement system_prompt."
        )

    def execute(
        self,
        task: str,
        context: dict | None = None,
    ) -> str:
        """
        Универсальное выполнение задачи через провайдера.
        """

        history = ""

        if context and "history" in context:
            history = "\n".join(context["history"])

        user_prompt = task

        if history:
            user_prompt = (
                f"История:\n{history}\n\n"
                f"Текущая задача:\n{task}"
            )

        return self.provider.generate(
            system_prompt=self.system_prompt,
            user_prompt=user_prompt,
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(name='{self.name}', role='{self.role}')"
        )
