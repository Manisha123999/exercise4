def main():
    zander_length = float(input("Enter the length of the zander in centimeters: "))

    if zander_length >= 42:
        print("Congratulations! You can keep the zander.")
    else:
        below_limit = 42 - zander_length
        print(f"Release the zander back into the lake. It is {below_limit:.2f} centimeters below the size limit.")

if __name__ == "__main__":
    main()
