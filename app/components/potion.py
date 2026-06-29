class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect


def create_potion_instance(potion: dict) -> Potion:
    return Potion(*potion.values())
