from __future__ import annotations

from typing import Dict

from src.agents.base import BaseAgent


class AgentRegistry:
    """
    Реестр агентов AI Studio Framework.
    """

    def __init__(self) -> None:
        self._agents: Dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        """Регистрирует агента."""
        self._agents[agent.name] = agent

    def get(self, name: str) -> BaseAgent | None:
        """Возвращает агента по имени."""
        return self._agents.get(name)

    def all(self) -> Dict[str, BaseAgent]:
        """Возвращает всех зарегистрированных агентов."""
        return self._agents
