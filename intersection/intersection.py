class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

def find_intersection(head1: Node, head2: Node) -> Node:
    a = set()
    if(head1 == None or head2 == None):
        return None
    while head1.next != None:
        a.add(head1)
        head1 = head1.next
    while head2.next != None:
        if head2 in a:
            return head2
        head2 = head2.next
    a.add(head1)
    if head2 in a:
        return head2