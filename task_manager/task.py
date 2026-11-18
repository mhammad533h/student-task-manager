"""Task model for the Student Task Manager."""
from dataclasses import dataclass, asdict


@dataclass
class Task:
    """A single student task."""

    id: int
    title: str
    completed: bool = False

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(id=data["id"], title=data["title"], completed=data.get("completed", False))

    def __str__(self):
        mark = "x" if self.completed else " "
        return f"[{mark}] {self.id}. {self.title}"
