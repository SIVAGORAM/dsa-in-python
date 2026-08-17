def main():
    # Question 29: : Print first n terms of an arithmetic progression (a, d).
    n = 5
    firstTerm = 3
    difference = 4
    for i in range(0, n):
        print(firstTerm + i * difference)


if __name__ == "__main__":
    main()

"""
Explanation:
The value stored in `n` is the input that the conditions or loops work on.
The `for` loop starts with `int i = 0`, keeps running while `i < n` is true, and updates using `i++`.
The print statement shows each value as soon as that value is calculated inside the loop.
"""