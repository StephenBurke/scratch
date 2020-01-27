#arr = [48, 51, 405, 235]
#summed = sum(arr)
#avg = summed/4
#print('average = ' + str(avg))

# An example of a recursive function to
# find the factorial of a number

def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))
        
num = 4
print("The factorial of", num, "is", calc_factorial(num))		

##########
# walrus example

sample_data = [ 
    {"userId": 1,  "name": "rahul", "completed": False}, 
    {"userId": 1, "name": "rohit", "completed": False}, 
    {"userId": 1,  "name": "ram", "completed": False}, 
    {"userId": 1,  "name": "ravan", "completed": True} 
] 
  
print("With Python 3.8 Walrus Operator:")  
for entry in sample_data:  
    if name := entry.get("name"): 
        print(f'Found name: "{name}"') 
  
print("Without Walrus operator:") 
for entry in sample_data: 
    name = entry.get("name") 
    if name: 
        print(f'Found name: "{name}"')

print('study')


