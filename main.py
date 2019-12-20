from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
   
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
   
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class OneHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "First":
            return f"OneHandler: I'll take the {request}"
        else:
            return super().handle(request)


class OtherHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Second":
            return f"OtherHandler: I'll take the {request}"
        else:
            return super().handle(request)


class DifferentHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Third":
            return f"DifferentHandler: I'll take the {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
 
    for task in ["First", "Second", "Third", "Fourth"]:
        print(f"\nWhos {task}?")
        result = handler.handle(task)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {task} was left untouched.", end="")


if __name__ == "__main__":
    one = OneHandler()
    two = OtherHandler()
    three = DifferentHandler()

    one.set_next(two).set_next(three)

    print("Chain: one > two > three")
    client_code(one)
    print("\n")

    print("Subchain: two > three")
    client_code(two)