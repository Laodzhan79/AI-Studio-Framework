from __future__ import annotations

from src.core.registry import AgentRegistry


class Orchestrator:
    """
    Центральный координатор AI Studio Framework.
    """

    def __init__(self, registry: AgentRegistry):
        self.registry = registry

    def execute(
        self,
        agent_name: str,
        task: str,
        context: dict | None = None,
    ) -> str:

        agent = self.registry.get(agent_name)

        if agent is None:
            raise ValueError(f"Agent '{agent_name}' not found.")

        return agent.execute(task, context)
