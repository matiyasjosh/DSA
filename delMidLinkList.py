#this function deletes the middle of linked list
class linkedList:
    def delMidLL(self):
        fast, slow = self.head, self.head
        prev = None #used to track the middle node
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next #represent the middle element with the next node after it
        return head
