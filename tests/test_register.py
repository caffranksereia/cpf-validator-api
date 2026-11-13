import pytest

from main import (
    calculate_digits,
    clean_cpf,
    has_all_equal_digits,
    has_valid_format,
    main,
    validate_cpf,
)


@pytest.mark.parametrize(
    "cpf, expected",
    [
        ("41552789870", True),
        ("11111111111", False),
        ("22222222222", False),
        ("1234567890A", False),
        ("1234567890", False),
        ("123456789012", False),
        ("415.527.898-70", True),
        ("  ", False),
        ("415 52789870", False),
        ("415@52789870", False),
        ("1234567890²", False),
        ("52998224799", False),
        ("01234567890", True),
    ],
)
def test_cpf_validation(cpf: str, expected: bool) -> None:
    assert validate_cpf(cpf) == expected


@pytest.mark.parametrize(
    "cpf, expected",
    [
        ("415.527.898-70", "41552789870"),
        (" 415.527.898-70 ", "41552789870"),
        ("415 527 898 70", "415 527 898 70"),
        ("41552789870", "41552789870"),
    ],
)
def test_clean_cpf(cpf: str, expected: str) -> None:
    assert clean_cpf(cpf) == expected


@pytest.mark.parametrize(
    "cpf, expected",
    [
        ("41552789870", True),
        ("12345678901", True),
        ("1234567890", False),
        ("123456789012", False),
        ("1234567890A", False),
        ("1234567890²", False),
        ("415 52789870", False),
        ("415.527.898-70", False),
    ],
)
def test_has_valid_format(cpf: str, expected: bool) -> None:
    assert has_valid_format(cpf) == expected


@pytest.mark.parametrize(
    "cpf, expected",
    [
        ("11111111111", True),
        ("22222222222", True),
        ("44444444444", True),
        ("33333333333", True),
        ("33333333334", False),
    ],
)
def test_has_all_equal_digits(cpf: str, expected: bool) -> None:
    assert has_all_equal_digits(cpf) == expected


@pytest.mark.parametrize(
    "cpf,expected",
    argvalues=[
        ("529982247", "52998224725"),
        ("415527898", "41552789870"),
        ("52998224799", "52998224725"),
        ("000000006", "00000000604"),
    ],
)
def test_calculate_digits(cpf: str, expected: str) -> None:
    assert calculate_digits(cpf) == expected


@pytest.mark.parametrize(
    "cpf, expected",
    [
        ("52998224725", "Valid CPF: 52998224725"),
        ("529.982.247-25", "Valid CPF: 529.982.247-25"),
        ("11111111111", "Invalid CPF"),
        ("1234567890A", "Invalid CPF"),
    ],
)
def test_main_output(
    cpf: str,
    expected: str,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:

    monkeypatch.setattr("builtins.input", lambda _: cpf)

    main()

    captured = capsys.readouterr()

    assert captured.out.strip() == expected
