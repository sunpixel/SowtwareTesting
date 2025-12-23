import pytest


class Calculator:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    def is_prime_number(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True


class TestCalculator:
    
    def setup_method(self):
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        assert self.calc.add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert self.calc.add(-2, -3) == -5

    def test_add_mixed_numbers(self):
        assert self.calc.add(5, -3) == 2

    def test_add_zero(self):
        assert self.calc.add(0, 5) == 5
        assert self.calc.add(5, 0) == 5

    def test_add_float_numbers(self):
        assert self.calc.add(2.5, 3.7) == 6.2

    def test_divide_positive_numbers(self):
        assert self.calc.divide(6, 3) == 2

    def test_divide_negative_numbers(self):
        assert self.calc.divide(-6, -3) == 2

    def test_divide_mixed_numbers(self):
        assert self.calc.divide(10, -2) == -5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            self.calc.divide(5, 0)

    def test_divide_float_result(self):
        assert self.calc.divide(5, 2) == 2.5

    def test_divide_float_numbers(self):
        assert self.calc.divide(2.5, 0.5) == 5.0

    def test_is_prime_number_small_primes(self):
        assert self.calc.is_prime_number(2) == True
        assert self.calc.is_prime_number(3) == True
        assert self.calc.is_prime_number(5) == True
        assert self.calc.is_prime_number(7) == True

    def test_is_prime_number_large_primes(self):
        assert self.calc.is_prime_number(17) == True
        assert self.calc.is_prime_number(97) == True
        assert self.calc.is_prime_number(113) == True

    def test_is_prime_number_not_prime(self):
        assert self.calc.is_prime_number(1) == False
        assert self.calc.is_prime_number(4) == False
        assert self.calc.is_prime_number(15) == False
        assert self.calc.is_prime_number(100) == False
        assert self.calc.is_prime_number(49) == False

    def test_is_prime_number_negative(self):
        assert self.calc.is_prime_number(-5) == False
        assert self.calc.is_prime_number(-1) == False

    def test_is_prime_number_zero(self):
        assert self.calc.is_prime_number(0) == False

    def test_is_prime_number_even_numbers(self):
        assert self.calc.is_prime_number(2) == True
        assert self.calc.is_prime_number(4) == False
        assert self.calc.is_prime_number(8) == False

    def test_is_prime_number_squares(self):
        assert self.calc.is_prime_number(9) == False
        assert self.calc.is_prime_number(25) == False
        assert self.calc.is_prime_number(49) == False