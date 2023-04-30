from typing import Any, Tuple

class SymbolTabel:
    def __init__(self):
        self.content = dict()
        self.next = None
    
    def try_fetch_id(self, _id):
        # decide on table format
        return self.content.get(_id, None)
    
 
class Stack:
    def __init__(self):
        self.head = SymbolTabel()
        self.size = 1

    def __str__(self):
        cur = self.head
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
        return self.head.value

    def insert_in_open_scope(self, key, value) -> Tuple[bool, Any]:
        if key in self.head.content:
            return False, self.head.content[key]
        self.head.content[key] = value
        return True, value

    def traverse(self, _id):
        # This is head
        stack_node = self.peek()
        for i in range(self.getSize()-1):
            val = stack_node.try_fetch_id(_id)
            if not val is None:
                return val  
               
            stack_node = stack_node.next


    # Push a value into the stack.
    def open_scope(self):
        node = SymbolTabel()
        node.next = self.head
        self.head = node
        self.size += 1
 
    # Remove a value from the stack and return.
    def close_scope(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head
        self.head = self.head.next
        self.size -= 1
        return remove.value

    @property
    def current(self):
        return self.head
 
    