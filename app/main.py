class AliveList(list):
    def __str__(self) -> list:

        list_of_animal = []
        for animal in self:
            list_of_animal.append(
                f"{{Name: {animal.name}, "
                f" Health: {animal.health}, "
                f" Hidden: {animal.hidden}}}"
            )
        return "[" + ", ".join(list_of_animal) + "]"


class Animal:
    alive = AliveList()

    def __init__(self, name: str, health: int = 100) -> None:
        # Не потрібно перезаписувати Animal.alive у конструкторі
        Animal.alive = AliveList(Animal.alive)
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    def bite(self, other: Herbivore) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)
