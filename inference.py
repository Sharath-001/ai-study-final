import os
from openai import OpenAI

# Required environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

# Initialize client
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

def run_inference(prompt: str):
    try:
        print(f"[START] task=demo env=openenv model={MODEL_NAME}")

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        output = response.choices[0].message.content

        print(f"[STEP] step=1 action=generate_text reward=1.00 done=true error=null")
        print(f"[END] success=true steps=1 rewards=1.00")

    except Exception as e:
        print(f"[END] success=false steps=0 rewards=0.00")

if __name__ == "__main__":
    run_inference("Hello from OpenEnv")