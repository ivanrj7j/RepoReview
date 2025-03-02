from .model import model, client
from google.genai import types
import json


with open("prompts/scoring.md", "r") as f:
    systemPrompt = f.read()

with open("prompts/scoringExampleInput.md", "r") as f:
    exampleInput = f.read()

with open("prompts/scoringExampleOutput.md", "r") as f:
    exampleOutput = f.read()


def generateScore(inp:dict[str, str]):
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=exampleInput
                ),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(
                    text=exampleOutput
                ),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=json.dumps(inp)
                ),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_mime_type="application/json",
        system_instruction=[
            types.Part.from_text(
                text=systemPrompt
            ),
        ],
    )

    response = json.loads(client.models.generate_content(
        model = model,
        contents=contents,
        config = generate_content_config
    ).text)

    overall = 0
    for x in response["evaluation"].values():
        overall += x["score"]

    overall /= len(response["evaluation"])

    response["total"] = round(overall)

    return response