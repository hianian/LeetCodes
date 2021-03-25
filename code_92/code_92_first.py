"""
给你单链表的头节点 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
个人解题思路：（修改节点的值）
    1. 先遍历链表，找到反转的起始位置，保存该位置；
    2. 接着遍历到结束位置，在遍历的过程中保留各个节点的值；
    3. 接着再次从起始位置遍历一遍，根据保留的值对节点重新赋值。
"""
# Definition for singly-linked list.


# 思路1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        start = head
        start_sec = head
        value = []

        if left == right:
            return head
        else:
            for i in range(1, left):
                start = start.next

            start_sec = start

            for i in range(left, right + 1):
                value.append(start.val)
                start = start.next

            # print("区间的值：", value)

            for i in range(right - left + 1):
                # print(value[right - left - 1 - i])
                start_sec.val = value[right - left - i]
                start_sec = start_sec.next

            return head


def answer_1():
    head = ListNode(val=1)
    point = head
    for i in range(2, 7):
        node = ListNode(val=i)
        point.next = node
        point = point.next

    point = head

    while point:
        print(point.val, end="")
        point = point.next

    print()

    s = Solution()
    heads = s.reverseBetween(head, 2, 6)

    while heads:
        print(heads.val, end="")
        heads = heads.next


if __name__ == '__main__':
    answer_1()
