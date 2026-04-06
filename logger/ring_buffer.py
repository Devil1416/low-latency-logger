"""Lock-free-style ring buffer for low-latency logging."""
from collections import deque
from typing import Any, Optional

class RingBuffer:
    """Fixed-capacity FIFO that overwrites oldest entries when full."""

    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError("Capacity must be >= 1")
        self._buf: deque = deque(maxlen=capacity)

    @property
    def capacity(self) -> int:
        return self._buf.maxlen  # type: ignore[return-value]

    def push(self, item: Any) -> None:
        self._buf.append(item)

    def pop(self) -> Optional[Any]:
        return self._buf.popleft() if self._buf else None

    def peek(self) -> Optional[Any]:
        return self._buf[0] if self._buf else None

    def __len__(self) -> int:
        return len(self._buf)

    def drain(self) -> list:
        items = list(self._buf)
        self._buf.clear()
        return items
