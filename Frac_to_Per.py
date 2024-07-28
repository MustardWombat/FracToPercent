def frac_to_percent(numb, den):
    # Convert fraction to percentage
    if den == 0:
        raise ValueError("Denominator cannot be zero.")
    return (numb / den) * 100

def main():
    print("Percent Calculator")
    print("1. Percent to Fraction")

    choice = input("Enter choice (1): ")

    if choice == '1':
        try:
            numb = float(input("Enter Numerator: "))
            den = float(input("Enter Denominator: "))

            percent = frac_to_percent(numb, den)
            print(f"The percentage is: {percent:.2f}%")

        except ValueError as e:
            print(f"Error: {e}")

    else:
        print("Invalid choice. Please enter 1")

if __name__ == "__main__":
    main()
