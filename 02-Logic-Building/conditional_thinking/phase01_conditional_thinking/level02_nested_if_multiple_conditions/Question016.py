def main():
    # Question 16: Check voting eligibility for a given age (18+).
    age = 19

    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")


if __name__ == "__main__":
    main()


"""
Explanation:
The value stored in `age` is the input that the condition works on.

The condition `age >= 18` checks whether the age is 18 or above.

- If `age >= 18` is True → "Eligible to vote"
- Otherwise → "Not eligible to vote"

Only the branch whose condition becomes true prints its message.
"""