## Lecture 33: The Cross Product
- The cross product of two vectors finds a vector perpendicular to each one (or the two vectors that we are applying the cross product to)
- Given $\vec{a} = a_1i + a_2j + a_3k$ and $\vec{b} = b_1i + b_2j + b_3k$, then $\vec{c} = \vec{a} \times \vec{b}$ gives
  - $$$
  \begin{vmatrix}
  \text{+} & \text{-} & \text{+} \\
  i & j & k \\
  a_1 & a_2 & a_3 \\
  b_1 & b_2 & b_3
  \end{vmatrix}
  $$$
  - $i(a_2b_3 - b_2a_3) - j(a_1b_3 - b_1a_3) + k(a_1b_2 - b_1a_2)$
  - The first row in the grid is your $\lt i, j, k \gt$ vector
  - The second row is the first vector
  - The third row is the second vector
  - The plus or minus pattern in the formula is based on the signs above $i j k$
  - To derive the formula, you "eliminate" the first column/first row, then multiply the determinant values together, then multiplied by $i$
    - Multiply the "backslash" ($a_2 \cdot b_3$) and subtract the "forward slash" ($b_2 \cdot a_3$)
      - This becomes $i(a_2b_3 - b_2a_3)$
  - Next, "eliminate" the second column/first row, then multiply the determinant values together, then multiplied by $j$
    - Multiply the "backslash" ($a_1 \cdot b_3$) and subtract the "forward slash" ($b_1 \cdot a_3$)
      - This becomes $j(a_1b_3 - b_1a_3)$
  - Finally, "eliminate" the third column/first row, then multiply the determinant values together, then multiplied by $k$
    - Multiply the "backslash" ($a_1 \cdot b_2$) and subtract the "forward slash" ($b_1 \cdot a_2$)
      - This becomes $k(a_1b_2 - b_1a_2)$
  - This gives us $i(a_2b_3 - b_2a_3) - j(a_1b_3 - b_1a_3) + k(a_1b_2 - b_1a_2)$, which is perpendicular to $\vec{a}$ and $\vec{b}$
#### Examples
1. Find the cross-product
   - $\vec{u} = 2i - 3j + k$ and $\vec{v} = 4i - j + 5k$; Find $\vec{u} \times \vec{v}$
   - $i((-3)(5) - (-1)(1)) - j((2)(5) - (4)(1)) + k((2)(-1) - (4)(-3))$
   - $-14i - 6j + 10k$
   $$$
   \begin{vmatrix}
   \text{+} & \text{-} & \text{+} \\
   i & j & k \\
   2 & -3 & 1 \\
   4 & -1 & 5 \\
   \end{vmatrix}
   $$$
2. Find the cross-product, $\vec{a} \times \vec{b}$
   - $\vec{a} = \lt 2, -3, 1 \gt$ and $\vec{b} = \lt -2, 1, 1 \gt$
   $$$
   \begin{vmatrix}
   \text{+} & \text{-} & \text{+} \\
   i & j & k \\
   2 & -3 & 1 \\
   -2 & 1 & 1 \\
   \end{vmatrix}
   $$$
   - $i((-3)(1) - (1)(1)) - j((2)(1) - (-2)(1)) + k((2)(1) - (-2)(-3))$
   - $-4i - 4j - 4k\text{ or }\lt -4, -4, -4 \gt$