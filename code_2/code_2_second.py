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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
    思路2：
        和上面的思路一样，只不过不是将结果保存在新建的节点中，而是直接更改已有的节点，不用去新建立节点。
"""


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 头结点
        head = ListNode()

        point = head

        # 保留余数
        tempQuotient = 0

        while l1 is not None or l2 is not None:

            if l1 is not None and l2 is not None:
                # 此时两个链表都非空，随意取一个节点，并更新值，作为结果节点
                l1.val = l1.val + l2.val + tempQuotient

                tempQuotient = l1.val // 10
                l1.val = l1.val % 10

                point.next = l1
                point = point.next

                l1 = l1.next
                l2 = l2.next
            elif l1 is not None:
                # 此时 l1链表非空，所以取该节点，并更新值，作为结果节点
                l1.val = l1.val + tempQuotient

                tempQuotient = l1.val // 10
                l1.val = l1.val % 10

                point.next = l1
                point = point.next

                l1 = l1.next
            else:
                # 此时 l2链表非空，所以取该节点，并更新值，作为结果节点
                l2.val = l2.val + tempQuotient

                tempQuotient = l2.val // 10
                l2.val = l2.val % 10

                point.next = l2
                point = point.next

                l2 = l2.next

        if tempQuotient != 0:
            point.next = ListNode(tempQuotient)

        return head.next


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
