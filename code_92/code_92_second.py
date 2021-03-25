"""
给你单链表的头节点 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
其他思路：头插法
    大概就是遍历的时候，将反转区间的节点插入到起始反转位置的前面。
    三个指针:
        1) 插入位置的前一个节点指针: insert_pre_point。（位置永远不会变）
        2) 反转序列的起始节点指针：reverse_pre_point。（这个只是反转序列的起始节点，因为是一个序列，所以这个节点不会反转，只是它后面的节点反转）
        3) 反转节点指针: reverse_point。（这个节点每次都更新）
    
    作用:
        1) 第一个指针用于插入
        2) 第二个指针用于寻找反转节点
        3) 第三个指针用于反转
"""
# Definition for singly-linked list.


# 思路2
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 新建一个新的头结点，便于“头”插
        HEAD = ListNode(next=head)
        # 指针1，指向反转序列的前一个节点。
        insert_pre_point = HEAD
        for i in range(1, left):
            insert_pre_point = insert_pre_point.next

        # 反转的话，反转的起始节点肯定不会动，是从第二个节点开始反转的。
        # 所以指针有三个：插入位置的前节点(insert_pre_point)，反转位置的前节点(reverse_pre_point)，反转节点(reverse_point)
        # 比如: A ——> B ——> C ——> D ——> E
        # 那么此时增加了空的头结点的链表就是: HEAD ——> A ——> B ——> C ——> D ——> E.
        # 如果反转是（2,4），insert_pre_point 就是指的是A节点。而我们应该就是将C插入到A和B之间。
        # 当前insert_pre_point是起始节点的前一个节点
        reverse_pre_point = insert_pre_point.next
        for i in range(left + 1, right + 1):
            # 取到反转节点，并将其“抽”出来。
            reverse_point = reverse_pre_point.next
            reverse_pre_point.next = reverse_point.next

            # 将反转节点插入到前面
            reverse_point.next = insert_pre_point.next
            insert_pre_point.next = reverse_point

            # 更新反转节点，注意，这里不用更新，因为循环的第一个语句已经更新了。
            # reverse_point = reverse_pre_point.next

        return HEAD.next

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
