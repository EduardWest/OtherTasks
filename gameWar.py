import random

class War:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(100, 150)
        self.current = self.health
        self.power = random.randint(20, 30)

    def take_damage(self, damage):
        self.current -= damage
        if self.current > 0:
            print(self.name, 'получил', damage, 'урона', 'осталось', self.current, 'здоровья')
        else:
            print(self.name, 'получил', self.power, 'урона и погиб')

    def get_power(self):
        return self.power

    def attack(self, enemies):
        if enemies == []:
            return
        cur_enemy = random.choice(enemies)
        cur_enemy.take_damage(self.get_power())


class WarWithProtect(War):
    def __init__(self, name):
        self.name = name
        self.health = random.randint(100, 150)
        self.current = self.health
        self.protect = random.randint(5, 10)
        self.power = random.randint(15, 25)

    def get_power(self):
        return self.power

    def take_damage(self, damage):
        super().take_damage(damage - self.protect)

class WarExpert(War):
    def __init__(self, name):
        self.name = name
        self.health = random.randint(100, 200)
        self.current = self.health
        self.power = random.randint(20, 30)

    def attack(self, enemies):
        if enemies == []:
            return
        if self.current < self.health * 0.5:
            if len(enemies) == 1:
                cur_enemy = random.choice(enemies)
                for i in range(2):
                    cur_enemy.take_damage(self.get_power())
            else:
                cur_enemy1, cur_enemy2 = random.choice(enemies), random.choice(enemies)
                cur_enemy1.take_damage(self.get_power())
                cur_enemy2.take_damage(self.get_power())
        else:
            cur_enemy = random.choice(enemies)
            cur_enemy.take_damage(self.get_power())



x = [[War("Red" + str(i)) for i in range(1, 5)], [WarWithProtect("protect_Red" + str(i)) for i in range(1, 5)],
[WarExpert("expert_Red" + str(i)) for i in range(1, 3)]]
y = [[War("white" + str(i)) for i in range(1, 5)], [WarWithProtect("protect_White" + str(i)) for i in range(1, 5)],
[WarExpert("expert_White" + str(i)) for i in range(1, 3)]]
red_Army = []
white_Army = []
for i in range(len(x)):
    for j in x[i]:
        red_Army.append(j)

for i in range(len(y)):
    for j in y[i]:
        white_Army.append(j)


while len(red_Army) > 0 and len(white_Army) > 0:
    f = random.choice(white_Army)
    f.attack(red_Army)
    for i in red_Army:
        if i.current < 0:
            red_Army.remove(i)

    if len(red_Army) <= 0  or len(white_Army) <= 0:
        break

    g = random.choice(red_Army)
    g.attack(white_Army)
    for j in white_Army:
        if j.current < 0:
            white_Army.remove(j)



if len(red_Army) > len(white_Army):
    print("Победила Red Army")
else:
    print("Победила White Army")
