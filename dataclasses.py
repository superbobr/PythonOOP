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


@dataclass
class User:
    name: str
    age: int


user1_name = input()
user1_age = int(input())
user2_name = input()
user2_age = int(input())

user1 = User(user1_name, user1_age)
user2 = User(user2_name, user2_age)
print(user1 == user2)