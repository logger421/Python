import pytest
import stack


def test_init():
    s = stack.Stack(3)
    assert s.items == [None, None, None]


def test_empty():
    s = stack.Stack(2)
    assert s.is_empty() == True
    s.push(1)
    assert s.is_empty() == False
    s.pop()
    assert s.is_empty() == True


def test_full():
    s = stack.Stack(2)
    assert s.is_full() == False
    s.push(1)
    s.push(1)
    assert s.is_full() == True


def test_push():
    s = stack.Stack(2)
    assert s.n == 0
    s.push(1)
    assert s.n == 1
    s.push(1)
    with pytest.raises(ValueError):
        s.push(1)

def test_pop():
    s = stack.Stack(2)
    s.push(1)
    s.push(1)
    s.pop()
    assert s.n == 1
    s.pop()
    with pytest.raises(ValueError):
        s.pop()

if __name__ == '__main__':
    pytest.main()
