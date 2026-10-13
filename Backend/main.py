import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="Gramma AI API", version="2.0.0")

allowed_origins = [origin.strip() for origin in os.getenv("FRONTEND_ORIGINS", "*").split(",") if origin.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=["POST", "GET"],
    allow_headers=["Content-Type"],
)

GATEWAY_URL = "https://ai-gateway.vercel.sh/v1/chat/completions"
MODEL = os.getenv("GRAMMAR_MODEL", "google/gemini-2.5-flash-lite")
MAX_CHARACTERS = 5000

class TextRequest(BaseModel):
    text: str = Field(min_length=3, max_length=MAX_CHARACTERS)

@app.get("/health")
def health():
    return {"status": "ok", "model": MODEL}

@app.post("/correct")
def correct_grammar(request: TextRequest):
    api_key = os.getenv("AI_GATEWAY_API_KEY")
    if not api_key:
        raise HTTPException(status_code=503, detail="AI Gateway is not configured on this deployment.")

    payload = {
        "model": MODEL,
        "temperature": 0.1,
        "max_tokens": 1200,
        "messages": [
            {"role": "system", "content": "You are a precise grammar editor. Return only the corrected text. Preserve the author's meaning, tone, formatting, and paragraph breaks. If the text is already correct, return it unchanged."},
            {"role": "user", "content": request.text.strip()},
        ],
    }
    gateway_request = Request(
        GATEWAY_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(gateway_request, timeout=45) as response:
            result = json.loads(response.read())
        corrected = result["choices"][0]["message"]["content"].strip()
    except (HTTPError, URLError, KeyError, IndexError, json.JSONDecodeError) as error:
        detail = "The grammar service is temporarily unavailable."
        if isinstance(error, HTTPError) and error.code in (401, 403):
            detail = "The AI Gateway credentials are invalid or unavailable."
        raise HTTPException(status_code=502, detail=detail) from error

    return {"original": request.text, "corrected": corrected, "model": MODEL}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
