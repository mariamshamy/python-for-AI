
######################################### one ##############################################
class Queue:
    def __init__(self):
        self.list=[]
        print("queue class !!")
    
    def insert(self,v):
        print("value inserted ")
        self.list.append(v)
        
    def pop(self):
        if self.is_empty() : 
            print("operation can not be done - queue is empty -")
            return None
  
        else:
            last=self.list[0]
            self.list.pop(0)  
            return last 
            
    def is_empty(self):
        return False if len(self.list) != 0 else True


######################################### three ##############################################
class QueueOutOfRangeException(Exception):
    pass


class NamedQueue(Queue):
    registry = {}
     
    def __init__(self,name,msize):
        super().__init__()
        self.name=name
        NamedQueue.registry[name]= self
        self.msize=msize
    
    def insert(self, v):
        if self.msize == len(self.list):
            raise QueueOutOfRangeException(f"queue {self.name} is full")
        else:
            print("insertion done")
            self.list.append(v)
######################################### four ##############################################          
    @classmethod
    def get_queue(cls, name):
        return cls.registry.get(name)

    
######################################### two ##############################################
# q1=Queue()

# print(q1.is_empty())
# q1.insert(22)
# q1.insert(25)
# q1.insert(27)
# q1.insert(29)

# print(q1.is_empty())
# print(q1.pop())
# print(q1.pop())
# print(q1.pop())
# print(q1.pop())


# print(q1.is_empty())
# print(q1.pop())

# #################################### test named queue 
# nq= NamedQueue("mariamss",3)
# print(nq.is_empty())

# nq.insert(10)
# nq.insert(15)
# nq.insert(12)
# try:
#     nq.insert(60)
# except QueueOutOfRangeException as e:
#     print(e)
    
    
# print(nq.is_empty())

# print(nq.pop())
# print(nq.pop())
# print(nq.pop())
# print(nq.pop())

# print(nq.is_empty())

# #######################################################
# nq2 = NamedQueue("tasks", 2)

# print(nq2.is_empty())

# nq2.insert(5)
# nq2.insert(15)

# print(nq2.is_empty())

# try:
#     nq2.insert(25)
# except QueueOutOfRangeException as e:
#     print(e)

# print(nq2.pop())
# print(nq2.pop())

# print(nq2.is_empty())

# #####################################
# nq3 = NamedQueue("students", 4)

# nq3.insert("Ali")
# nq3.insert("Mona")
# nq3.insert("Sara")

# print(nq3.is_empty())

# print(nq3.pop())

# nq3.insert("Omar")
# nq3.insert("Nour")

# try:
#     nq3.insert("Ahmed")
# except QueueOutOfRangeException as e:
#     print(e)
    
    
# print(nq3.pop())
# print(nq3.pop())


nq1 = NamedQueue("first", 3)
nq2 = NamedQueue("second", 5)
nq3 = NamedQueue("third", 2)

x = NamedQueue.get_queue("second")
print(x.name)
print(x is nq2)