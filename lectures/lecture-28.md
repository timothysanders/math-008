## Lecture 28: Parametric Equations
- Up until this point, we have been dealing with trigonometry, but here we are getting into a more "algebra-based" section
- Parametric equations: equations that help describe the movement/direction along a curve
  - These curves will resemble a lot of algebraic curves (parabolas, ellipses, etc.)
- Equation form
  - $x = f(t)$; $y = g(t)$
  - Parameter "$t$"
- x and y coordinates come from the functions f() and g()
#### Examples
1. $x = 3t^2, y = 2t; -2 \leq t \leq 2$
   - We want to go from smallest to largest, so choose -2, -1, 0, 1, 2
   - When we graph, we need to make sure that we graph them in the order of the ordered pairs
   - The "direction" of the order is the movement

   | t  | x               | y    |
   |----|-----------------|------|
   | -2 | $3(-2)^2 = 12$  | $-4$ |
   | -1 | $3(-1)^2 = 3$   | $-2$ |
   | 0  | $3(0)^2 = 0$    | $0$  |
   | 1  | $3(1)^2 = 3$    | $2$  |
   | 2  | $3(2)^2 = 12$   | $4$  |
   - This ends up being a sideways parabola
   - This happens when you have an equation where the y is squared instead of the x being squared ($x = y^2$)
2. $x = -2t + 2, y = 4t^2 - 2; -2 \leq t \leq 2$
    - Remember to graph the ordered pairs from smallest t-value to highest

   | t  | x                | y                  |
   |----|------------------|--------------------|
   | -2 | $-2(-2) + 2 = 6$ | $4(-2)^2 - 2 = 14$ |
   | -1 | $-2(-1) + 2 = 4$ | $4(-1)^2 - 2 = 2$  |
   | 0  | $-2(0) + 2 = 2$  | $4(0)^2 - 2 = -2$  |
   | 1  | $-2(1) + 2 = 0$  | $4(1)^2 - 2 = 2$   |
   | 2  | $-2(2) + 2 = -2$ | $4(2)^2 - 2 = 14$  |
   - This is a parabola opening upwards, which is when $y = x^2$
3. $x = 5\sin t, y = 4\cos t; 0 \leq t \lt 2\pi$

   | t                | x                            | y                           |
   |------------------|------------------------------|-----------------------------|
   | 0                | $5\sin(0) = 0$               | $4\cos(0) = 4$              |
   | $\frac{\pi}{2}$  | $5\sin(\frac{\pi}{2} = 5$    | $4\cos(\frac{\pi}{2}) = 0$  |
   | $\pi$            | $5\sin\pi = 0$               | $4\cos(\pi) = -4$           |
   | $\frac{3\pi}{2}$ | $5\sin(\frac{3\pi}{2}) = -5$ | $4\cos(\frac{3\pi}{2}) = 0$ |
   - This shape is an ellipse
   - Equation of an ellipse: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$
4. Rewrite in rectangular form
   - Goal is to remove the parameter
   - $x = 3t^2, y = 2t$
   - Use the concept of systems of equations from algebra
   - $y = 2t \to t = \frac{y}{2}$
   - $x = 3(\frac{y}{2})^2 \to x = \frac{3y^2}{4}$
   - We now have our rectangular form of our parametric equation
   - Note the $y^2$ in the equation, this is the sideways parabola
5. $x = 5\sin t, y = 4\cos t$
   - Goal is to eliminate the parameter
   - If we are going to isolate an argument from a trig function, we need to use the inverse
   - Note: remember the pythagorean identity $\sin^2t + \cos^2t = 1 \to (\sin t)^2 + (\cos t)^2 = 1$
   - $\sin t = \frac{x}{5}, \cos t = \frac{y}{4}$
   - $(\frac{x}{5})^2 + (\frac{y}{4})^2 = 1$
   - $\frac{x^2}{5^2} + \frac{y^2}{4^2} = 1$
   - Note that the denominators are the same as the coefficients of the trig functions
