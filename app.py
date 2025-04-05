from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

# Load the fine-tuned model
#classifier = pipeline('text-classification', model='bert-base-uncased-sentiment-model')
classifier = pipeline('text-classification', model='sikk41/bert-base-uncased-sentiment-model-finetuned-sikk41')

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend requests from any origin (adjust for prod)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request format
class InputText(BaseModel):
    text: str

# Route to handle predictions
@app.post("/predict")
async def predict_sentiment(input: InputText):
    prediction = classifier(input.text)[0]
    return {"label": prediction["label"], "score": prediction["score"]}
