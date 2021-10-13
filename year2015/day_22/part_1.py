class Creature:
    poison_effect = 0
    poison_damage = 0

    def __init__(self, max_hp, damage):
        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage

    def attack(self, target: 'Player'):
        damage = self.damage - target.armor
        if damage > 0:
            target.hp -= damage

    def recover(self):
        self.hp = self.max_hp
        self.poison_effect = 0

    def is_dead(self):
        if self.hp <= 0:
            return True
        else:
            return False


class Player(Creature):
    shield_effect = 0
    mana_effect = 0
    mana_recharge = 0
    mana_lost = 0

    def __init__(self, max_hp, damage, max_mana, armor):
        Creature.__init__(self, max_hp, damage)
        self.max_hp = max_hp
        self.hp = max_hp
        self.mana = max_mana
        self.max_mana = max_mana
        self.armor = armor

    def magic_missile(self, target: Creature, mana_cost=53, damage=4):
        target.hp -= damage
        if self.mana - mana_cost < 0:
            return False
        else:
            self.mana -= mana_cost
            self.mana_lost += mana_cost
            return True

    def drain(self, target: Creature, mana_cost=73, damage=2, heal=2):
        target.hp -= damage
        if self.mana - mana_cost < 0:
            return False
        else:
            self.mana -= mana_cost
            self.mana_lost += mana_cost
            self.hp += heal
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            return True

    def shield(self, mana_cost=113, duration=6, armor=7):
        if self.mana - mana_cost < 0:
            return False
        else:
            self.mana -= mana_cost
            self.mana_lost += mana_cost
            self.shield_effect += duration
            self.armor = armor
            return True

    def poison(self, target: Creature, mana_cost=173, duration=6, damage=3):
        if self.mana - mana_cost < 0:
            return False
        else:
            self.mana -= mana_cost
            self.mana_lost += mana_cost
            target.poison_effect += duration
            target.poison_damage = damage
            return True

    def recharge(self, mana_cost=229, duration=5):
        if self.mana - mana_cost:
            return False
        else:
            self.mana -= mana_cost
            self.mana_lost += mana_cost
            self.mana_effect += duration
            return True

    def recover(self):
        Creature.recover(self)
        self.mana = self.max_mana
        self.mana_lost = 0  # Check this line.
        self.mana_effect = 0
        self.armor = 0
        self.shield_effect = 0


def main():
    pass


if __name__ == '__main__':
    main()