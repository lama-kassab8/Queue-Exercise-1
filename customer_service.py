# here's a list-based queue:

arriving=[] # create a queue to enqueue customers
serving=[] # create a queue to enqueue all the customers that were dequeued from the arriving queue

def enqueue(customer):
    arriving.append(customer) # enqueue every customer into arriving
    print(f"Arriving: {customer}") # print out the customers that arrived one customer at a time

def dequeue():
    while arriving: # as long as arriving queue is not empty
        customer= arriving.pop(0) # dequeue the first customer that got arrived. With every loop, as the element at the front of the queue gets dequeued, the front's pointer gets updated so now the second element in the list is at index 0 and so forth
        serving.append(customer) # enqueue all the customers that were dequeued to the serving queue
        print(f"Serving: {customer}") # print out the customers that were served one customer at a time
    print("All customers served.") # when teh loop is complete, this means all customers got served

# enque the customers
enqueue("Alice")
enqueue("Bob")
enqueue("Carol")

# serve the customers
dequeue()


# here's a linked-list-based queue:

class ListNode:
    def __init__(self, data):
        self.data= data 
        self.next= None

class LinkedListQueue:
    def __init__(self):
        self.front= None
        self.rear= None

    def enqueue(self,data):
        new_node= ListNode(data) # create a new node for the arriving customer
        if self.front is None: # if the queue is empty, make new_node the front and the rear of the list
            self.front= new_node
            self.rear= new_node
        else: # if there are already customers in the queue
            self.rear.next= new_node # link the current rear to the new node
            self.rear= new_node # update the rear to the new customer
        print(f"Arriving: {data}")

    def dequeue(self):
        if self.front is not None: # if there are customers who arrived
            value= self.front.data # store the name of the customer in value
            self.front= self.front.next # update the self.front pointer to poin to the next customer
            if self.front is None: # if all the customers are served (no more new arrivals)
                self.rear= None # set self.rear to None since now the arriving queue is empty
                print(f"Serving: {value}") # this is the name of the last customer who got served
                print("All customers served.")
            else:
                print(f"Serving: {value}") # print the name of the customers who got served
        else: # this part handles the case in which there are no customers arrived
            print("There are no customers for now.")
            return None
    

queue = LinkedListQueue()

queue.enqueue("Alice")
queue.enqueue("Bob")
queue.enqueue("Carol")

queue.dequeue()
queue.dequeue()
queue.dequeue()