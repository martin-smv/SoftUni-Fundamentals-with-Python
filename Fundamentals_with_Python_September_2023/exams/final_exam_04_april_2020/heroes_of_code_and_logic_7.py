def cast_spell(name, mp_needed, spell, heroes):
    if heroes[name]["MP"] >= mp_needed:
        heroes[name]["MP"] -= mp_needed
        print(f"{name} has successfully cast {spell} and now has {heroes[name]['MP']} MP!")
    else:
        print(f"{name} does not have enough MP to cast {spell}!")

    return heroes


def take_damage(name, damage, attacker, heroes):
    if heroes[name]["HP"] <= damage:
        del heroes[name]
        print(f"{name} has been killed by {attacker}!")
    else:
        heroes[name]["HP"] -= damage
        print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['HP']} HP left!")

    return heroes


def recharge(name, mp_amount, heroes):
    recovered_amount = 0
    if heroes[name]["MP"] + mp_amount > 200:
        recovered_amount = 200 - heroes[name]["MP"]
        heroes[name]["MP"] = 200
    else:
        recovered_amount = (mp_amount + heroes[name]["MP"]) - heroes[name]["MP"]
        heroes[name]["MP"] += mp_amount
    print(f"{name} recharged for {recovered_amount} MP!")

    return heroes


def heal(name, hp_amount, heroes):
    recovered_amount = 0
    if heroes[name]["HP"] + hp_amount > 100:
        recovered_amount = 100 - heroes[name]["HP"]
        heroes[name]["HP"] = 100
    else:
        recovered_amount = (hp_amount + heroes[name]["HP"]) - heroes[name]["HP"]
        heroes[name]["HP"] += hp_amount
    print(f"{name} healed for {recovered_amount} HP!")

    return heroes


heroes_dict = {}

number_of_heroes = int(input())

for number in range(number_of_heroes):
    current_hero = input().split()
    hero_name = current_hero[0]
    hit_points = int(current_hero[1])
    mana_points = int(current_hero[2])
    heroes_dict[hero_name] = {"HP": hit_points, "MP": mana_points}

command = input()
while command != "End":
    command = command.split(" - ")

    if command[0] == "CastSpell":
        hero_name = command[1]
        mana_points = int(command[2])
        spell_name = command[3]
        heroes_dict = cast_spell(hero_name, mana_points, spell_name, heroes_dict)

    elif command[0] == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker_name = command[3]
        heroes_dict = take_damage(hero_name, damage, attacker_name, heroes_dict)

    elif command[0] == "Recharge":
        hero_name = command[1]
        amount = int(command[2])
        heroes_dict = recharge(hero_name, amount, heroes_dict)

    elif command[0] == "Heal":
        hero_name = command[1]
        amount = int(command[2])
        heroes_dict = heal(hero_name, amount, heroes_dict)

    command = input()

for hero_name, value in heroes_dict.items():
    hit_points = value["HP"]
    mana_points = value["MP"]
    print(f"{hero_name}\n"
          f"  HP: {hit_points}\n"
          f"  MP: {mana_points}")
