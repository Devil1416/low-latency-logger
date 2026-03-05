"""Structured log entry with severity levels."""
import time
from dataclasses import dataclass, field
from enum import IntEnum

class Level(IntEnum):
    DEBUG   = 10
    INFO    = 20
    WARNING = 30
    ERROR   = 40
    CRITICAL= 50

@dataclass
class LogEntry:
    level: Level
    message: str
    source: str = ''
    timestamp: float = field(default_factory=time.monotonic)

    def __str__(self) -> str:
        return f'[{self.level.name}] {self.source}: {self.message}'
