from src.core.registry import AgentRegistry
from src.core.orchestrator import Orchestrator
from src.agents.pm_agent import PMAgent
from src.agents.developer_agent import DeveloperAgent
from src.providers.base_provider import BaseProvider


class MockProvider(BaseProvider):
    @property
    def name(self) -> str:
        return "MockProvider"

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
    ) -> str:
        return user_prompt


def main():
    registry = AgentRegistry()

    provider = MockProvider()

    pm = PMAgent(
        name="pm",
        role="Project Manager",
        provider=provider,
    )

    developer = DeveloperAgent(
        name="developer",
        role="Developer",
        provider=provider,
    )

    registry.register(pm)
    registry.register(developer)

    orchestrator = Orchestrator(registry)

    print(orchestrator.execute(
        agent_name="pm",
        task="Составить план разработки."
    ))

    print("-" * 50)

    print(orchestrator.execute(
        agent_name="developer",
        task="Создать класс ContextManager."
    ))


if __name__ == "__main__":
    main()
