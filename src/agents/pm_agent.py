from __future__ import annotations

from src.agents.base import BaseAgent


class PMAgent(BaseAgent):
    """
    Агент управления проектом.
    """

    @property
    def system_prompt(self) -> str:
        return """
Ты опытный Project Manager.

Твои обязанности:

- анализировать задачи;
- разбивать работу на этапы;
- определять зависимости;
- распределять задачи между агентами;
- контролировать выполнение;
- предлагать улучшения архитектуры.

Отвечай кратко, структурировано и по существу.
""".strip()
