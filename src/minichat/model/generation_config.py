from __future__ import annotations
from dataclasses import dataclass



@dataclass(frozen=True)
class GenerationConfig:
    """Immutable configuration for text generation parameters.

    Attributes:
        temperature: Sampling temperature; higher values produce
            more random output (default: 0.7).
        top_p: Nucleus sampling probability threshold (default: 0.95).
        top_k: Limit of highest-probability tokens to consider (default: 50).
        max_new_tokens: Maximum number of tokens to generate (default: 120).
        max_ctx_tokens: Maximum context length to retain (default: 900).

    Example:
        cfg = GenerationConfig(temperature=0.8, top_p=0.9)
    """

    temperature: float = 0.7
    top_p: float = 0.95
    top_k: int = 50
    max_new_tokens: int = 120
    max_ctx_tokens: int = 900

    def __post_init__(self):
        if self.temperature <= 0:
            raise ValueError("temperature must be positive")
        if not (0 < self.top_p <= 1):
            raise ValueError("top_p must be in (0, 1]")
        if self.top_k < 0:
            raise ValueError("top_k must be >= 0")
        if self.max_new_tokens <= 0:
            raise ValueError("max_new_tokens must be positive")
        if self.max_ctx_tokens <= 0:
            raise ValueError("max_ctx_tokens must be positive")