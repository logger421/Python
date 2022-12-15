import pytest
from single_list import Node
from single_list import SingleList


def test_eq():
    l1 = SingleList()
    l1.insert_head(Node(11))
    l1.insert_head(Node(12))
    l1.insert_head(Node(13))

    l2 = SingleList()
    l2.insert_head(Node(11))
    l2.insert_head(Node(12))
    l2.insert_head(Node(13))

    assert l1 == l2

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
    assert alist.head == Node(22)

    alist.insert_tail(Node(33))
    assert alist.tail == Node(33)
    assert alist.head != alist.tail

def test_remove():
    alist = SingleList()
    alist.insert_head(Node(11))
    alist.insert_head(Node(22))
    alist.insert_head(Node(33))
    assert alist.remove_head() == Node(33)
    assert alist.remove_tail() == Node(11)

def test_join():
    alist = SingleList()
    alist.insert_head(Node(11))
    alist.insert_head(Node(22))
    alist.insert_head(Node(33))

    join_test = SingleList()
    join_test.insert_head(Node(1))
    join_test.insert_head(Node(2))
    join_test.insert_head(Node(3))

    alist.join(join_test)
    assert alist == create_list([33, 22, 11, 3 , 2, 1])
    assert join_test.count() == 0
    assert join_test.is_empty() == True


def create_list(l):
    my_list = SingleList()
    for el in l:
        my_list.insert_tail(Node(el))
    return my_list


if __name__ == "__main__":
    pytest.main()
