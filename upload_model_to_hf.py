from huggingface_hub import HfApi, HfFolder, Repository, create_repo
from huggingface_hub import upload_folder  # For folders with tokenizer and config

# Step 1: Create a repo (if not already created)
repo_name = "sikk41/bert-base-uncased-sentiment-model-finetuned-sikk41"
#create_repo(repo_id=repo_name, private=False)

# Step 2: Upload your model (assume model and tokenizer are saved in ./my_model/)
upload_folder(
    repo_id=repo_name,
    folder_path="bert_base_train_dir",
    commit_message="Finetuned model II -  bert_base_train_dir"
)
