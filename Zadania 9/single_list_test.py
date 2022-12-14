import pytest
from single_list import Node
from single_list import SingleList


def test_empty_list():
    l = SingleList()
    assert l.is_empty() == True
    l.insert_head(Node(1))
    assert l.is_empty() == False

def test_clear_list():
    alist = SingleList()
    alist.insert_head(Node(11))  # [11]
    alist.insert_head(Node(22))  # [22, 11]
    alist.insert_head(Node(33))  # [33, 22, 11]
    alist.clear()
    assert alist.is_empty() == True

def test_count():
    alist = SingleList()
    alist.insert_head(Node(11))  # [11]
    alist.insert_head(Node(22))  # [22, 11]
    alist.insert_head(Node(33))  # [33, 22, 11]
    assert alist.count() == 3

def test_insert():
    alist = SingleList()
    alist.insert_head(Node(11))
    assert alist.head == alist.tail

    alist.insert_head(Node(22))
    assert alist.head.data == 22

    alist.insert_tail(Node(33))
    assert alist.tail.data == 33
    assert alist.head != alist.tail

def test_remove():
    pass

def test_join():
    pass

if __name__ == "__main__":
    pytest.main()
