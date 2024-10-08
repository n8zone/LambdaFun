from operators import *
from tests import test_operator


def main():
    test_or = test_operator(LOG_OR, "or")
    test_or()

    test_and = test_operator(LOG_AND, "and")
    test_and()

    var = 5
    is_less_than = CMP_LT(var)(6)(TRUE)(FALSE)

    output = LOG_NOT(CMP_EQ(5)(5))("true!!")("false!!")
    print(output)

    output = is_less_than("true")("false")

    print(output)
if __name__ == '__main__':
    main()