# BOOLEANS #
TRUE = lambda x: lambda y: x
FALSE = lambda x: lambda y: y

# LOGICAL OPERATORS #
LOG_NOT = lambda b: b(FALSE)(TRUE)
LOG_AND = lambda b1: lambda b2: b1(b2)(FALSE)
LOG_NAND = lambda b1: lambda b2: LOG_NOT(LOG_AND(b1)(b2))
LOG_OR = lambda b1: lambda b2: b1(b2)(TRUE)
LOG_NOR = lambda b1: lambda b2: LOG_NOT(LOG_OR(b1)(b2))

# OPERATIONS #
INCREMENT = lambda x: x+1
DECREMENT = lambda x: x-1

# APPLYING LOGIC & OPERATORS #
operation = LOG_AND(TRUE)(TRUE)(INCREMENT)(DECREMENT)
operation2 = LOG_AND(TRUE)(FALSE)(INCREMENT)(DECREMENT)

# IMPURE CESS PIT #
def main():
    print(operation(4))  # Expecting:: 5
    print(operation2(4)) # Expecting:: 3

if __name__ == '__main__':
    main()