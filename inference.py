import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

API_BASE_URL = os.environ["API_BASE_URL"]
API_KEY = os.environ["API_KEY"]

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=API_KEY
)

class EmailInput(BaseModel):
    email: str

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    return {"status": "reset successful"}

@app.post("/validate")
def validate(data: EmailInput):

    prompt = f"Classify this email: {data.email}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50
    )

    return {"result": response.choices[0].message.content}


def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()