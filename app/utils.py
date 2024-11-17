import random
from dataclasses import dataclass

first_name = ["Добросовестный", "Очаровательный", "Влюбленный", "Осязаемый", "Загадочный", "Страшный",
              "Законопослушный", "Смешной", ]
second_name = ["закон", "пёс", "корабль", "источник", "предмет", "чайник", "парень", "стул", ]
third_name = ["государства", "соседа", "c кавказа", "владельца", "соседа", "подруги", "босса", "Зинаиды", ]


def custom_serializer(data: list | dict) -> dict:
    if isinstance(data, list):
        for item in data:
            item["_id"] = str(item["_id"])
    elif isinstance(data, dict):
        data["_id"] = str(data["_id"])
    else:
        return {}
    return data


@dataclass()
class Cinema:
    name: str
    session_start: str
    session_end: str

    def __repr__(self):
        return f"<Name: {self.name}, session starts at: {self.session_start}, session ends at: {self.session_end}>"

    def to_dict(self):
        return {"name": self.name,
                "start": self.session_start,
                "end": self.session_end}


def generate_data() -> Cinema:
    return Cinema(name=f"{random.choice(first_name)} {random.choice(second_name)} {random.choice(third_name)}",
                  session_start=f"{random.choice(range(0, 24))}:00",
                  session_end=f"{random.choice(range(0, 24))}:15")
