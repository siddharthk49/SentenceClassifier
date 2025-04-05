Sentiment Classifier with FastAPI + BERT

This project is a *FastAPI-based backend* that uses a *fine-tuned BERT model* to perform multi-class sentiment classification on sentences. A minimal **HTML + JavaScript frontend** is included for interaction.

 No large model files are stored in the repository — the model is finetuned and uploaded at huggingface - sikk41/bert-base-uncased-sentiment-model-finetuned-sikk41 and called from huggingface at runtime and loaded via `transformers.pipeline`.

---

Features

- 🧠 Fine-tuned BERT for sentiment classification
- 🚀 FastAPI backend for serving predictions
- 🌐 HTML/JS frontend to test the model
- ☁️ Model download from huggingface
- ✅ CORS enabled for frontend-backend interaction