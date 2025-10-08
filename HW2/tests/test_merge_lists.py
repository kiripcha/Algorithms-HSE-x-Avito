import pytest
from src.merge_lists import ListNode, merge_two_lists_dummy, merge_two_lists_no_dummy

def create_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

@pytest.mark.parametrize("method", [merge_two_lists_dummy, merge_two_lists_no_dummy])
def test_merge_example(method):
    '''list1 = [1,2,4], list2 = [1,3,4]'''
    list1 = create_list([1, 2, 4])
    list2 = create_list([1, 3, 4])
    result = method(list1, list2)
    assert list_to_array(result) == [1, 1, 2, 3, 4, 4]

@pytest.mark.parametrize("method", [merge_two_lists_dummy, merge_two_lists_no_dummy])
def test_merge_empty_lists(method):
    '''слияние двух пустых списков'''
    assert list_to_array(method(None, None)) == []

@pytest.mark.parametrize("method", [merge_two_lists_dummy, merge_two_lists_no_dummy])
def test_merge_one_empty(method):
    '''слияние непустого и пустого списков'''
    list1 = create_list([1, 2, 3])
    list2 = None
    result = method(list1, list2)
    assert list_to_array(result) == [1, 2, 3]

@pytest.mark.parametrize("method", [merge_two_lists_dummy, merge_two_lists_no_dummy])
def test_merge_single_elements(method):
    '''слияние списков с одним элементом'''
    list1 = create_list([1])
    list2 = create_list([2])
    result = method(list1, list2)
    assert list_to_array(result) == [1, 2]

@pytest.mark.parametrize("method", [merge_two_lists_dummy, merge_two_lists_no_dummy])
def test_merge_different_lengths(method):
    '''слияние списков разной длины'''
    list1 = create_list([1, 3, 5])
    list2 = create_list([2, 4])
    result = method(list1, list2)
    assert list_to_array(result) == [1, 2, 3, 4, 5]

@pytest.mark.parametrize("method", [merge_two_lists_dummy, merge_two_lists_no_dummy])
def test_merge_same_elements(method):
    '''слияние списков с одинаковыми элементами'''
    list1 = create_list([1, 1, 1])
    list2 = create_list([1, 1, 1])
    result = method(list1, list2)
    assert list_to_array(result) == [1, 1, 1, 1, 1, 1]