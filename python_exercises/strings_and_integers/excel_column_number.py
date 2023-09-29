﻿# Excel Column Number
# Given a string that represents the column title as appears in an Excel sheet, return its corresponding column number.

# But how does the Excel column numbering actually work? Well, the column number is like decimal number, but with base (radix) 26 and "digits" A-Z. Read more about number bases. Let's look at the exact numbers:

# Excel   Decimal
#     A   1
#    ..
#     Z   26
# The 1-"digit" numbers have ended. 2-"digits" numbers start from double first "digit" and go to double last one:

# Excel   Decimal
#     A   1
#    ..
#     Z   26
#    AA   27
#    ..
#    AZ   52
#    BA   53
#    ..
#    BZ   78
#    CA   79
#    ..
#    ..
#    ZZ   702
# Now it's turn for 3-"digit" numbers...

# Input: A string (str).

# Output: An integer (int).

# Examples:

# assert column_number("A") == 1
# assert column_number("Z") == 26
# assert column_number("AB") == 28
# assert column_number("ZY") == 701

# Precondition: Non empty, only upper case, only English letters

################################################ SOLUTION#####################################################
def column_number(name: str) -> int:
    col_num = 0
    for i in name:
        col_num = col_num * 26 + ord(i) - 64
    return col_num


print("Example:")
print(column_number("AA"))
################################################### OR########################################################


def column_number(name: str) -> int:
    import string
    collector = []
    for e in range(0, len(name)):
        collector.append((string.ascii_uppercase.index(
            name[e]) + 1)*(26**(len(name) - (e+1))))
    return sum(collector)


################################################### OR########################################################
COLUMNS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def column_number(name: str) -> int:

    if len(name) == 1:
        return COLUMNS.index(name) + 1
    else:
        recursion = column_number(name[1:])

    return recursion + (COLUMNS.index(name[0])+1) * len(COLUMNS) ** (len(name)-1)
################################################### OR########################################################
################################################### OR########################################################
