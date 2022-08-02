class MyCircularQueue:
    def __init__(self, size: int):
        self.queue = [None]*size
        self.size = size
        self.rear = -1
        self.front = -1

    def enqueue(self, value: int) -> bool:
        if is_full()!=1:
            if (self.rear==self.size-1) and self.queue[self.rear-1]==None:
                

    def dequeue(self) -> bool:
        # Write code here

    def get_front(self):
        return self.queue[self.front]

    def get_rear(self):
        return self.queue[self.rear]

    def is_empty(self):
        if (self.front==-1 and self.rear==-1):
            return 1
        elif (self.front+1==self.rear) and self.rear==self.size-1:
            self.front=-1
            self.rear=-1
            return 1
        else :
            return 0

    def is_full(self):
        if (self.front==0 and self.rear==self.size-1) or self.rear==self.front+1:
            return 1
        else:
            return 0


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
data = []
for item in input().split(','):
    item = item.strip()
    if item == '-':
        data.append([])
    else:
        data.append([int(item)])
obj = MyCircularQueue(data[0][0])
result = []
for i in range(len(operations)):
    if i == 0:
        result.append(None)
    elif operations[i] == "enqueue":
        result.append(obj.enqueue(data[i][0]))
    elif operations[i] == "get_rear":
        result.append(obj.get_rear())
    elif operations[i] == "get_front":
        result.append(obj.get_front())
    elif operations[i] == "dequeue":
        result.append(obj.dequeue())
    elif operations[i] == "is_full":
        result.append(obj.is_full())
    elif operations[i] == "is_empty":
        result.append(obj.is_empty())

print(result)



/*class Solution:
    """This class implements linear queue.
      Attributes:
          stack: A list which maintains the content of stack.
          queue: A list which maintains the content of queue.
          top: An integer which denotes the index of the element at the top of the stack.
          front: An integer which denotes the index of the element at the front of the queue.
          rear: An integer which denotes the index of the element at the rear of the queue.
          size: An integer which represents the size of stack and queue.
      """

    # Write your code here
    def __init__(self, size):
        """Inits Solution with stack, queue, size, top, front and rear.
        Arguments:
          size: An integer to set the size of stack and queue.
        """
        self.stack = [None]*size
        self.queue = [None]*size
        self.size = size
        self.top = -1
        self.rear = -1
        self.front = -1

    def is_stack_empty(self):
        """
        Check whether the stack is empty.
        Returns:
          True if it is empty, else returns False.
        """
        if self.top==-1:
            return 1
        else :
            return 0

    def is_queue_empty(self):
        """
        Check whether the queue is empty.
        Returns:
          True if it is empty, else returns False.
        """
        if (self.front==-1 and self.rear==-1):
            return 1
        elif (self.front>self.rear):
            self.front=-1
            self.rear=-1
            return 1
        else :
            return 0

    def is_stack_full(self):
        """
        Check whether the stack is full.
        Returns:
          True if it is full, else returns False.
        """
        if self.top==self.size-1:
            return 1
        else:
            return 0

    def is_queue_full(self):
        """
        Check whether the queue is full.
        Returns:
          True if it is full, else returns False.
        """
        if (self.rear==self.size-1):
            return 1
        else:
            return 0

    def push_character(self, character):
        """
        Push the character to stack, if stack is not full.
        Arguments:
            character: A character that will be pushed to the stack.
        """
        if self.is_stack_full()==1:
            print("Stack is full")
        else:
            self.top+=1
            self.stack[self.top]=character


    def enqueue_character(self, c):
        """
        Enqueue the character to queue, if queue is not full.
        Arguments:
            character: A character that will be enqueued to queue.
        """
        if self.is_queue_full()==1:
            print("Queue overflow")
        elif self.is_queue_empty()==1:
            self.front+=1
            self.rear+=1
            self.queue[self.front]=c
        else:
            self.rear+=1
            self.queue[self.rear]=c

            
            

    def pop_character(self):
        """
        Do pop operation if the stack is not empty.
        Returns:
          The data that is popped out if the stack is not empty.
        """
        if self.is_queue_empty()==1:
            print("Stack is Empty")
        else:
            a=self.stack[self.top]
            self.stack[self.top]=None
            self.top-=1
            return a

    def dequeue_character(self):
        """
        Do dequeue operation if the queue is not empty.
        Returns:
          The data that is dequeued if the queue is not empty.
        """
        if self.is_queue_empty()==1:
            print("Queue is empty")
        else:
            b=self.queue[self.front]
            self.queue[self.front]=None
            self.front+=1
            return b
            


# read the string text
text = input()

# find the length of text
length_of_text = len(text)

# Create the Solution class object
solution = Solution(length_of_text)

# push/enqueue all the characters of string text to stack
for i in text:
    solution.push_character(i)
    solution.enqueue_character(i)
    

is_palindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both characters
If the comparison fails, set is_palindrome as False.
'''
for index in text:
    if solution.pop_character()==solution.dequeue_character():
        is_palindrome = True
    else :
        is_palindrome = False
        break


# finally print whether string text is palindrome or not.
if is_palindrome==True:
    print("The word, " + text + ", is a palindrome.")
else:
    print("The word, " + text + ", is not a palindrome.")


