from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseAgent(ABC):
    """
    Базовый класс для всех агентов AI Studio Framework.
    Каждый агент обязан реализовать метод execute().
    """

    def __init__(self, name: str, role: str, provider: Any):
        self.name = name
        self.role = role
        self.provider = provider

    @abstractmethod
    def execute(self, task: str, context: dict | None = None) -> str:
        """
        Выполнить задачу.

        Args:
            task: Задача, поставленная агенту.
            context: Контекст выполнения.

        Returns:
            Ответ агента.
        """
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', role='{self.role}')"
