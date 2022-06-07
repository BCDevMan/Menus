from dataclasses import dataclass
from typing import Callable, Any


@dataclass
class MenuItem:
    text: str
    key: str
    function: Callable[[Any], None]
    parent: Any

    def __str__(self):
        return self.text

    def __call__(self, *args, **kwargs):
        if self.function is None:
            raise StopIteration('No Function Defined')
        try:
            self.function(self.parent)
        except TypeError:
            self.function()
