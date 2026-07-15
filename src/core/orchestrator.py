from __future__ import annotations

from src.core.registry import AgentRegistry
from src.core.router import Router
from src.memory.context_manager import ContextManager


class Orchestrator:
    """
    Центральный координатор AI Studio Framework.
    """

    def __init__(
        self,
        registry: AgentRegistry,
        context_manager: ContextManager,
        router: Router,
    ) -> None:
        self.registry = registry
        self.context = context_manager
        self.router = router

    def execute(
        self,
        task: str,
        session_id: str = "default",
    ) -> str:

        agent = self.router.route(task)

        if agent is None:
            raise ValueError("Router did not return an agent.")

        self.context.add_message(session_id, f"USER: {task}")

        response = agent.execute(
            task=task,
            context={
                "history": self.context.get_history(session_id),
            },
        )

        self.context.add_message(
            session_id,
            f"{agent.name}: {response}",
        )

        return response
