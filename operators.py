from booleans import *

# LOGICAL OPERATORS #
LOG_NOT = lambda b: b(FALSE)(TRUE)
LOG_AND = lambda b1: lambda b2: b1(b2)(FALSE)
LOG_TRAND = lambda b1: lambda b2: lambda b3: b1(b2(b3)(FALSE))(FALSE)
LOG_NAND = lambda b1: lambda b2: LOG_NOT(LOG_AND(b1)(b2))
LOG_OR = lambda b1: lambda b2: b1(b2)(TRUE)
LOG_NOR = lambda b1: lambda b2: LOG_NOT(LOG_OR(b1)(b2))

# ARITHMETIC OPERATIONS #
INCREMENT = lambda x: x+1
DECREMENT = lambda x: x-1
ADD = lambda x: lambda y: x + y
SUBTRACT = lambda x: lambda y: x - y
MULTIPLY = lambda x: lambda y: x*y
DIVIDE = lambda x: lambda y: x/y
EXPONENT = lambda x: lambda y: x**y