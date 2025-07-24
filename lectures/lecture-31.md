## Lecture 31: Dot Product
- The dot product multiplication is distinct from scalar multiplication
- Scalar multiplication enlarges, shrinks, changes direction, etc., but dot product is different
- The dot product is finding the angle that is created by the two vectors that are in question
- If we have $\vec{u} = \lt a_1, a_2 \gt$ and $\vec{v} = \lt b_1, b_2 \gt$, the dot product denoted by $\vec{u} \cdot \vec{v}$ is defined by $\vec{u} \cdot \vec{v} = a_1 \cdot b_1 + a_2 \cdot b_2$
  - This version of the dot product gives us a number that we will use to find our angle
- "Non-zero vector" means that a vector has some length/magnitude to it
- If $\theta$ is the angle between two non-zero vectors $\vec{u}$ and $\vec{v}$, then the dot product ($\vec{u} \cdot \vec{v}$) is given by $|\vec{u}||\vec{v}|\cos\theta$
- To get $\theta$ out of the argument, we need to use inverses
- Divide both sides by the magnitude of the two vectors
- $\cos\theta = \frac{\vec{u}\cdot\vec{v}}{|\vec{u}||\vec{v}|}$
- $\theta = \cos^{-1}(\frac{\vec{u}\cdot\vec{v}}{|\vec{u}||\vec{v}|})$
#### Examples
1. Find $\vec{u} \cdot \vec{v}$
   - $\vec{u} = \lt 3, -2 \gt, \vec{v} = \lt 4, 5 \gt$
     - $\vec{u} \cdot \vec{v} = (3)(4) + (-2)(5) = 12 + (-10) = 2$
   - $\vec{a} = 2i + j, \vec{b} = 5i - 6j$
     - $\vec{a} \cdot \vec{b} = (2)(5) + (1)(-6) = 10 + (-6) = 4$
2. Find the angle between the vectors
   - $\vec{u} = 3i - 2j$ and $\vec{v} = 4i + 5j$
     - Find theta: $\theta = \cos^{-1}(\frac{\vec{u}\cdot\vec{v}}{|\vec{u}||\vec{v}|})$
     - $\vec{u} \cdot \vec{v} = (3)(4) + (-2)(5) = 12 + (-10) = 2$
     - $|\vec{u}| = \sqrt{3^2 + (-2)^2} = \sqrt{13}$
     - $|\vec{v}| = \sqrt{4^2 + 5^2} = \sqrt{41}$
     - $\theta = \cos^{-1}(\frac{2}{\sqrt{13}\cdot\sqrt{41}})$
     - $\theta \approx 85^\circ$
   - $\vec{u} = \lt 3, 0 \gt$ and $\vec{v} = \lt 0, 2 \gt$
     - $\vec{u} \cdot \vec{v} = (3)(0) + (0)(2) = 0$
     - $|\vec{u}| = \sqrt{3^2 + 0^2} = 3$
     - $|\vec{v}| = \sqrt{0^2 + 2^2} = 2$
     - $\theta = \cos^{-1}(\frac{0}{6}) = \cos^{-1}(0)$
     - $\theta = 90^\circ$
     - These vectors are perpendicular to each other
     - This can also be described as these two vectors being "orthogonal"