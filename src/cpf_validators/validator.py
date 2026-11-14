from src.cpf_validators.constants.constant import (
    CPF_BASE_LENGTH,
    CPF_LENGTH,
    MIN_WEIGHT,
    MODULUS,
    MULTIPLIER,
)


def calculate_digits(cpf: str) -> str:
    digits = [int(digit) for digit in cpf[:CPF_BASE_LENGTH]]

    for _ in range(MIN_WEIGHT):
        weighted_sum = 0

        for index, digit in enumerate(digits):
            weighted_sum += digit * (len(digits) + 1 - index)

        check_digit = (weighted_sum * MULTIPLIER) % MODULUS
        check_digit = check_digit if check_digit <= CPF_BASE_LENGTH else 0

        digits.append(check_digit)
    calculated_cpf = "".join(map(str, digits))

    return calculated_cpf


def clean_cpf(cpf: str) -> str:
    cleaned_cpf = cpf.replace(".", "").replace("-", "").strip()

    return cleaned_cpf


def has_valid_format(cpf: str) -> bool:
    return len(cpf) == CPF_LENGTH and cpf.isdigit() and cpf.isascii()


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
