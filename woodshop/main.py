from price_calculation import calculate_wood_price

def main():
    print("Welcome to the Wood Price Calculator!")

    # Get user input for the wood properties
    try:
        density = float(input("Enter the density of the wood (kg/m³): "))
        length = float(input("Enter the length of the wood (m): "))
        width = float(input("Enter the width of the wood (m): "))
        height = float(input("Enter the height of the wood (m): "))
        price_per_cubic_meter = float(input("Enter the price per cubic meter of the wood: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    # Calculate the price
    price, volume, mass = calculate_wood_price(density, length, width, height, price_per_cubic_meter)

    # Output the result
    print("\nWood Price Summary:")
    print(f"Price: ${price:.2f}")
    print(f"Volume: {volume:.2f} cubic meters")
    print(f"Mass: {mass:.2f} kg")

if __name__ == "__main__":
    main()
