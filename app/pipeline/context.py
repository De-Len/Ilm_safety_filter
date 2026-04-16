from dataclasses import dataclass, field

@dataclass
class Context:
    text: str
    scores: dict = field(default_factory=dict)
    flags: dict = field(default_factory=dict)
    decision: str | None = None