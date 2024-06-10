from main import soma, sub

def test_soma():
    assert soma(2, 2) == 4

def test_soma2():
    assert soma(2, 3) == 5

def test_sub():
    assert sub(2, 1) == 1