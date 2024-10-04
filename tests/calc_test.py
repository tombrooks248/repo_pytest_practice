from app.calculator import Calculator

def test_add():

    calc_1 = Calculator()

    assert calc_1.add(7, 12) == 19
