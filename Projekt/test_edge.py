import pytest
import edge as ed


def test_init():
    e1 = ed.Edge(0, 1)
    assert e1.v1 == 0 and e1.v2 == 1

    with pytest.raises(ValueError):
        e2 = ed.Edge(-1, 0)
        e3 = ed.Edge(0, -1)


def test_eq():
    e1 = ed.Edge(0, 1)
    e2 = ed.Edge(0, 1)
    e3 = ed.Edge(1, 1)

    assert e1 == e2
    assert e1 != e3


def test_str():
    e1 = ed.Edge(0, 1)
    assert e1.__str__() == '(0->1)'


if __name__ == '__main__':
    pytest.main()
