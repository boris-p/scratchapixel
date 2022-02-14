# we're given two non empty linked lists representing two no negative integerts.
# digits are stored in reverse order and each of the nodes contains a single digit
# add two numbers and return as linked list


from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(num1: ListNode, num2: ListNode):
    dummy = ListNode()
    cur = dummy

    carry = 0

    while num1 or num2 or carry:
        v1 = num1.val if num1 else 0
        v2 = num2.val if num2 else 0

        # new digit
        val = v1 + v2 + carry
        carry = val // 10
        cur.next = ListNode(val % 10)
        cur = cur.next

        num1 = num1.next if num1 else None
        num2 = num2.next if num2 else None

    return dummy.next
