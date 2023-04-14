# A function named concatenate_args that takes any number of string 
# arguments in positional arguments format and concatenates them into a single string

def concatenate_args(*names):
   string=""
   for name in names:
     string+=(f"{name} ")
   return string
 

# A function named concatenate_kwargs that takes any number of string arguments in keyword arguments 
#  format and concatenates them into a single string
def concatenate_kwargs(**arguments):
   long=""
   for key,value in arguments.items():
     long+=(f"{key}, {value} ")
   return long

