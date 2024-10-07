from operators import *

# IMPURE CESS PIT #
def expect(expected, result):
    print(f"Expecting {expected}, Got: {result}")


def main():
    operation = LOG_AND(TRUE)(TRUE)(INCREMENT)(DECREMENT)
    operation2 = LOG_AND(TRUE)(FALSE)(INCREMENT)(DECREMENT)

    print(operation(4))  # Expecting:: 5
    print(operation2(4)) # Expecting:: 3
    print("TESTS")
    print(LOG_AND(TRUE)(TRUE)(1)(2))
    print(LOG_TRAND(TRUE)(TRUE)(TRUE)(1)(0))
    expect(1, LOG_TRAND(TRUE)(TRUE)(TRUE)(1)(0))
    expect(0, LOG_TRAND(TRUE)(TRUE)(FALSE)(1)(0))
    expect(0, LOG_TRAND(TRUE)(FALSE)(TRUE)(1)(0))
    expect(0, LOG_TRAND(FALSE)(TRUE)(TRUE)(1)(0))
    expect(0, LOG_TRAND(FALSE)(FALSE)(FALSE)(1)(0))

    print("\nNEW TRAND")
    expect(0, LOG_TRAND_2(TRUE)(FALSE)(TRUE)(1)(0))
    expect(0, LOG_TRAND_2(FALSE)(TRUE)(TRUE)(1)(0))
    expect(0, LOG_TRAND_2(FALSE)(TRUE)(FALSE)(1)(0))
    expect(0, LOG_TRAND_2(FALSE)(FALSE)(FALSE)(1)(0))
    expect(1, LOG_TRAND_2(TRUE)(TRUE)(TRUE)(1)(0))

if __name__ == '__main__':
    main()