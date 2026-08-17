def main():
    # Question 34: Take 24-hour time (hours and minutes) and print whether it is AM or PM.
    hour = 14
    minutes = 30

    if hour < 12:
        print("AM")
    else:
        print("PM")


if __name__ == "__main__":
    main()


"""
Explanation:

The question gives a time in 24-hour format and asks us to determine
whether the time is AM or PM.

In 24-hour time:

Hours 0 through 11 → AM
Hours 12 through 23 → PM


Example:

hour = 14
minutes = 30

We only need to check the hour.

Condition:

hour < 12

14 < 12 → False

Therefore:

PM


Dry Run:

Given:

hour = 14
minutes = 30

Step 1:

Check:

14 < 12

Result:

False

So the `if` block is skipped.


Step 2:

The `else` block executes.

Output:

PM


Another Example:

hour = 9
minutes = 45

Check:

9 < 12 → True

Therefore:

AM


Boundary Example:

hour = 0
minutes = 30

0 < 12 → True

Therefore:

AM


Important Boundary Example:

hour = 12
minutes = 00

12 < 12 → False

Therefore:

PM


Another Boundary Example:

hour = 23
minutes = 59

23 < 12 → False

Therefore:

PM


Test Cases:

1. Input:
   hour = 9
   minutes = 30

   Output:
   AM


2. Input:
   hour = 11
   minutes = 59

   Output:
   AM


3. Input:
   hour = 12
   minutes = 0

   Output:
   PM


4. Input:
   hour = 14
   minutes = 30

   Output:
   PM


5. Input:
   hour = 18
   minutes = 45

   Output:
   PM


6. Input:
   hour = 23
   minutes = 59

   Output:
   PM


7. Input:
   hour = 0
   minutes = 0

   Output:
   AM


Key Concepts:

`<` → Less than

`if` → Checks the condition.

`else` → Executes when the condition is False.

24-hour format:

0–11  → AM
12–23 → PM


Important:

The `minutes` value does not affect whether the time is AM or PM.
Only the `hour` determines the result.

For this question, we assume the given hour is a valid 24-hour
value from 0 to 23.
"""