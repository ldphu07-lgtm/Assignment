print("Enter mass in medieval units:")
talents = float(input("Talents: "))
pounds = float(input("Pounds: "))
lots = float(input("Lots: "))

total_lots = (talents * 20 * 32) + (pounds * 32) + lots

total_grams = total_lots * 13.3

kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")