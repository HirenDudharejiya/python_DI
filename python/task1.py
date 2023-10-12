def damage(dmg, s, time):
    
    total_attacks = s * time
    total_damage = dmg * total_attacks
    return total_damage


damage_per_attack = int(input("Please enter damage: "))
attacks_per_second = int(input("Please enter attacks: "))
time = int(input("Please enter time: "))

total_damage = damage(damage_per_attack, attacks_per_second, time)
print(f"{total_damage}")
