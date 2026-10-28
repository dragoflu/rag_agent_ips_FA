from dataclasses import dataclass, field
from typing import Protocol


@dataclass(frozen=True)
class Source:
    doc_id: str
    text: str
    page: int | None = None
    score: float | None = None


@dataclass
class Answer:
    text: str
    sources: list[Source] = field(default_factory=list)


class Pipeline(Protocol):
    name: str

    def answer(self, question: str) -> Answer: ...
