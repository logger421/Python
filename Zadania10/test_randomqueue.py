import pytest
import random_queue as rq


def test_init():
    q = rq.RandomQueue()
    assert type(q.items) is list


def test_insert():
    q = rq.RandomQueue()
    assert q.is_empty()
    q.insert(1)
    assert not q.is_empty()
    q.insert(1)
    assert len(q.items) == 2


def test_remove():
    q = rq.RandomQueue()
    with pytest.raises(ValueError):
        q.remove()
    q.insert(1)
    q.remove()
    assert q.is_empty()


def test_is_empty():
    assert rq.RandomQueue().is_empty()


def test_is_full():
    assert rq.RandomQueue().is_full() == False


def test_clear():
    q = rq.RandomQueue()
    q.insert(1)
    q.insert(2)
    q.insert(3)
    q.insert(4)
    assert not q.is_empty()
    q.clear()
    assert q.is_empty()

if __name__ == '__main__':
    pytest.main()
