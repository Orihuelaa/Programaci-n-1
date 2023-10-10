import pytest #para correrlo hay que colocar en la terminal pytest test_funciones.py
from funciones import *

# Ejer 1
@pytest.mark.parametrize("dni, expected", [
    ("44746407", True),
    ("44748405", True),
    ("44746", False),
])
def test_validate_dni(dni, expected):
    assert validate_dni(dni) == expected

# Ejer 2
@pytest.mark.parametrize("chain, expected", [
    ("Hello World", 5),
    ("Python is fun", 3),
    ("  Spaces   ", 6),
])
def test_last_word_length(chain, expected):
    assert last_word_length(chain) == expected

# Ejer 3
@pytest.mark.parametrize("full_name, dni, expected", [
    ("Maria Ines Rosales", 25469648, "Maria7254"),
    ("John Doe", 12345678, "John3123"),
    ("Alice Wonderland", 9876543, "Alice10987"),
])
def test_generate_identifier(full_name, dni, expected):
    assert generate_identifier(full_name, dni) == expected

# Ejer 4
@pytest.mark.parametrize("number1, number2, expected", [
    (10, 2, True),
    (15, 5, True),
    (7, 3, False),
])
def test_en_multiplo(number1, number2, expected):
    assert en_multiplo(number1, number2) == expected

# Ejer 5
@pytest.mark.parametrize("temp_max, temp_min, expected", [
    (30, 20, 25.0),
    (25, 25, 25.0),
    (0, 10, 5.0),
])
def test_calculate_temp_half(temp_max, temp_min, expected):
    assert calculate_temp_half(temp_max, temp_min) == expected

# Ejer 6
@pytest.mark.parametrize("text, expected", [
    ("Hello", "H e l l o "),
    ("Python", "P y t h o n "),
    (" Spaces ", "  S p a c e s   "),
])
def test_add_space_between_letters(text, expected):
    assert add_space_between_letters(text) == expected

# Ejer 7
@pytest.mark.parametrize("numbers, expected", [
    ([10, 5, 15, 20], (20, 5)),
    ([3, 3, 3, 3], (3, 3)),
    ([7, 2, 9, 4, 6], (9, 2)),
])
def test_find_max_min(numbers, expected):
    assert find_max_min(numbers) == expected

# Ejer 8
@pytest.mark.parametrize("radius, expected", [
    (5, (78.54, 31.42)),
    (0, (0.0, 0.0,)),
    (10, (314.16, 62.83)),
])
def test_calculate_area_perimeter(radius, expected):
    assert calculate_area_perimeter(radius) == expected

# Ejer 9
@pytest.mark.parametrize("user, password, attempts, expected", [
    ("usuario1", "asdasd", 0, (True, 0)),
    ("user", "pass", 1, (False, 2)),
    ("usuario1", "123456", 2, (False, 3)),
])
def test_login(user, password, attempts, expected):
    assert login(user, password, attempts) == expected

# Ejer 10
@pytest.mark.parametrize("shopping_cart, expected", [
    ({"apple": 2.0, "banana": 1.0, "orange_20_descuento": 5.0}, 7.0),
    ({}, 0.0),
])
def test_apply_discount(shopping_cart, expected):
    assert apply_discount(shopping_cart) == expected

# Ejer 11
@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3, 4, 5], [1, 4, 9, 16, 25]),
    ([], []),
])
def test_apply_function_to_list(numbers, expected):
    assert apply_function_to_list(square, numbers) == expected

@pytest.mark.parametrize("x, expected", [
    (2, 4),
    (5, 25),
    (0, 0),
])
def test_square(x, expected):
    assert square(x) == expected
# Ejer 12
@pytest.mark.parametrize("sentence, expected", [
    ("Hello World", {"Hello": 5, "World": 5}),
    ("Python is fun", {"Python": 6, "is": 2, "fun": 3}),
])
def test_get_word_length(sentence, expected):
    assert get_word_length(sentence) == expected

# Ejer 13
@pytest.mark.parametrize("x, y, z, expected", [
    (3, 4, 0, 5.0),
    (1, 1, 1, 1.732),
    (0, 0, 0, 0.0),
])
def test_calculate_module_vector(x, y, z, expected):
    assert calculate_module_vector(x, y, z) == pytest.approx(expected, 0.01)

# Ejer 14
@pytest.mark.parametrize("number, expected", [
    (7, True),
    (20, False),
    (2, True),
])
def test_cousin(number, expected):
    assert cousin(number) == expected

# Ejer 15
@pytest.mark.parametrize("n, expected", [
    (5, 120),
    (0, 1),
    (1, 1),
])
def test_factorial(n, expected):
    assert factorial(n) == expected

# Ejer 16
@pytest.mark.parametrize("number, digit, expected", [
    (12345, 3, 1),
    (54321, 7, 0),
    (112233, 2, 2),
])
def test_count_occurrences_digits(number, digit, expected):
    assert count_occurrences_digits(number, digit) == expected

# Ejer 17
@pytest.mark.parametrize("number, expected", [
    (12345, 15),
    (987654321, 45),
    (0, 0),
])
def test_calculate_sum_digits(number, expected):
    assert calculate_sum_digits(number) == expected



