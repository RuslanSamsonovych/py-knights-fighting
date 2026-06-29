class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


def create_armour_instances(armours: list[dict]) -> list[Armour]:
    return [Armour(*armour.values()) for armour in armours]
