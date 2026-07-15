from __future__ import annotations

from src.agents.base import BaseAgent


class AgentRegistry:
    """
    Реестр зарегистрированных агентов.
    """

    def __init__(self) -> None:
        self._agents: dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        self._agents[agent.name] = agent

    def get(self, name: str) -> BaseAgent | None:
        return self._agents.get(name)

    def exists(self, name: str) -> bool:
        return name in self._agents

    def list_agents(self) -> list[str]:
        return sorted(self._agents.keys())

    def count(self) -> int:
        return len(self._agents)

    def clear(self) -> None:
        self._agents.clear()
