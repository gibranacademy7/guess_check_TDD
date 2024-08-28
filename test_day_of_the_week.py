# file: test_days_of_week.py

import pytest
from days_of_week import get_day_of_week

def test_day_1():
    assert get_day_of_week(1) == "Sunday"

def test_day_2():
    assert get_day_of_week(2) == "Monday"

def test_day_3():
    assert get_day_of_week(3) == "Tuesday"

def test_day_4():
    assert get_day_of_week(4) == "Wednesday"

def test_day_5():
    assert get_day_of_week(5) == "Thursday"

def test_day_6():
    assert get_day_of_week(6) == "Friday"

def test_day_7():
    assert get_day_of_week(7) == "Saturday"

def test_invalid_day():
    with pytest.raises(ValueError):
        get_day_of_week(8)
