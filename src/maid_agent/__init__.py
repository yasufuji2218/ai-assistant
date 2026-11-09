from maid_agent.llm import ask

MAID_PROMPT = "あなたは丁寧で親切なメイドです。ご主人様に短く返事をしてください。"


def main() -> None:
    reply = ask(MAID_PROMPT, "こんばんは")
    print(reply)
