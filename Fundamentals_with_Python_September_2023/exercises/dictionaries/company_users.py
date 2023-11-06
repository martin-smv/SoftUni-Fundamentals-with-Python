companies_info = {}

while True:
    command = input()
    if command == "End":
        break

    company_name, ID = command.split(" -> ")
    if company_name not in companies_info.keys():
        companies_info[company_name] = [ID]
    if ID not in companies_info[company_name]:
        companies_info[company_name] += [ID]

for name in companies_info.keys():
    print(name)
    for ID in companies_info[name]:
        print(f"-- {ID}")
