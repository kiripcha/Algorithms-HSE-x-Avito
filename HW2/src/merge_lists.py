class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists_dummy(list1, list2):
    '''слияние двух отсортированных списков с использованием фиктивного узла'''
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    if list2:
        current.next = list2
    
    return dummy.next

def merge_two_lists_no_dummy(list1, list2):
    '''слияние двух отсортированных списков без использования фиктивного узла'''
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val <= list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next
    
    current = head
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    
    return head