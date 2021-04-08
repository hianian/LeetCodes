"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

比如两个数 342，465.
那么这两个数的链表形式则是：
    2 --> 4 --> 3
    5 --> 6 --> 4

那么结果相加则是：807。返回的链表形式如下：
    7 --> 0 --> 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
    思路1：
        和题目中描述的那样，因为题目提供的是链表，每个节点都是数字中的一位，所以同时遍历两个链表（非空的情况下）
        因为链表节点的顺序是数字的逆序，而二者求和就是对应位求和，保留在新节点中，然后低位向高位进位。所以直接遍历，保留进位即可。
        
        2 --> 4 --> 3
        5 --> 6 --> 4
        
        2和5相加，得7，保留在新节点中，无进位
        4和6相加，的10，进位为1，余数0保留在新节点中。
        3和4相加，注意还要加上上一个节点的进位1，得8，保留在新节点中。
        最终结果就是 7 --> 0 --> 8.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        resultHead = ListNode()
        point = resultHead
        tempQuotient = 0
        while l1 is not None or l2 is not None:

            if l1 is not None and l2 is not None:
                tempVal = l1.val + l2.val + tempQuotient
                l1 = l1.next
                l2 = l2.next
            elif l1 is not None:
                tempVal = l1.val + tempQuotient
                l1 = l1.next
            else:
                tempVal = l2.val + tempQuotient
                l2 = l2.next

            tempQuotient = tempVal // 10

            tempNode = ListNode(tempVal % 10)
            point.next = tempNode
            point = point.next

        # 判断最后的商，因为即使两个链表遍历完了，但是可能二者的最高位相加之后，还会有进位，所以需要单独判断一下商，
        # 如果不是0，则意味着最高位有进位，所以需要新开一个节点保存最高位。
        if tempQuotient != 0:
            point.next = ListNode(tempQuotient)

        return resultHead.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    sol = Solution()

    result = sol.addTwoNumbers(l1, l2)

    while result is not None:
        print(result.val, end="\t")
        result = result.next
