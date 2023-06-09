#create stack using list
class St:
    def __init__(self):
        self.stack = []
    def push(self,item):
        self.stack.append(item)
        print(self.stack)
    def pop(self):
        if len(self.stack ) > 0:
            self.stack.pop()
            print(self.stack)
        esle: None

    def peek(self):
        if len(self.stack) >0:
            print(self.stack[len(self.stack)-1])
            print(self.stack)
        else:None

    def __str__(self):
        str(self.stack)

st1 = St()
st1.push(1)
st1.push(2)
st1.push(3)
st1.push(4)
st1.pop()
st1.peek()




