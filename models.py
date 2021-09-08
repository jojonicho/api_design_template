from dataclass import SomethingDC
from dataclasses import dataclass, field
import threading
import collections


@dataclass()
class Something:
    key_to_valule: dict = field(default_factory=dict)
    # implement me
