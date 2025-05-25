from huggingface_hub import snapshot_download
from huggingface_hub import login

login(token="YOUR_TOKEN_HERE")


snapshot_download(
    repo_id="HUGGINGFACE_REPO_ID",
    local_dir="DEST_FOLDER"
)
