from dataclasses import dataclass, field
from typing import List


@dataclass
class User:
    username: str
    is_active: bool = True
    level: int = 1


@dataclass(frozen=True)
class APIConfig:
    base_url: str
    api_key: str


@dataclass(order=True)
class Employee:
    salary: int
    name: str


@dataclass
class Team:
    name: str
    members: List[str]=field(default_factory=list)