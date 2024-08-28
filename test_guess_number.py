# from Terminal > pip install pytest
# from Terminal > pytest .
from guess_number import check_guess
import pytest

# ניחוש כמו מספר המזל, ובדוק שחזרה המחרוזת "BINGO"
def test_guess_correct():
    assert check_guess(50, "50") == "!!BINGO"


# ניחוש גבוה ממספר המזל, בדוק שחזרה המחרוזת "higher guess"
def test_higher_guess():
    assert check_guess(50, "45") == "higher guess"

# ניחוש נמוך ממספר המזל, בדוק שחזרה המחרוזת "lower guess"
def test_lower_guess():
    assert check_guess(40, "80") == "lower guess"

# כתוב טסט ושלח בו מחרוזת במקום מספר, בדוק שאכן התרחשה שגיאה מסוג ValueError
def test_invalid_input_string():
    with pytest.raises(ValueError):
        check_guess(50, "forty-two");

# מספר לא בטווח, בדוק שאכן התרחשה שגיאה מסוג ValueError
def test_out_of_range_high():
    with pytest.raises(ValueError, match="number out of range"):
        check_guess(50, "144");


# מספר שלילי, בדוק שאכן התרחשה שגיאה מסוג ValueError
def test_out_of_range_negative():
    with pytest.raises(ValueError, match="number out of range"):
        check_guess(50, "-10")




