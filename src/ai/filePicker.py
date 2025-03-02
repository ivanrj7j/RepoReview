import base64
import os
from google import genai
from google.genai import types
import json
from .. import env

with open("prompts/filePicker.md", "r") as f:
    filePickerSystemPrompt = f.read()

with open("prompts/filePickerOutput.md", "r") as f:
    filePickerOutputSystemPrompt = f.read()


def generate(fileStructure: dict[str, str]) -> str:
    client = genai.Client(
        api_key=env.GEMINI_API_KEY
    )

    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text="""{'.gitignore': 'file', 'LICENSE': 'file', 'README.md': 'file', 'config.py': 'file', 'main.py': 'file', 'src': {'init.py': 'file', 'blocks.py': 'file', 'discriminator.py': 'file', 'generator.py': 'file', 'loss.py': 'file'}, 'train': {'mseTrain.py': 'file', 'vggTrain.py': 'file'}, 'utils': {'init.py': 'file', 'dataloader.py': 'file', 'utils.py': 'file'}}"""
                ),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(
                    text=filePickerOutputSystemPrompt
                ),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=json.dumps(fileStructure)
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
                text=filePickerSystemPrompt
            ),
        ],
    )

    return json.loads(client.models.generate_content(
        model = model,
        contents=contents,
        config = generate_content_config
    ).text)
    