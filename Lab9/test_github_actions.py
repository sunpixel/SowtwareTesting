"""
Pytest script for GitHub Actions CI/CD pipeline testing.
This script tests various mathematical operations and data structures.
"""

import pytest
import math
from typing import List, Dict, Any, Optional


# Functions to test
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def subtract_numbers(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b


def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


def divide_numbers(a: int, b: int) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_even(number: int) -> bool:
    """Check if a number is even."""
    return number % 2 == 0


def is_prime(number: int) -> bool:
    """Check if a number is prime."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def fibonacci_sequence(n: int) -> List[int]:
    """Generate Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence


def find_max(numbers: List[int]) -> Optional[int]:
    """Find the maximum number in a list."""
    if not numbers:
        return None
    return max(numbers)


def string_reversal(text: str) -> str:
    """Reverse a string."""
    return text[::-1]


def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome."""
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    return clean_text == clean_text[::-1]


# Test fixtures
@pytest.fixture
def sample_numbers() -> List[int]:
    """Fixture providing sample numbers for testing."""
    return [1, 2, 3, 4, 5, 10, 20]


@pytest.fixture
def sample_strings() -> List[str]:
    """Fixture providing sample strings for testing."""
    return ["hello", "world", "python", "pytest", "github"]


@pytest.fixture
def palindrome_strings() -> List[str]:
    """Fixture providing palindrome strings."""
    return ["racecar", "madam", "level", "A man a plan a canal Panama"]


# Test classes for grouping related tests
class TestArithmeticOperations:
    """Test class for arithmetic operations."""
    
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 200, 300),
        (-5, -10, -15),
    ])
    def test_addition(self, a: int, b: int, expected: int):
        """Test addition operation with various inputs."""
        assert add_numbers(a, b) == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (5, 3, 2),
        (10, 10, 0),
        (0, 5, -5),
        (-5, -3, -2),
    ])
    def test_subtraction(self, a: int, b: int, expected: int):
        """Test subtraction operation."""
        assert subtract_numbers(a, b) == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 6),
        (0, 5, 0),
        (-2, 4, -8),
        (7, 0, 0),
    ])
    def test_multiplication(self, a: int, b: int, expected: int):
        """Test multiplication operation."""
        assert multiply_numbers(a, b) == expected
    
    def test_division(self):
        """Test division operation."""
        assert divide_numbers(10, 2) == 5.0
        assert divide_numbers(9, 3) == 3.0
        assert divide_numbers(1, 4) == 0.25
    
    def test_division_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide_numbers(10, 0)


class TestNumberProperties:
    """Test class for number property checks."""
    
    @pytest.mark.parametrize("number,expected", [
        (2, True),
        (3, False),
        (0, True),
        (100, True),
        (-4, True),
        (-7, False),
    ])
    def test_even_numbers(self, number: int, expected: bool):
        """Test even number detection."""
        assert is_even(number) == expected
    
    @pytest.mark.parametrize("number,expected", [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (20, False),
        (97, True),
        (1, False),
        (0, False),
        (-5, False),
    ])
    def test_prime_numbers(self, number: int, expected: bool):
        """Test prime number detection."""
        assert is_prime(number) == expected


class TestSequenceOperations:
    """Test class for sequence operations."""
    
    def test_fibonacci_sequence(self):
        """Test Fibonacci sequence generation."""
        assert fibonacci_sequence(0) == []
        assert fibonacci_sequence(1) == [0]
        assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]
        assert fibonacci_sequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    def test_find_max(self, sample_numbers: List[int]):
        """Test finding maximum value in a list."""
        assert find_max(sample_numbers) == 20
        assert find_max([1]) == 1
        assert find_max([]) is None
        assert find_max([-5, -1, -10]) == -1


class TestStringOperations:
    """Test class for string operations."""
    
    def test_string_reversal(self, sample_strings: List[str]):
        """Test string reversal."""
        for text in sample_strings:
            reversed_text = string_reversal(text)
            assert len(reversed_text) == len(text)
            assert reversed_text[::-1] == text
    
    def test_palindrome_detection(self, palindrome_strings: List[str]):
        """Test palindrome detection."""
        for text in palindrome_strings:
            assert is_palindrome(text) == True
    
    @pytest.mark.parametrize("text", [
        "hello",
        "world",
        "python",
        "not a palindrome",
    ])
    def test_non_palindromes(self, text: str):
        """Test that non-palindromes are correctly identified."""
        assert is_palindrome(text) == False


# Integration tests
class TestIntegration:
    """Integration tests combining multiple functions."""
    
    def test_math_operations_chain(self):
        """Test chaining of mathematical operations."""
        # Start with addition
        result = add_numbers(10, 5)  # 15
        # Multiply result
        result = multiply_numbers(result, 2)  # 30
        # Subtract
        result = subtract_numbers(result, 10)  # 20
        # Divide
        result = divide_numbers(result, 4)  # 5.0
        
        assert result == 5.0
        assert is_even(int(result)) == False
    
    def test_number_properties_sequence(self):
        """Test number properties on a sequence."""
        fib_sequence = fibonacci_sequence(10)
        max_value = find_max(fib_sequence)
        
        assert max_value == 34
        assert is_even(max_value) == True
        assert is_prime(max_value) == False


# Performance and edge case tests
class TestEdgeCases:
    """Tests for edge cases and boundary conditions."""
    
    @pytest.mark.parametrize("value", [
        0,
        1,
        -1,
        1000000,
        -1000000,
    ])
    def test_addition_identity(self, value: int):
        """Test addition with identity element (0)."""
        assert add_numbers(value, 0) == value
        assert add_numbers(0, value) == value
    
    def test_empty_list_operations(self):
        """Test operations with empty lists."""
        assert find_max([]) is None
        assert fibonacci_sequence(0) == []
    
    def test_single_character_strings(self):
        """Test string operations with single characters."""
        assert string_reversal("a") == "a"
        assert is_palindrome("a") == True
        assert is_palindrome("!") == True


# Custom markers for different test categories
@pytest.mark.slow
class TestSlowOperations:
    """Tests marked as slow (for demonstration)."""
    
    def test_large_fibonacci(self):
        """Test Fibonacci with large number (slow operation)."""
        result = fibonacci_sequence(50)
        assert len(result) == 50
        assert result[49] == 7778742049


@pytest.mark.skip(reason="Feature not implemented yet")
def test_future_feature():
    """Example of a skipped test."""
    assert False


# Run some tests if the script is executed directly
if __name__ == "__main__":
    print("Running tests directly...")
    pytest.main([__file__, "-v"])