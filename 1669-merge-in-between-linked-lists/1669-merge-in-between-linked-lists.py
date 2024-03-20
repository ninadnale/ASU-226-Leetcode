# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list1_itr = list1
        for i in range(a-1):
            list1_itr = list1_itr.next

        temp = list1_itr        
        for i in range(a-1, b):
            temp = temp.next
        list1_patch = temp.next

        list2_end = None
        temp = list2
        while(temp.next):
            temp = temp.next
        list2_end = temp

        list1_itr.next = list2
        list2_end.next = list1_patch


        return list1