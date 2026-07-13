from __future__ import annotations

from src.agents.base import BaseAgent


class DeveloperAgent(BaseAgent):
    """
    Агент-разработчик.
    Отвечает за задачи, связанные с программированием.
    """

    def execute(self, task: str, context: dict | None = None) -> str:
        return (
            f"Developer Agent\n"
            f"Получена задача: {task}\n"
            f"Статус: задача принята в разработку."
        )
