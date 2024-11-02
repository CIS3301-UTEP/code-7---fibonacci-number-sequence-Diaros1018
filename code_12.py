
def get_fibonacci_number(position):
   if position == 1:
       return 1
   elif position == 2:
       return 1
   else:
       return get_fibonacci_number(position - 1) + get_fibonacci_number(position - 2)
   
def get_fibonacci_number_sequence(number):
    return [get_fibonacci_number(i) for i in range (1, number + 1)]
   

if __name__ == "__main__":
    
    n = 7 
    print(f"The fibonacci for {n} number is {get_fibonacci_number_sequence(n)} ")
    