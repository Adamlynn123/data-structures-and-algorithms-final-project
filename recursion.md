# Recursion

Recursion is when a function calls itself. It is used when you need to loop through a function to find a desired result.

## Real World Example

Lets say there are people in a line each with their own number. The person in the front of the line has number 1, the person in second place has number 2 and so forth. Now lets say that there are ten people in the line and each of them wants to figure out the total of all numbers in front of them. So if you are in third place, you will add 2 and 1 because they are the numbers of the people in front of you.

If you are in tenth place, that may take a lot of brain power to add up all numbers in front of you so a simple method can be used to figure it out a lot easier. 

The method goes like this, for the person in tenth place, all you have to do is take the value for the person in ninth place and add ten to it. The same can be applied for every person in the list until the first person in line.
1. The person in second place would take 1 and the add their value of 2 to it, to make 3. 
2. Then the person in third place can take the total value of the person in second and add 3 too it which would be 3 (second place total value) + 3 (third place given value) = 6. 

Six would then be the total value of the person in 3rd place. 

This is in essence, how recursion works. It calls a function multiple times until it reaches the base case which in our example, the base case would be the person in first place.

## Python Programming Example

In this Python Programming example, we will use recursion to complete a similar problem to the real world example where it will take the sum of all numbers in front. 
```python
# create the sum recursion formula
def sum_recursion(n):
    # base case
    if n <= 0:
        return 0

    # use recursion to call function again and add to current number.
    else:
        return sum_recursion(n-1) + n
print(sum_recursion(10)) #55
```

## Challenge for you!
For you to understand recursion or anything in programming for that matter, it is strongly advised that you try out a problem for yourself. The problem that I would like you to solve is involving the Fibonacci sequence. The short explanation for people who are not aware of the Fibonacci sequence is that it is just the sum of the 2 numbers previous of the current number.

Your goal is to write a function that will find the number in the Fibonacci sequence when taking a specific index as a parameter. 

* 0, 1, 1, 2, 3, 5, 8, 13, 21 (Fibonacci sequence)
* 0, 1, 2, 3, 4, 5, 6, 7, 8 (Index sequence)

For example, if you were going to find the fibonacci number for index 6, you would get 8 because 8 is the 6th index in the fibonacci sequence.
