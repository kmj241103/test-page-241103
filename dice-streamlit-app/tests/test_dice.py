import pytest
from src.dice import roll_dice

def test_roll_dice():
    # Test that the roll_dice function returns a value between 1 and 6
    for _ in range(100):  # Roll the dice 100 times
        result = roll_dice()
        assert 1 <= result <= 6, "Dice roll is out of range!"