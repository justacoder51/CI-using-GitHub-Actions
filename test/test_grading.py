import pytest

from evaluate_grads import grade, score


def test_score():
    assert score([90, 100]) == 95
    assert score([70, 71]) == 70.5

def test_grade():
    assert grade([90, 90]) == "A+"
    assert grade([85, 84]) == "A"
    assert grade([60]) == "B"
    assert grade([55]) == "C"
    assert grade([49]) == "F"

if __name__ == "__main__":
    pytest.main()
