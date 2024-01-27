def main():
    gender = input("Enter biological gender (Male/Female): ").capitalize()
    hemoglobin_value = float(input("Enter hemoglobin value (g/l): "))
    if gender == "Male":
        if 134 <= hemoglobin_value <= 167:
            print("Hemoglobin level is normal for adult males.")
        elif hemoglobin_value < 134:
            print("Hemoglobin level is low for adult males.")
        else:
            print("Hemoglobin level is high for adult males.")
    elif gender == "Female":
        if 117 <= hemoglobin_value <= 155:
            print("Hemoglobin level is normal for adult females.")
        elif hemoglobin_value < 117:
            print("Hemoglobin level is low for adult females.")
        else:
            print("Hemoglobin level is high for adult females.")
    else:
        print("Invalid gender input. Please enter Male or Female.")

if __name__ == "__main__":
    main()
