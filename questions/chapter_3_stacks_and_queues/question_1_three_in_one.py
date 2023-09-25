"""
Three in One:
Describe how you could use a single array to implement three stacks.

I can create an object called MyStack. I used a single array to implement the required logic.

"""
from questions.chapter_3_stacks_and_queues.my_stack import MyStack


def using_my_stack():
    my_stack = MyStack([1, 2, 3, 4, 5])

    my_stack.push(10)
    print(my_stack.peek())
    print(my_stack.peek())
    print(my_stack.is_empty())
    print(my_stack)
