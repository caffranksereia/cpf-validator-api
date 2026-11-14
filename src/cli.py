from src.cpf_validators.validator import validate_cpf


def process_cpf() -> None:
    cpf = input("Enter your CPF: ")
    if validate_cpf(cpf):
        print(f"Valid CPF: {cpf}")
    else:
        print("Invalid CPF")
