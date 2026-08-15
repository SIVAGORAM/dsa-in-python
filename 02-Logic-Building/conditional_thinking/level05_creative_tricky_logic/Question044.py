def main():
    # Question 44: Take time (hours and minutes) and print the smaller
    # angle between the hour and minute hands.

    hours = 3
    minutes = 30

    hour_angle = (hours % 12) * 30 + minutes * 0.5
    minute_angle = minutes * 6

    angle = abs(hour_angle - minute_angle)

    if angle > 180:
        angle = 360 - angle

    print("Smaller angle =", angle)


if __name__ == "__main__":
    main()


"""
QUESTION:

Take time (hours and minutes) and print the smaller angle
between the hour and minute hands.


WHAT DOES THE QUESTION MEAN?

An analog clock has two hands:

1. Hour hand
2. Minute hand

We need to calculate the angle between these two hands.

There are always two possible angles between the hands:

Example:

If the angle is 270 degrees, the other angle is:

360 - 270 = 90 degrees

We need the SMALLER angle.

Therefore, the final answer must always be between:

0 and 180 degrees.


--------------------------------------------------
IMPORTANT CLOCK FACTS
--------------------------------------------------

A complete clock circle:

360 degrees


There are 12 hours:

360 / 12 = 30 degrees

Therefore:

Each hour = 30 degrees


There are 60 minutes:

360 / 60 = 6 degrees

Therefore:

Each minute = 6 degrees


--------------------------------------------------
HOUR HAND ANGLE
--------------------------------------------------

The hour hand does NOT stay exactly on the hour.

It moves gradually as the minutes pass.

For every hour:

30 degrees

For every minute:

0.5 degrees


Why?

The hour hand moves 30 degrees in 60 minutes.

Therefore:

30 / 60 = 0.5 degrees per minute.


Formula:

hour_angle = (hours % 12) * 30 + minutes * 0.5


--------------------------------------------------
MINUTE HAND ANGLE
--------------------------------------------------

The minute hand moves:

6 degrees per minute.


Formula:

minute_angle = minutes * 6


--------------------------------------------------
FINAL ANGLE
--------------------------------------------------

First calculate the difference:

angle = abs(hour_angle - minute_angle)


We use `abs()` because we only need the distance between
the two hands, not a negative value.


Then:

if angle > 180:
    angle = 360 - angle


This converts the larger angle into the smaller angle.


--------------------------------------------------
EXAMPLE: 3:30
--------------------------------------------------

Given:

hours = 3
minutes = 30


STEP 1: HOUR HAND

Formula:

(hours % 12) * 30 + minutes * 0.5


Substitute:

(3 % 12) * 30 + 30 * 0.5


3 % 12 = 3

Therefore:

3 * 30 + 30 * 0.5

= 90 + 15

= 105 degrees


Hour hand angle:

105 degrees


--------------------------------------------------
STEP 2: MINUTE HAND
--------------------------------------------------

Formula:

minutes * 6


30 * 6

= 180 degrees


Minute hand angle:

180 degrees


--------------------------------------------------
STEP 3: DIFFERENCE
--------------------------------------------------

angle = abs(hour_angle - minute_angle)


= abs(105 - 180)

= abs(-75)

= 75


Therefore:

angle = 75 degrees


--------------------------------------------------
STEP 4: CHECK FOR ANGLE > 180
--------------------------------------------------

75 > 180 → False

So we don't change the angle.


Final:

Smaller angle = 75.0


--------------------------------------------------
DRY RUN
--------------------------------------------------

Given:

hours = 3
minutes = 30


Hour angle:

(3 % 12) * 30 + 30 * 0.5

= 3 * 30 + 15

= 105


Minute angle:

30 * 6

= 180


Difference:

abs(105 - 180)

= 75


Check:

75 > 180 → False


Output:

Smaller angle = 75.0


--------------------------------------------------
ANOTHER EXAMPLE: 12:00
--------------------------------------------------

hours = 12
minutes = 0


Hour angle:

(12 % 12) * 30 + 0 * 0.5

= 0


Minute angle:

0 * 6

= 0


Difference:

abs(0 - 0)

= 0


Output:

Smaller angle = 0.0


--------------------------------------------------
ANOTHER EXAMPLE: 6:00
--------------------------------------------------

hours = 6
minutes = 0


Hour angle:

(6 % 12) * 30

= 180


Minute angle:

0 * 6

= 0


Difference:

abs(180 - 0)

= 180


Output:

Smaller angle = 180.0


--------------------------------------------------
IMPORTANT EXAMPLE: 9:00
--------------------------------------------------

hours = 9
minutes = 0


Hour angle:

9 * 30 = 270


Minute angle:

0


Difference:

abs(270 - 0)

= 270


But:

270 > 180 → True


So:

angle = 360 - 270

= 90


Final:

Smaller angle = 90.0


This is why this condition is necessary:

if angle > 180:
    angle = 360 - angle


--------------------------------------------------
ANOTHER EXAMPLE: 1:05
--------------------------------------------------

hours = 1
minutes = 5


Hour angle:

(1 % 12) * 30 + 5 * 0.5

= 30 + 2.5

= 32.5


Minute angle:

5 * 6

= 30


Difference:

abs(32.5 - 30)

= 2.5


Output:

Smaller angle = 2.5


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

hours = 3
minutes = 30

Output:

Smaller angle = 75.0


TEST CASE 2:

Input:

hours = 12
minutes = 0

Output:

Smaller angle = 0.0


TEST CASE 3:

Input:

hours = 6
minutes = 0

Output:

Smaller angle = 180.0


TEST CASE 4:

Input:

hours = 9
minutes = 0

Output:

Smaller angle = 90.0


TEST CASE 5:

Input:

hours = 1
minutes = 5

Output:

Smaller angle = 2.5


TEST CASE 6:

Input:

hours = 3
minutes = 0

Output:

Smaller angle = 90.0


TEST CASE 7:

Input:

hours = 12
minutes = 30

Output:

Smaller angle = 165.0


TEST CASE 8:

Input:

hours = 6
minutes = 30

Output:

Smaller angle = 15.0


--------------------------------------------------
TEST CASE TABLE
--------------------------------------------------

| Hours | Minutes | Expected Angle |
|------:|--------:|---------------:|
| 3 | 30 | 75.0° |
| 12 | 0 | 0.0° |
| 6 | 0 | 180.0° |
| 9 | 0 | 90.0° |
| 1 | 5 | 2.5° |
| 3 | 0 | 90.0° |
| 12 | 30 | 165.0° |
| 6 | 30 | 15.0° |


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. Modulo `%`

Used here:

hours % 12

This converts 12-hour clock values.

For example:

12 % 12 = 0
13 % 12 = 1
14 % 12 = 2
15 % 12 = 3


2. Multiplication

`*` is used to calculate the angle.


3. `abs()`

Returns the absolute value.

Example:

abs(-75) → 75


4. Decimal values

The hour hand moves:

0.5 degrees per minute.

Therefore, the answer can be a decimal.

Example:

2.5 degrees


5. `if`

Used to check whether the calculated angle is greater than
180 degrees.


--------------------------------------------------
MAIN FORMULAS TO REMEMBER
--------------------------------------------------

Hour hand:

(hours % 12) * 30 + minutes * 0.5


Minute hand:

minutes * 6


Difference:

abs(hour_angle - minute_angle)


Smaller angle:

if angle > 180:
    angle = 360 - angle


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How did you solve this problem?"

You can say:

"First, I calculate the hour-hand angle using 30 degrees per hour
and 0.5 degrees per minute. Then I calculate the minute-hand angle
using 6 degrees per minute. I take the absolute difference between
the two angles. If the difference is greater than 180 degrees, I
subtract it from 360 to get the smaller angle."


--------------------------------------------------
IMPORTANT
--------------------------------------------------

The hour hand moves continuously.

For example, at 3:30, the hour hand is NOT at exactly 90 degrees.

It has moved another:

30 × 0.5 = 15 degrees

So:

Hour hand = 105 degrees

not:

90 degrees


This is the most important concept in this problem.


--------------------------------------------------
MAIN LOGIC
--------------------------------------------------

Given:

Hours + Minutes
       ↓
Calculate hour-hand angle
       ↓
Calculate minute-hand angle
       ↓
Find absolute difference
       ↓
Is difference > 180?
       ↓
YES → 360 - difference
NO  → Keep difference
       ↓
Smaller angle
"""