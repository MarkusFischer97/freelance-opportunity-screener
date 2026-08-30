from dataclasses import dataclass


@dataclass
class Opportunity:
    company: str
    title: str
    url: str
    skills: list[str]
    location: str
    remote_percent: int
    contract_type: str
    duration: str
    beginning: str
    created: str