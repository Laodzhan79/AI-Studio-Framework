from src.core.registry import AgentRegistry
from src.agents.echo_agent import EchoAgent
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
    agent = EchoAgent(
        name="echo",
        role="Test Agent",
        provider=provider,
    )

    registry.register(agent)

    result = registry.get("echo").execute("Проверка архитектуры")

    print(result)


if __name__ == "__main__":
    main()
