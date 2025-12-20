class Character:
    def __init__(self, name, damage):
        self.name = name
        self._health = 100
        self._damage = damage

    def attack(self, target):
        if hasattr(target, 'take_damage'):
            target.take_damage(self._damage)

    def take_damage(self, amount):
        self._health -= amount

    def get_status(self):
        return f"Имя: {self.name}, Здоровье: {self._health}"


class Warrior(Character):
    def __init__(self, name, damage, armor):
        super().__init__(name, damage)
        self.armor = armor

    def take_damage(self, amount):
        if self.armor < amount:
            self._health -= (amount - self.armor)


class Mage(Character):
    def __init__(self, name, damage, mana):
        super().__init__(name, damage)
        self.mana = mana

    def attack(self, target):
        if self.mana >= 10:
            super().attack(target)
            self.mana -= 10



