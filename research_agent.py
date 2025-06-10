"""Example research agent using AutoGen's DeepResearchAgent."""

from __future__ import annotations

import argparse

from autogen import UserProxyAgent, config_list_from_dotenv
from autogen.agents.experimental.deep_research import DeepResearchAgent


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a deep research agent")
    parser.add_argument("question", help="Question to research")
    args = parser.parse_args()

    config_list = config_list_from_dotenv()
    if not config_list:
        raise RuntimeError(
            "No LLM configuration found. Set an API key in a .env file or as environment variables."
        )
    llm_config = {"config_list": config_list}

    user = UserProxyAgent("user", human_input_mode="NEVER")
    researcher = DeepResearchAgent(name="researcher", llm_config=llm_config)

    result = user.initiate_chat(researcher, message=args.question)
    print(result.summary)


if __name__ == "__main__":
    main()
