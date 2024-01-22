
    inches_str = input("Enter the length in inches: ")
    inches_float = float(inches_str)
     centimeters = 2.54 * inches_float
     print(f"{inches_float} inches is equal to {centimeters} centimeters.")
    except ValueError:
        print("Please enter a valid number for inches.")
