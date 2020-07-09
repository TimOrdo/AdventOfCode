class Creature:
    def __init__(self, hit_points, damage, armor):
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor


class Item:
    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor


class Player(Creature):
    weapon: Item = None
    wearing_armor: Item = None
    l_ring: Item = None
    r_ring: Item = None

    def set_weapon(self, weapon=None):
        self.weapon = weapon
        self.damage += weapon.damage

    def set_armor(self, wearing_armor=None):
        self.wearing_armor = wearing_armor
        self.armor += wearing_armor.armor

    def set_l_ring(self, l_ring=None):
        self.l_ring = l_ring
        self.damage += l_ring.damage
        self.armor += l_ring.armor

    def set_r_ring(self, r_ring=None):
        self.r_ring = r_ring
        self.damage += r_ring.damage
        self.armor += r_ring.armor

    def get_item_cost(self):
        return self.weapon.cost + self.wearing_armor.cost + self.l_ring.cost +\
               self.r_ring.cost


shop = {
    'weapon': [
        Item('Dagger', 8, 4, 0),
        Item('Shortsword', 10, 5, 0),
        Item('Warhammer', 25, 6, 0),
        Item('Longsword', 40, 7, 0),
        Item('Greataxe', 74, 8, 0),
    ],
    'armor': [
        Item('None', 0, 0, 0),
        Item('Leather', 13, 0, 1),
        Item('Chainmail', 31, 0, 2),
        Item('Splintmail', 53, 0, 3),
        Item('Bandedmail', 75, 0, 4),
        Item('Platemail', 102, 0, 5),
    ],
    'rings': [
        Item('None', 0, 0, 0),
        Item('Damage +1', 25, 1, 0),
        Item('Damage +2', 50, 2, 0),
        Item('Damage +3', 100, 3, 0),
        Item('Defense +1', 20, 0, 1),
        Item('Defense +2', 40, 0, 2),
        Item('Defense +3', 80, 0, 3),
    ],
}


def main():
    cost_list = list()
    for w_item in shop['weapon']:
        for a_item in shop['armor']:
            for lr_item in shop['rings']:
                for rr_item in shop['rings']:
                    if lr_item == rr_item:
                        continue
                    boss = Creature(109, 8, 2)
                    player = Player(100, 0, 0)
                    player.set_weapon(w_item)
                    player.set_armor(a_item)
                    player.set_l_ring(lr_item)
                    player.set_r_ring(rr_item)
                    if player.damage <= boss.armor:
                        continue
                    while True:
                        pl_damage = player.damage - boss.armor
                        if pl_damage > 0:
                            boss.hit_points -= pl_damage
                        if boss.hit_points < 0:
                            print('Player WIN. Congratulations!')
                            break
                        boss_damage = boss.damage - player.armor
                        if boss_damage > 0:
                            player.hit_points -= boss_damage
                        if player.hit_points < 0:
                            cost_list.append(player.get_item_cost())
                            print('Player Lose. My apologise.')
                            break
    print('Game is over.')
    print('Max cost:', max(cost_list))


if __name__ == '__main__':
    main()
