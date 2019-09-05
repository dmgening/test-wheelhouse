from dataclasses import dataclass


@dataclass()
class Vertex:
    entity: str
    factor: str

    @property
    def is_any_entity(self) -> bool:
        return self.entity == "*"

    @property
    def is_any_factor(self) -> bool:
        return self.factor == "*"


@dataclass()
class Attribute:
    name: str
    value: str

    @property
    def is_text(self) -> bool:
        return self.name.endswith("_text_search")
