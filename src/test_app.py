import app

def test_add():
    assert app.add(7,3) == 10
    assert app.add(7)   == 9
    assert app.add(5)   == 7

def test_product():
    assert app.product(5, 5) == 25
    assert app.product(5) == 10
    assert app.product(7) == 14

