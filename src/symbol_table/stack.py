class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def try_fetch_id(self, _id):
        # decide on table format
        if self.value != "head":
            return self.value.get(_id, None)
    
 
 
class Stack:
    def __init__(self):
        self.head = StackNode("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    def traverse(self, _id):
        # This is head
        stack_node = self.peek()
        for i in range(self.getSize()-1):
            stack_node = stack_node.next
            val = stack_node.try_fetch_id(_id)
            if not val is None:
                return val     


    # Push a value into the stack.
    def open_scope(self, value):
        node = StackNode(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
 
    # Remove a value from the stack and return.
    def close_scope(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value
 
    