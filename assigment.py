#!/usr/bin/env python
# coding: utf-8

# 1. What are the two values of the Boolean data type? How do you write them?
# 
# 
# Ans:-
#      True and False are two values of the boolean data types. we have to use capital T and F and with the rest of the word in lowercase.

# In[3]:


a=True
b=False
print(a,type(a))
print(b,type(b))


# 2. What are the three different types of Boolean operators?.
# 
# 
# Ans:-
#     The Three different types of boolean in python are : are,and,not
# 

# In[4]:


a=100
b=200
print(a>50 and b>100)
print(a>200 or b>100)
print(not(a>10))


# 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
# 
# 
# Ans:-
#     The Truth Tables for the boolean table are as follows:-
#     
#   * Truth table for AND operator
#         True and True is True
#         True and False is False
#         False and True is False
#         False and False is False
#         
#   * Truth table for OR operator
#         True and True is True
#         True and False is True
#         False and True is True
#         False and False is False
#         
#  * Truth table for NOT operator
#        True not is False False not is True
#         
# 

# 4. What are the values of the following expressions?
# (5 > 4) and (3 == 5)
# not (5 > 4)
# (5 > 4) or (3 == 5)
# not ((5 > 4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)
# 
# 
# Ans:-
#     
#     
# 

# In[3]:


print((5>4)and(3==5))
print(not(5>4))
print((5>4)or(3==5))
print(not((5>4)or(3==5)))
print((True and True)and (True==False))
print((not False)or(not True))


# 5. What are the six comparison operators ?
# 
# 
# Ans:-
# The six comparision operators avaliable in python are:-
#  ==,!=,<,>,<=,=>
#  
# 
# 
# 
# 

# 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
# 
# 
# Ans:-
#  
#  == is the equal to operator that compares two values and evaluates to a boolean,While = is that assignment operator that stores a value in a variable.

# 7. Identify the three blocks in this code:
# spam = 0
# if spam == 10:
# print('eggs')
# if spam > 5:
# print('bacon')
# else:
# print('ham')
# print('spam')
# print('spam')
# 
# 
# Ans:-
# In python , code block refers to a collection of code that is the same block or indent this is most commonly found in classes, functions, and loops.
# 
# 

# In[4]:


spam=0
if spam==10:
    print('eggs')
if spam>5:
    print('bacon')
else:
    print('hum')
    print('spam')
    print('spam')


# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
# 
# 
# Ans:-
#  
# 

# In[17]:


def spamCode(spam):
    if spam ==1:
        print('hello')
    elif spam ==2:
        print('howdy')
    else:
        print('Greetings')
        
spamCode(1)
spamCode(2)
spamCode(3)


# 9. If your programme is stuck in an endless loop, what keys you’ll press?
# 
# 
# Ans:-
#  
#    Press Ctrl-c to stop a program stuck in an infinite loop.
#    

# 10. How can you tell the difference between break and continue?
# 
# Ans:-
# 
#    The break statement will move the execution outside the loop is break condition is satisfied where as the continue statement will move the execution to the start of the loop.
# 

# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# 
# Ans:-
#       
#       The differences are as follows:-
#           1.The range(10)call range from 0 to 9(but not incide 10)
#           2.the range (0,10) explicity tells the loop to start at 0 .
#           3. the range (0,10,1) explicity tells the loop to increase the variable by 1 on each iteration.
#           
#      

# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
# 
# 
# Ans:-
#     

# In[23]:


print('-'*10,'Using For Loop','-'*10)
for i in range(1,11):
    print(i, end=" ")
print('\n')
print('-'*10,'Using While Loop','-'*10) 
i=1
while i<=10:
    print(i, end=" ")
    i+=1


# 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# 
# 
# Ans:-
# 
#  This functin can be called with spam.bacon()
