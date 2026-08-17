def isVowel(ch):
    lower = ch.lower()
    return lower == 'a' or lower == 'e' or lower == 'i' or lower == 'o' or lower == 'u'


def main():
    # Question 9: Take a character and check if it's a vowel or consonant.
    ch = 'A'

    if ch.isalpha():
        if isVowel(ch):
            print("Vowel")
        else:
            print("Consonant")
    else:
        print("Not an alphabet")


if __name__ == "__main__":
    main()


"""
Explanation:
The value stored in `ch` is the input that the conditions work on.

The helper function `isVowel()` converts the character to lowercase
and checks whether it is one of `a`, `e`, `i`, `o`, or `u`.

The `ch.isalpha()` condition first checks whether the character is
an alphabet.

- If it is an alphabet, `isVowel()` checks whether it is a vowel.
- If it is not a vowel, it is a consonant.
- If it is not an alphabet, "Not an alphabet" is printed.

Only the branch whose condition becomes true prints its message.
"""