from operators import *
# TRUTH TABLE #
truth_table = {LOG_AND: [(0,0,0),(1,0,0),(0,1,0),(1,1,1)],
               LOG_OR: [(0,0,0),(1,0,1),(0,1,1),(1,1,1)]}

tobool = {0: FALSE, 1: TRUE}

# IMPURE CESS PIT #
def expect(expected, result):
    print(f"Expecting {expected}, Got: {result}")

def test_operator(operation, label=None):
    if label is not None:
        print(f"=== {label} ===".upper())
    truths = truth_table[operation]

    def do():
        for truth in truths:
            print(truth, end="; ")
            expected = truth[2]
            bool_1 = tobool[truth[0]]
            bool_2 = tobool[truth[1]]
            expect(expected, operation(bool_1)(bool_2)(1)(0))

    return do