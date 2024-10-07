from operators import *
from tests import test_operator


def main():
    test_or = test_operator(LOG_OR, "or")
    test_or()

    test_and = test_operator(LOG_AND, "and")
    test_and()


if __name__ == '__main__':
    main()