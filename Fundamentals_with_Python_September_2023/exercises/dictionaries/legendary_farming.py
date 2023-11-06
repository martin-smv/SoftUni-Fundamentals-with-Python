materials = {"shards": 0, "fragments": 0, "motes": 0}

obtained_item = ""
obtained = False
while not obtained:
    sequence_of_materials = input().split()

    for index in range(0, len(sequence_of_materials), 2):
        quantity = int(sequence_of_materials[index])
        name = sequence_of_materials[index + 1].lower()

        if name not in materials.keys():
            materials[name] = 0
        materials[name] += quantity

        if materials["shards"] >= 250:
            obtained_item = "Shadowmourne"
            materials["shards"] -= 250
            obtained = True

        elif materials["fragments"] >= 250:
            obtained_item = "Valanyr"
            materials["fragments"] -= 250
            obtained = True

        elif materials["motes"] >= 250:
            obtained_item = "Dragonwrath"
            materials["motes"] -= 250
            obtained = True

        if obtained:
            break
    if obtained:
        break

print(f"{obtained_item} obtained!")
for material, quantity in materials.items():
    print(f"{material}: {quantity}")