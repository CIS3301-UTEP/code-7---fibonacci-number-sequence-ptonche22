def get_fibonacci_number(position):
    if position == 1 or position == 2:
        return 1
#with recursion
    return get_fibonacci_number(position - 1) + get_fibonacci_number(position - 2)

def get_fibonacci_number_sequence(number):
    #list
    fibonacci_sequence = []
    for i in range(1, number + 1):
        fibonacci_sequence.append(get_fibonacci_number(i))
        return fibonacci_sequence

if __name__ == "__main__":
    #test code
    position = 8
    print(f"The Fibonacci number at position {position} is: {get_fibonacci_number(position)}")