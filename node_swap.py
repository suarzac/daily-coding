'''
Algoexpert solution to nodeswap
'''
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def nodeSwap(head):
    if head is None or head.next is None:
        return  head
    nextNode = head.next
    head.next = nodeSwap(head.next.next)
    nextNode.next = head
    return nextNode


