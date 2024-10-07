from operators import *

# IMPURE CESS PIT #
def main():
    operation = LOG_AND(TRUE)(TRUE)(INCREMENT)(DECREMENT)
    operation2 = LOG_AND(TRUE)(FALSE)(INCREMENT)(DECREMENT)

    print(operation(4))  # Expecting:: 5
    print(operation2(4)) # Expecting:: 3

if __name__ == '__main__':
    main()