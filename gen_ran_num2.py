from datetime import datetime


def linear_congruential_generator(seed, a, c, m, quantity):
    numbers = []
    x = seed
    for _ in range(quantity):
        x = (a * x + c) % m
        numbers.append(round(x / m, 5))  # Normalize to [0,1] and round to 5 decimal places
    return numbers


def generate_random_numbers(quantity):
    # Generate filename with current date and time
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"random_{current_time}.txt"

    # LCM Parameters
    seed = 7  # Initial seed
    a = 1664525  # Multiplier
    c = 1013904223  # Increment
    m = 2 ** 32  # Modulus

    # Generate random numbers using LCM
    numbers = linear_congruential_generator(seed, a, c, m, quantity)

    # Store numbers in a file
    with open(filename, 'w') as file:
        for num in numbers:
            file.write(f"{num}\n")

    return filename


if __name__ == "__main__":
    # Ask the user for the quantity of random numbers to generate
    quantity = int(input("Enter the number of random numbers to generate: "))
    filename = generate_random_numbers(quantity)
    print(f"{quantity} random numbers have been written to {filename}")