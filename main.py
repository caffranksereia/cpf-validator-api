def calculate_digits(cpf: str) -> str:
    digits = [int(digit) for digit in cpf[:9]]

    for _ in range(2):
        weighted_sum = 0

        for index, digit in enumerate(digits):
            weighted_sum += digit * (len(digits) + 1 - index)

        check_digit = (weighted_sum * 10) % 11
        check_digit = check_digit if check_digit <= 9 else 0

        digits.append(check_digit)
    calculated_cpf = "".join(map(str, digits))

    return calculated_cpf


def clean_cpf(cpf: str) -> str:
    cleaned_cpf = cpf.replace(".", "").replace("-", "").strip()

    return cleaned_cpf


def has_valid_format(cpf: str) -> bool:
    return len(cpf) == 11 and cpf.isdigit() and cpf.isascii()


def has_all_equal_digits(cpf: str) -> bool:
    for index in range(len(cpf) - 1):
        current_digit = cpf[index]
        next_digit = cpf[index + 1]

        if current_digit != next_digit:
            return False

    return True


def validate_cpf(cpf: str) -> bool:
    cleaned_cpf = clean_cpf(cpf)

    if not has_valid_format(cleaned_cpf) or has_all_equal_digits(cleaned_cpf):
        return False

    return cleaned_cpf == calculate_digits(cleaned_cpf)


def main() -> None:
    cpf = input("Enter your CPF: ")

    if validate_cpf(cpf):
        print(f"Valid CPF: {cpf}")
    else:
        print("Invalid CPF")


if __name__ == "__main__":
    main()
