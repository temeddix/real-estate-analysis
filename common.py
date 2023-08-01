import json

API_KEY = "466edbcd290d44e4b8a5aa8a8bd83a0b"


def format_json(input: str) -> str:
    return json.dumps(
        json.loads(input),
        indent=2,
        ensure_ascii=False,
    )
