from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ConvertInfo:
    currency_from: str
    currency_to: str
    amount: int
