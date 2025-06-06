from fizzbuzz import fizzbuzz


def test_with_zero():
    assert fizzbuzz(0) == 0


def test_same_number_with_1_2_and_4():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(4) == 4


def test_print_Fizz_when_multiple_of_3_only():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(6) == 'Fizz'
    assert fizzbuzz(12) == 'Fizz'  # corregido, 12 es múltiplo de 3


def test_print_Buzz_when_multiple_of_5_only():
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(10) == 'Buzz'
    assert fizzbuzz(20) == 'Buzz'  # corregido, 20 es múltiplo de 5


def test_print_FizzBuzz_when_multiple_of_3_and_5():
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz(30) == 'FizzBuzz'  # agregué otro caso múltiplo de 3 y 5
