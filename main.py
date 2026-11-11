def calculate_digits(register: str):
    numbers = [int(digit) for digit in register[:9]]

    for _ in range(2):
        result = 0

        for index, digit in enumerate(numbers):

            result += digit * (len(numbers) + 1 - index)

        new_digit = (result * 10) % 11
        new_digit = new_digit if new_digit <= 9 else 0

        numbers.append(new_digit)
    register_calculated = "".join(map(str, numbers))

    return register_calculated


def clean_register(register: str):
    new_register = register.replace(".", "").replace("-", "").strip()

    return new_register


def has_all_equal_digits(register: str) -> bool:
    for index in range(len(register) - 1):
        current = int(register[index])
        next_number = int(register[index + 1])

        if current != next_number:
            return False

    return True


def has_valid_format(register: str) -> bool:
    for index in range(len(register) - 1):
        current = int(register[index])
        next_number = int(register[index + 1])

        print(current, next_number)


def validate_cpf(register: str) -> bool:
    register = clean_register(register)

    if len(register) != 11 or not register.isdigit():
        return False

    if len(set(register)) == 1:
        return False

    return register == calculate_digits(register)


def main():
    register = input("Which's your registered, please:")

    register = calculate_digits(register)

    print(f"Register gerenation: {register}")

    if validate_cpf(register):
        print("register valid")
    else:
        print("register invalid")


if __name__ == "__main__":
    main()
