def hello(*names):
    for name in names:
        print(f"Hello {name}") 

def sum(*numbers):
    answer=0
    for number in numbers:
        answer+=number
    return answer    

# write a function that accepts any number of integers and returns the result of multiply all off them
def multiply(*digits):
    mult= 1
    for no in digits:
        mult*=no
    return mult

 # functions taking in keyword positional args

def student_attributes(**kwargs):
  for key,value in kwargs.items():
   print (f"{key}:{value}")

# functions with a default value
def my_country(country="Burundi"):
   print(f"Hello from {country}")   

