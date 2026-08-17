def main():
    # Question 26: Take coordinates (x, y) and determine which quadrant the point lies in.
    x = -4
    y = 6

    if x > 0 and y > 0:
        print("Quadrant I")
    elif x < 0 and y > 0:
        print("Quadrant II")
    elif x < 0 and y < 0:
        print("Quadrant III")
    elif x > 0 and y < 0:
        print("Quadrant IV")
    else:
        print("Point lies on an axis or origin")


if __name__ == "__main__":
    main()


"""
Explanation:

The question gives us a point using two coordinates:

(x, y)

The value of `x` tells us whether the point is on the left or right
side of the Y-axis.

The value of `y` tells us whether the point is above or below
the X-axis.


Quadrant rules:

Quadrant I:
x > 0 and y > 0

Quadrant II:
x < 0 and y > 0

Quadrant III:
x < 0 and y < 0

Quadrant IV:
x > 0 and y < 0


Example:

x = -4
y = 6

Step 1:
x > 0 and y > 0
-4 > 0 → False

Step 2:
x < 0 and y > 0
-4 < 0 → True
6 > 0 → True

Both conditions are True.

Therefore:
Quadrant II


Another example:

x = 5
y = -3

x > 0 → True
y < 0 → True

Therefore:
Quadrant IV


What happens when x or y is zero?

Example:
x = 0
y = 5

The point is on the Y-axis.

Example:
x = 5
y = 0

The point is on the X-axis.

Example:
x = 0
y = 0

The point is at the origin.

Therefore, the `else` block handles:
- X-axis
- Y-axis
- Origin


Test Cases:

1. Input: x = 4, y = 6
   Output: Quadrant I

2. Input: x = -4, y = 6
   Output: Quadrant II

3. Input: x = -4, y = -6
   Output: Quadrant III

4. Input: x = 4, y = -6
   Output: Quadrant IV

5. Input: x = 0, y = 5
   Output: Point lies on an axis or origin

6. Input: x = 5, y = 0
   Output: Point lies on an axis or origin

7. Input: x = 0, y = 0
   Output: Point lies on an axis or origin


Key Concepts:

`>`  → Greater than
`<`  → Less than
`and` → Both conditions must be True

Important:

Python uses `and`, not `&&`.

The four quadrants are determined by the signs of `x` and `y`:

(+ , +) → Quadrant I
(- , +) → Quadrant II
(- , -) → Quadrant III
(+ , -) → Quadrant IV
"""