import re

pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
count_of_barcodes = int(input())
for number in range(count_of_barcodes):
    product_group = ""
    barcode = input()
    match = re.findall(pattern, barcode)
    if match:
        for char in "".join(match):
            if char.isdigit():
                product_group += char
        if product_group:
            print(f"Product group: {product_group}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")
