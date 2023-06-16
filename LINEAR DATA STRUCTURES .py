#!/usr/bin/env python
# coding: utf-8

# Delete the elements in an linked list whose sum is equal to zero

# In[1]:


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def delete_zero_sum(head):
    dummy = Node(0)  
    dummy.next = head
    prefix_sum = 0
    prefix_sum_map = {}
    current = dummy

    while current:
        prefix_sum += current.data

        if prefix_sum in prefix_sum_map:
            prev = prefix_sum_map[prefix_sum].next
            temp = prefix_sum + prev.data

            while temp != prefix_sum:
                del_node = prev.next
                temp += del_node.data
                del prefix_sum_map[temp]
                prev.next = del_node.next

        else:
            prefix_sum_map[prefix_sum] = current

        current = current.next

    return dummy.next


# Reverse a linked list in groups of given size

# In[2]:


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_groups(head, k):
    if not head or not head.next or k == 1:
        return head

    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    i = 0

    while curr:
        i += 1

        if i % k == 0:
            prev = reverse_subgroup(prev, curr.next)
            curr = prev.next
        else:
            curr = curr.next

    return dummy.next

def reverse_subgroup(prev, next_node):
    last = prev.next
    curr = last.next

    while curr != next_node:
        last.next = curr.next
        curr.next = prev.next
        prev.next = curr
        curr = last.next

    return last


# Merge a linked list into another linked list at alternate positions:

# In[3]:


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def merge_alternate(head1, head2):
    if not head1:
        return head2

    if not head2:
        return head1

    curr1 = head1
    curr2 = head2

    while curr1 and curr2:
        next1 = curr1.next
        next2 = curr2.next

        curr1.next = curr2
        curr2.next = next1

        curr1 = next1
        curr2 = next2

    return head1


# Count pairs with a given sum in an array:

# In[4]:


def count_pairs_with_sum(arr, target_sum):
    count = 0
    complements = {}

    for num in arr:
        complement = target_sum - num

        if complement in complements:
            count += complements[complement]

        if num in complements:
            complements[num] += 1
        else:
            complements[num] = 1

    return count


# Find duplicates in an array:

# In[5]:


def find_duplicates(arr):
    duplicates = []
    for num in arr:
        if arr[abs(num)] >= 0:
            arr[abs(num)] = -arr[abs(num)]
       


# Find the Kth largest and Kth smallest number in an array:

# In[6]:


import heapq

def find_kth_largest_smallest(arr, k):
    k_largest = heapq.nlargest(k, arr)[-1]
    k_smallest = heapq.nsmallest(k, arr)[-1]
    return k_largest, k_smallest


# Move all the negative elements to one side of the array:

# In[7]:


def move_negative_elements(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left += 1
        elif arr[left] >= 0 and arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] >= 0 and arr[right] >= 0:
            right -= 1

    return arr


# Reverse a string using a stack data structure:

# In[8]:


def reverse_string(string):
    stack = []
    for char in string:
        stack.append(char)

    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string


# Evaluate a postfix expression using a stack:

# In[9]:


def evaluate_postfix(expression):
    stack = []
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y}

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[token](operand1, operand2)
            stack.append(result)

    return stack[0]


# Implement a queue using the stack data structure:

# In[10]:


class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if self.stack2:
            return self.stack2.pop()

        return None


# In[ ]:




