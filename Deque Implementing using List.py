class Deque:

    def __init__(self):
        self.front = None
        self.rear = None
        self.items = []

    def is_empty(self):
        return len(self.items)==0
    
    def insert_front(self , data):
        self.items.insert(0 , data)
    
    def insert_rear(self , data):
        self.items.append(data)

    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque Undeflow")
        else:
            self.items.pop(0)

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque Undeflow")
        else:
            self.items.pop()

    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque Undeflow")
        else:
            return self.items[0]
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque Undeflow")
        else:
            return self.items[-1]
        
    def size(self):
        return len(self.items)
    
dq = Deque()
dq.insert_front(10)
dq.insert_front(20)
dq.insert_front(30)
dq.insert_rear(40)
dq.insert_rear(50)

print("Front Value = " , dq.get_front() , "Rear Value = " , dq.get_rear() , "Length of Deque = " , dq.size())
dq.delete_front()

print("Front Value = " , dq.get_front() , "Rear Value = " , dq.get_rear(), "Length of Deque = " , dq.size())

dq.delete_rear()
print("Front Value = " , dq.get_front() , "Rear Value = " , dq.get_rear(), "Length of Deque = " , dq.size())


    

        