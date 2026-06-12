from app.services.fizzbuzz import generate_fizzbuzz


def test_fizzbuzz_basic():
    result = generate_fizzbuzz(3, 5, 15, "Fizz", "Buzz")

    assert result[2] == "Fizz"
    assert result[4] == "Buzz"
    assert result[14] == "FizzBuzz"