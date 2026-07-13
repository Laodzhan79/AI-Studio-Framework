from __future__ import annotations

from src.agents.base import BaseAgent


class PMAgent(BaseAgent):
    """
    Project Manager Agent.

    Координирует выполнение задач и распределяет работу между агентами.
    """

    def execute(self, task: str, context: dict | None = None) -> str:
        return (
            f"PM Agent\n"
            f"Получена задача: {task}\n"
            f"Статус: задача принята в обработку."
        )
