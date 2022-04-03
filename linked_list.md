# Linked Lists

Linked lists are a lot like arrays in Python except there are a few distinct advantages and disadvantages. 

### Advantages:
 * (Dynamic size) With ordinary arrays, there is an upper limit to how large the list can be as each element in the array is allocated a piece of memory. With linked lists there is  no limit to how large the list can be as it has dynamic size.
* (Inserting and deleting elements from a linked list). In order to insert an element into the middle of an array, it will have to move each item after the insertion point forward by one piece of memory. That can take awhile as room needs to be made for the new element. With linked lists, insertion is does not have this drawback and items can be inserted much easier and quicker.

### Disadvantages
* (Memory access is not available) One of the disadvantages for arrays can also be viewed as an advantage because with elements of arrays being given its own memory location. Searching through the array is fast but linked lists do not have this feature which means you have to start from the head of the list and iterate through each item until you found what you are looking for.

## Inserting into Linked Lists

### Inserting/creating the head
1. Start by creating a new node.
2. Set the "Next" of the new node to the current head.
3. Set the "Prev" of the head to the new node.
4. Set the head to the new node.

Note: you must have a linked list library imported.
```python
new.node = Node           # STEP 1
new_node.next = self.head # STEP 2
self.head.prev = new_node # STEP 3
self.head = new_node      # STEP 4
```

### Inserting into the middle

Inserting into the middle of the linked list is a lot more complicated than inserting into the head. Try your best to understand the steps and see how the code works.

1. Start by creating a new node.
2. Set the "Prev" of the new node to the current node.
3. Set the "Next" of the new node to the node after current node.
4. Set the "Prev" of the node after current node to new node.
5. Set the "Next" of the current node to the new node.

```python
new_node = Node                 #STEP 1
new_node.prev = current         #STEP 2
new_node.next = current.next    #STEP 3
current.next.prev = new_node    #STEP 4
current.next = new_node         #STEP 5
```

### Inserting into the tail

`CHALLENGE: TRY THIS ONE BEFORE LOOKING AT STEPS`

Inserting into the tail is a very similar to inserting into the head. The only thing that is changing is instead of using "Next" in some cases, you would use "Prev" and instead of using the head, you would be using the tail. 

1. Create a new node.
2. Set the "Prev" of the new node to the current tail.
3. Set the "Next" of the tail to the new node.
4. Set the tail to the new node.

```python
new.node = Node           # STEP 1
new_node.prev = self.tail # STEP 2
self.tail.next = new_node # STEP 3
self.tail = new_node      # STEP 4
```

## Removing nodes from Linked Lists

Removing nodes from linked lists are a lot easier than inserting into linked lists.

### Removing the head

1. Set the "Prev" of the node after the head to nothing.
2. Set the head to now be the second node.

```python
self.head.next.prev = None
self.head = self.head.next
```

### Removing the tail

1. Set the "Next" of the node before the tail to nothing.
2. Set the tail to now be the node before.

```python
self.tail.prev.next = None
self.tail = self.tail.prev
```

## Removing from the middle

`CHALLENGE: TRY THIS ONE BEFORE LOOKING AT STEPS!`

Removing from the middle is still a 2 step process. Now that you have an idea at how nodes are removed from the head and tail. I want you to try removing from the middle on your own and after you have tried. You can look at the steps below.

1. Set the node to the right of the current to the node before the current.
2. Set the node to the left of the current to the node after the current.

```python
current.next.prev = current.prev
current.prev.next = current.next
```

## Test Problems

In order to test your new found skills of linked lists, here are some tests for you to try.

Implement this code at the end of your file to see if they pass.

```python
list.insert_head(1)
list.insert_head(3)
list.insert_tail(1)
list.insert_after(1, 4)
list.insert_after(3, 10)
list.insert_tail(5)
list.insert_tail(6)
list.remove(10)
list.remove_tail()
print(list) #[3, 1, 4, 1, 5]
```

After implementing your functions, you should get a list that contains the first 5 digits of PI in order.

## Conclusion

Linked lists are a great way to improve performance when adding items to a list. They allow for better performance when inserting and removing from the front of the list while dynamic arrays cannot say the same. Now what does this mean for Dynamic Arrays? Are they useless? Of course not! Dynamic arrays have their advantages over Linked Lists and will continue to remain in use until they are completely obsolete. 