## Lecture 32: Three Dimensional Vectors
- Compared to two dimensional vectors, our notation will change slightly
- Notation: $\lt a_1, a_2, a_3 \gt$
- $(x, y, z)$ where $z$ is the new component
- $a_1i + a_2j + a_3k$
- Other operations for vectors are largely the same
- Vectors are made up of three portions
  - We first go in the x direction
  - Then the y direction
  - Then the z direction
- "The initial point of k goes on the terminal point of j, the initial point of j goes on the terminal point of i"
  - Then you go from the first initial to the last terminal to create your vector
### Component form of a vector
- Represented in a space with initial point $P(x_1, y_1, z_1)$ and terminal point $Q(x_2, y_2, z_2)$ then $\vec{v} = \lt x_2 - x_1, y_2 - y_1, z_2 - z_1 \gt$
### Algebraic Operations
- If $\vec{u} = \lt a_1, a_2, a_3 \gt$ and $\vec{v} = \lt b_1, b_2, b_3 \gt$
  - $\vec{u} + \vec{v} = \lt a_1 + b_1, a_2 + b_2, a_3 + b_3 \gt$
  - $\vec{u} - \vec{v} = \lt a_1 - b_1, a_2 - b_2, a_3 - b_3 \gt$
  - $c\vec{u} = \lt ca_1, ca_2, ca_3 \gt$
### Magnitude
- Given $\vec{v} = \lt a_1, a_2, a_3 \gt$
- $|\vec{v}| = \sqrt{{a_1}^2 + {a_2}^2 + {a_3}^2}$
### Dot Product
- If $\vec{u} = \lt a_1, a_2, a_3 \gt$ and $\vec{v} = \lt b_1, b_2, b_3 \gt$, then the dot product is denoted by $\vec{u}\cdot\vec{v} = a_1 \cdot b_1 + a_2 \cdot b_2 + a_3 \cdot b_3$
- Remember that the dot product of two vectors is just a scalar
### Angles Between Vectors
- If $\theta$ is the angel between two non-zero vectors $\vec{u}$ and $\vec{v}$
  - $\vec{u}\cdot\vec{v} = |\vec{u}||\vec{v}|\cos\theta$
  - $\cos\theta = \frac{\vec{u}\cdot\vec{v}}{|\vec{u}||\vec{v}|}$
  - $\theta = \cos^{-1}(\frac{\vec{u}\cdot\vec{v}}{|\vec{u}||\vec{v}|})$
- Two vectors are orthogonal if they are perpendicular to each other
- Two vectors are perpendicular to each other if their dot product is 0
#### Examples
1. Find the components of the vector
   - Given $P(1, -4, 5)$ and $Q(3, 1, -1)$
   - $\vec{v} = (3 - 1), (1 - (-4)), (-1 - 5) = \lt 2, 5, -6 \gt$
2. Given $\vec{u} = \lt 1, -2, 4 \gt$ and $\vec{v} = 6, -1, 1 \gt$
   - Find $2\vec{u} - \vec{v}$
   - $2\vec{u} = \lt 2, -4, 8 \gt$
   - $2\vec{u} - \vec{v} = (2 - 6), (-4 - (-1)), (8 - 1) = \lt -4, -3, 7 \gt$
3. Find $|\vec{v}|$ where $\vec{v} = \lt 3, 2, 5 \gt$ (could write as $3i + 2j + 5k$)
   - $|\vec{v}| = \sqrt{3^2 + 2^2 + 5^2} = \sqrt{38}$
4. Find the dot product
   - $(2i - 3j - k) \cdot (-i + 2j + 3k)$
   - $(2)(-1) + (-3)(2) + (-1)(3) = -11$
5. Find the angle between $\vec{u} = 2i + 2j - k$ and $\vec{v} = 5i - 4j + 2k$
   - Start with dot product: $\vec{u}\cdot\vec{v} = (2)(5) + (2)(-4) + (-1)(2) = 0$
   - $|\vec{u}| = \sqrt{2^2 + 2^2 + (-1)^2} = \sqrt{9} = 3$
   - $|\vec{v}| = \sqrt{5^2 + (-4)^2 + 2^2} = \sqrt{45}$
   - $\theta = \cos^{-1}(\frac{0}{3\sqrt{45}})$
   - $\theta = \cos^{-1}(0) = 90$
   - These vectors are perpendicular to each other, or you can call them orthogonal