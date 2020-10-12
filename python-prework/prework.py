#Question 1: Write a function to print "Hello USERNAME"

def hello_name(user_name):
    print("Hello," + user_name.title() + "!")

hello_name("George")

def hello_name2(user_name):
    print(f"Hello, {user_name}!") 

hello_name2("George")







#Question 2: Write the first 100 odd numbers in Python 

i = 1
n = 100

while i < n:
    print(i)
    i+=2

#Question 3: Write a function, max_num_in_list to return the max number in a list 

def max_num_in_list(a_list):
    print(max(a_list))

list1 = [19, 10, 67, 9, 1]

max_num_in_list(list1)

#Question 4: Write a function to return if the given year is a leap year

def is_leap_year(a_year):
    year = int(input("Enter a year:"))

    return year %4 == 0 and not year %100 == 0 or year %400 == 0

print(is_leap_year(2000))


#Question 5: Write a function to check to see if all numbers in a list are consecutive numbers

def is_consecutive(a_list):
    return a_list == list(range(min(a_list), max(a_list)+1))

print(is_consecutive([5,6,7,8,9,10]))   #True 
print(is_consecutive([1,4,9,10,11,12]))  #False

    








  


    






