pounds_per_talent = 20
lots_per_pound = 32
grams_per_lot = 13.3
talents = float(input("Enter the mass in talents: "))
pounds = float(input("Enter the mass in pounds: "))
lots = float(input("Enter the mass in lots: "))
total_grams = (talents * pounds_per_talent + pounds) * lots_per_pound * grams_per_lot
kilograms = total_grams // 1000
remaining_grams = total_grams % 1000
print("The mass is equivalent to {} kilograms and {} grams.".format(int(kilograms), int(remaining_grams)))
