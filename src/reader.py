import sys

class List:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def print_list(head):
    curr = head
    string = ""
    while curr:
        string += str(curr.data)
        string += " "
        curr = curr.next
    string += ""
    print(string)

def isspace(char):
    return char.isspace()

def isparen(char):
    return char in ['(', ')']

def iseof(char):
    return char == "ß" # alt + s

def get_tokens():
    curr = None
    head = List(None, curr)

    next = sys.stdin.read(1)
    while not iseof(next):
        token = ""
        while isspace(next):
            next = sys.stdin.read(1)
        if isparen(next):
            token += next
            next = sys.stdin.read(1)
        else:
            while not isspace(next) and not isparen(next) and not iseof(next):
                token += next
                next = sys.stdin.read(1)
                
        if not curr:
            curr = List(token, None)
            head.next = curr
        else:
            curr.next = List(token, None)
            curr = curr.next
        print_list(head.next)




if __name__ == "__main__":
    token_list = get_tokens()
    print_list(token_list)