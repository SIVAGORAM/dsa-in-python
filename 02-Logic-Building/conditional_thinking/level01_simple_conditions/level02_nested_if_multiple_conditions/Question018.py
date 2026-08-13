def main():
    # Question 18: Take an alphabet character and check
    # if it lies between 'a' and 'm' or 'n' and 'z'.
    ch = 'h'

    if ch >= 'a' and ch <= 'm':
        print("Between a and m")
    elif ch >= 'n' and ch <= 'z':
        print("Between n and z")
    else:
        print("Not a lowercase alphabet")


if __name__ == "__main__":
    main()


"""
Explanation:
The value stored in `ch` is the input that the conditions work on.

The first condition checks whether `ch` is between 'a' and 'm':
`ch >= 'a' and ch <= 'm'`

The second condition checks whether `ch` is between 'n' and 'z':
`ch >= 'n' and ch <= 'z'`

If neither condition is true, the character is not a lowercase
alphabet character in the specified ranges.

Only the branch whose condition becomes true prints its message.
"""