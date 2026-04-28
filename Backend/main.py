import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from happytransformer import HappyTextToText, TTSettings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Standardize the path logic
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "my_custom_model")

# 2. Define settings BEFORE the route
settings = TTSettings(num_beams=5, min_length=1)

# 3. Robust Loading
print(f"Attempting to load model from: {model_path}")

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Folder NOT FOUND at: {model_path}")

# Check for the actual weight file
weights_file = os.path.join(model_path, "model.safetensors")
if not os.path.isfile(weights_file):
    # Check for the old format just in case
    if not os.path.isfile(os.path.join(model_path, "pytorch_model.bin")):
        raise FileNotFoundError(f"Weights (model.safetensors) missing in: {model_path}")

happy_tt = HappyTextToText("T5", model_path)

class TextRequest(BaseModel):
    text: str

@app.post("/correct")
async def correct_grammar(request: TextRequest):
    input_text = "gec: " + request.text
    result = happy_tt.generate_text(input_text, args=settings)
    return {"original": request.text, "corrected": result.text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
