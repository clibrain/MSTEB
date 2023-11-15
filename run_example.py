"""Example script for benchmarking all datasets constituting the MTEB English leaderboard & average scores"""

import logging
import os

from mteb.evaluation.MTEB import MTEB
from sentence_transformers import SentenceTransformer
from mteb.tasks import  ArguAna, SCIDOCS
import huggingface_hub

def log_into_huggingface_hub() -> None:
    """
    Log into the Hugging Face Hub.

    :raises ValueError: If the HUGGINGFACE_TOKEN environment variable is not set.
    """
    
    TOKEN = "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"
    if not TOKEN:
        raise ValueError("HUGGINGFACE_TOKEN is not set in the .env file.")

    huggingface_hub.login(token=TOKEN, write_permission=True)


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("main")

models = ["BAAI/bge-small-en-v1.5"]
log_into_huggingface_hub()
for model_name in models:
    model = SentenceTransformer(model_name, device="cpu")
    evaluation = MTEB(task_langs=["es"])
    # evaluation = MTEB(tasks=[
    #         SCIDOCS(langs=["en"])
    # ])
    evaluation.run(model, output_folder=f"./results/{model_name}", eval_splits=["test"])

    