## Lecture 29: Vectors
- A vector is a line segment with direction and magnitude/length
- To conceptualize a vector, think about a force in real life that are acting on objects
  - These forces can be represented as a vector
  - The length of the line segment can be thought of as the "strength"
  - Pushing and pulling have different directions, they could have similar/the same magnitudes, but the direction in which they go matters
- Note that the position of the vector does not matter, it does not impact the direction and magnitude
- Notation: $\vec{v}$, $\lt a, b\gt$
- To represent a stronger force, we draw a longer line
- `Representation vector`: A vector that has an initial point on the origin
  - Having a vector that originates at origin helps visualize the components
### Components of a vector
- Initial point $P(x_1, y_!)$
- Terminal point $Q(x_2, y_2)$
- This vector can be represented as $\vec{v} = \lt x_2 - x_1, y_2 - y_1\gt$
- How do the initial and terminal points correspond to the vector?
  - The component of the vector is "similar" to the slope of a line
  - You can think of the component x-value as the right/left direction the vector goes, and the y-value as the up/down direction the vector goes
### Magnitude (length) of a vector
- Our representation vector looks like a right triangle, our magnitude is the hypotenuse of the triangle
  - $a^2 + b^2 = h^2$
- The magnitude is always going to have a positive value
- The magnitude or length of a vector $\vec{v} \lt a_1, a_2 \gt$ is $|\vec{v}| = \sqrt{{a_1}^2 + {a_2}^2}$
- Vectors can have the same magnitude, even if they have a different direction
### Algebraic Operations on Vectors
- If $\vec{u} = \lt a_1, a_2 \gt$ and $\vec{v} = \lt b_1, b_2 \gt$, then
  - Addition: $\vec{u} + \vec{v} = \lt a_1 + b_1, a_2 + b_2 \gt$
  - Subtraction: $\vec{u} - \vec{v} = \lt a_1 - b_1, a_2 - b_2 \gt$
  - Scalar Multiplication: $c\vec{u} = \lt ca_1, ca_2 \gt$ ($c$ is the scalar)
### Graphing Vectors
- Geometrically to add vectors $\vec{u}, \vec{v}$ together, you have to take the initial point (IP) of $\vec{v}$ and put it on the terminal point (TP) of $\vec{u}$
- The sum is the vector from IP $\vec{u}$ and TP $\vec{v}$, this creates the vector $\vec{u} + \vec{v}$ that forms a triangle
- The scalar multiplication of a vector doubles the length of a vector
  - When the scalar is positive, the vector grows in the original direction
  - When the scalar is negative, the vector grows in the opposite direction
#### Examples
1. Find the component of the vector
   - IP: $P(-2, 5)$ and TP $Q(3, 7)$
     - $\vec{v} = \lt 3 - (-2), 7 - 5 \gt = \lt 5, 2 \gt$
2. Find the component of the vector
   - IP: $P(4, 1)$ and TP $Q(2, 3)$
     - $\vec{v} = \lt 2 - 4, 3 - 1 \gt = \lt -2, 2 \gt$
3. Find $| \cdot |$
   - $\vec{v} = \lt 2, -3 \gt$
     - $|\vec{v}| = \sqrt{2^2 + (-3)^2} = \sqrt{13}$
   - $\vec{v} = \lt 5, 0 \gt$
     - $|\vec{v}| = \sqrt{5^2 + 0^2} = \sqrt{25} = 5$
   - $\vec{v} = \lt 4, 3 \gt$
     - $|\vec{v}| = \sqrt{4^2 + 3^2} = \sqrt{25} = 5$
4. Apply operations on given $\vec{u} = \lt 2, -3 \gt, \vec{v} = \lt -1, 2 \gt$
   - $\vec{u} + \vec{v}$
     - $\lt 2 + (-1), -3 + 2 \gt = \lt 1, -1 \gt$
   - $\vec{u} - \vec{v}$
     - $\lt 2 - (-1), -3 - 2 \gt = \lt 3, -5 \gt$
   - $2\vec{u} - 3\vec{v}$
     - $2\vec{u} = \lt 2(2), 2(-3) \gt = \lt 4, -6 \gt$
     - $3\vec{v} = \lt 3(-1), 3(2) \gt = \lt -3, 6 \gt$
     - $\lt 4 - (-3), -6 - 6 \gt = \lt 7, -12 \gt$