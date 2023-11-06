key = input().split(", ")
value = input().split(", ")

country_dictionary = {k: v for k, v in zip(key, value)}

for country, capital in country_dictionary.items():
    print(f"{country} -> {capital}")

