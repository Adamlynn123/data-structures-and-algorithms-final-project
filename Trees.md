# Trees

Trees are another type of data structure that unlike linked lists, are non-linear. Trees are structured in a hierarchical manner where you start at the **root node** and make your way down to the **leaf nodes** 

Trees can be a great way to improve performance when searching through a data structure of elements. Here is a list of different basic trees.

* General Tree - A tree with no order or organization with its content.
* Binary Tree - A tree that has no order but is organized with a max of 2 child nodes per node.
* Binary Search Tree(BST) - Like a binary tree but is orderd so numbers less than the parent node go to the left, and numbers that are greater than the parent node go the the right.

## Binary Search Trees

This is the data structure that we will be focusing on as it allows for much quicker performance (O(logn)) when searching through the list.

![binary search tree image](https://miro.medium.com/max/1400/1*4M5MU3CqJYGNExEi5Ttuew.png)

In this binary search tree, `7` is the root node and `2` and `9` are its child nodes. The way binary search trees are structured, you can see that because 2 is less than 7, it is placed on the left and because 9 is greater than 7, it is placed on the right. Now each child of the root has children of its own and they follow the same format. For the `2` node, it has 2 children, those being `1` and `5`. 

This structure may not look like much but it allows for some extremely fast performance when searching through very large data sets with millions of nodes.

## Inserting into A BST

Inserting into a BST is quite a complicated process as it uses recursion, so pay attention to the steps and the code.

Insertion is also very similar to searching through a BST so we wont be giving the steps for searching through a tree as it is just a few changes in the code.

**Note: A Node class must be implemented to create a BST in python.**

1. Call the insert function using a root and new_value.
2. Start by seeing if there is a root. If no root, then place node there.
3. If no root, check to see if the new_value is equal to the root. If it is, then exit function as we already have that value.
4. Check to see if the new_value is greater than or less than the root. If its either of those, use recursion to run the function again with the new root in place of the old one.

```python
def insert(root, value):    # Step 1
	if root is None:        # Step 2
		return Node(value)
	else:
		if root.val == value:   # Step 3
			return root
		elif root.val < value:  # Step 4
			root.right = insert(root.right, value)
		elif root.val > value:                      
			root.left = insert(root.left, value)
	return root
```

### Example: Insertion

That can be a lot to understand so here is an example of how this function works.

We will start by refering to the tree 

![binary search tree image](https://miro.medium.com/max/1400/1*4M5MU3CqJYGNExEi5Ttuew.png)

Lets implement the function to add `8` to the tree. 

1. When the function first starts, it looks at the root and asks if it is None. In this case we have a `7` there so it is not None.
2. Then it checks to see if `7` is equal to our value of `8` which it is not so it moves on to the next if statment.
3. Then it checks to see if `7` is less than our value of `8`, which it is, so we then use recursion to move to the rightmost child node and start the function again.
4. Then call to the function replaces the root which was `previously: 7` to `currently: 9`.
5. It then runs through the function again checking if the root is None which it is not so we move on.
6. Then it checks is `9` is equal to our value `8` which its not so it moves on.
7. Then it checks to see if `9` is less than our value `8`, which it's not so it moves on
8. Then it checks to see if `9` is greater than our value `8` which it is, so it moves to the leftmost child and calls the insert function again.
9. It again replaces the value of `previously: 9` to `currently: none`. The reason it is none is because there is no leftmost child to 9.
10. It checks to see if the root is None which it is so it creates a new node and adds it there.

## Traversing a BST

There are many ways to traverse a BST but in this tutorial we will cover the `inorder traversal`.

Traversing a BST is not as complicated as inserting into a BST as it takes only 3 to 4 steps to complete but still involves recursion.

1. Start at the root and move to the left subtree using recursion.
2. Visit the root.
3. Move through the right subtree using recursion.

```python
def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)
```

### Example: Traversal

We are going to refer to this tree again

![binary search tree image](https://miro.medium.com/max/1400/1*4M5MU3CqJYGNExEi5Ttuew.png)

1. This functions starts at the root and makes its way all the way to the left most node which is `1`.
2. Once it gets to `1`, it attmpts to reccur on the left subtree of `1` but because there is no subtree to the left of `1`, it returns `None`.
3. It then prints `1` and attempts to reccur on the right subtree of `1` but again there is no subtree tho the right of `1`, so it returns `None`.
4. The function then returns back to the root of `1` which is `2`.
5. Because the left subtree of `2` has already been traveresed, it moves on to the right subtree of `2` which starts at `5`.
6. It then moves to the left subtree of `5` but because there is no leftmost subtree of `5`, it prints `5` and moves on to the right subtree of `5`.
7. Again the right subtree of `5` is None, so it moves back up the tree back to `2`. 
8. Since the left and right subtree of `2` has been traversed, it moves back up to the root of `2` which is `7`. 
9. Because `7` is the root of the entire BST, it then completes the rest of the traversal by moving to the right of `7` and completing the same steps over again.

There are more steps after but in the interest of space and time, I am going to leave it at that because the logic and steps are the same as before.
## Test Problems

Now that you have the hang of inserting and traversing through a BST. Here are some tests for you to try to see if your code works.

```python
r = Node(7)
r = insert(r, 2)
r = insert(r, 5)
r = insert(r, 1)
r = insert(r, 9)
r = insert(r, 14)
r = insert(r, 8)

# Inorder traversal
inorder(r)

#Prints
1, 2, 5, 7, 8, 9, 14
```

## Conclusion

Binary Search Trees can be complicated at first but they allow for extreme fast performance that linear based data structures can lack.

The big(0) notation for searching through a BST is O(logn) while searching through a linear based data structure such as a dynamic array, has performance O(n).

One thing that will blow your mind is that thinking about the worst case scenarios for searching through a BST and a dynamic array. If you had 10,000,000 items that you needed to search through, the dynamic array's worst case scenario would be 10,000,000 while BST's worst case scenario would only take `7 steps`!