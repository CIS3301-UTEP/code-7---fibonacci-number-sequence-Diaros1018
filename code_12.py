import random
def get_fibonacci_number(position):
   if position <= 1:
       return 1
   return get_fibonacci_number(position - 1) + get_fibonacci_number(position - 2)
   
def get_fibonacci_number_sequence(number):
    return [get_fibonacci_number(i) for i in range (number)]
def check_list():
    return True
    

if __name__ == "__main__":
    check_list ()
    # n = 7 
    # print(f"The fibonacci for {n} number is {get_fibonacci_number_sequence(n)} ")
    