from typing import Optional, Tuple
from transformers import (
    AutoModelForCausalLM,
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    pipeline,
)

def _is_seq2seq(model_name: str) -> bool:
    """
    Detects whether the model is seq2seq (T5, FLAN, BART, etc.)
    """
    name = model_name.lower()
    return any(key in name for key in ["t5", "flan", "bart", "ul2", "mt0", "marian"])

def load_text_generation_pipeline(
    model_name: str = "google/flan-t5-base",
    device: Optional[int] = None,
) -> Tuple[any, bool]:
    """
    Loads a Hugging Face generation pipeline and detects if it's seq2seq.
    Returns (pipeline, is_seq2seq)
    """
    seq2seq = _is_seq2seq(model_name)
    device = device if device is not None else -1

    print(f"[INFO] Loading model: {model_name} ({'seq2seq' if seq2seq else 'causal'})")
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    if seq2seq:
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=device)
    else:
        model = AutoModelForCausalLM.from_pretrained(model_name)
        generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=device)

    print("[INFO] Model and tokenizer loaded successfully.\n")
    return generator, seq2seq
