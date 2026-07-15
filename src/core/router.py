from __future__ import annotations

from src.core.registry import AgentRegistry
from src.agents.base import BaseAgent


class Router:
    """
    Маршрутизатор задач.
    Возвращает объект агента, а не его имя.
    """

    def __init__(self, registry: AgentRegistry):
        self.registry = registry

    def route(self, task: str) -> BaseAgent:
        text = task.lower()

        developer_keywords = (
            "код",
            "python",
            "класс",
            "функция",
            "метод",
            "рефакторинг",
            "bug",
            "ошибка",
        )

        if any(keyword in text for keyword in developer_keywords):
            return self.registry.get("developer")

        return self.registry.get("pm")
