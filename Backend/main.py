from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from happytransformer import HappyTextToText, TTSettings


app = FastAPI()

# Allow the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the AI model (This may take a minute on first run)
print("Loading AI Model...")
happy_tt = HappyTextToText("T5", "vennify/t5-small-grammar-correction")
settings = TTSettings(num_beams=5, min_length=1)

class TextRequest(BaseModel):
    text: str

@app.post("/correct")
async def correct_grammar(request: TextRequest):
    # The model expects a prefix for T5
    input_text = "gec: " + request.text
    result = happy_tt.generate_text(input_text, args=settings)
    return {"original": request.text, "corrected": result.text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)