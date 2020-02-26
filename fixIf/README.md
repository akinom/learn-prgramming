# Depending on age print approriate response

## The Task ## 
Print resposne depending on age; respond differently for an age lower than 10, lower than 100, abiove 100, and above 2000.


### The code below has all sorts of problems ###



```python
age_str = input('How old are you ? ')
age = int(age_str)

if (age < 10):
    print("Hey kiddo")
elif age > 100:
    print("You are really old")
elif age > 2000:
    print("Are you a mummy?")
elif (age < 100):
    print("You have reached maturity")
```

### Simplify Testing ###

Instead of testing this manually for several values you can define a python function and call it several times with a different value for age. 


```python
def age_appropiate_response(age): 
    if (age < 10):
        print("Hey kiddo")
    elif age > 100:
        print("You are really old")
    elif age > 2000:
        print("Are you a mummy?")
    elif (age < 100):
        print("You have reached maturity")
```

Think of this method as a recipe that you can apply to any age like you see below


```python
test_age = 9 
print("Age: " + str(test_age))
age_appropiate_response(test_age)    
# this now execured the age_appropiate_response method with tst_age (9) assigned top age

test_age = 50 
print("Age: " + str(test_age))
age_appropiate_response(test_age)    
# this now execured the age_appropiate_response method with tst_age (100) assigned top age
```

    Age: 9
    Hey kiddo
    Age: 50
    You have reached maturity


Instead of repeating the same statements for different age values, lets define a list of interesting age values and use a for loop to perform the statements for each of the values in the list:


```python
for test_age in [1, 10, 11, 50, 99, 100, 101, 2000, 2001]: 
    print("Age: " + str(test_age))
    age_appropiate_response(test_age)    
```

    Age: 1
    Hey kiddo
    Age: 10
    You have reached maturity
    Age: 11
    You have reached maturity
    Age: 50
    You have reached maturity
    Age: 99
    You have reached maturity
    Age: 100
    Age: 101
    You are really old
    Age: 2000
    You are really old
    Age: 2001
    You are really old


This is not what should happen. Nothing is printed for the age of 100, the test (age > 2000) is never triggered since any number greater 2000 is also bigger than 100. 

### Fix the  code ###


```python
def age_appropiate_response(age): 
    if (age < 10):
        print("Hey kiddo")
    elif age < 100:
        print("You have reached maturity")
    elif age > 2000:
        print("Are you a mummy?")
    elif (age >= 100):
        print("You are really old")
        
for test_age in [1, 10, 11, 50, 99, 100, 101, 2000, 2001]: 
    print("Age: " + str(test_age))
    age_appropiate_response(test_age)
```

    Age: 1
    Hey kiddo
    Age: 10
    You have reached maturity
    Age: 11
    You have reached maturity
    Age: 50
    You have reached maturity
    Age: 99
    You have reached maturity
    Age: 100
    You have reached maturity
    Age: 101
    You are really old
    Age: 2000
    You are really old
    Age: 2001
    Are you a mummy?


### Make it more readable ###

This is correct code now, but it is not easy to understand. Here a more readable version: 


```python
def age_appropiate_response(age): 
    if (age < 10):
        print("Hey kiddo")
    elif age < 100:
        print("You have reached maturity")
    elif age <= 2000:
        print("You are really old")
    else: 
        print("Are you a mummy?")
```
