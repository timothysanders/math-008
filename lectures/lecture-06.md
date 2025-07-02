## Lecture 6: Trigonometric functions
- For radians, our initial exploration has been rotating in the counter-clockwise direction. This is known as the "positive direction"
    - This is $\theta$
    - We can do the same thing, but go in the clockwise direction. This is the "negative direction" and radians are shown as negatives for these cases
        - Example: $\theta = -\frac{3\pi}{4}$
        - Everything else is the same, it just goes in the opposite direction (clockwise)
- Trig Functions
    - Sine
        - $\sin(\theta)$
        - $\frac{\text{opp}}{\text{hyp}}$: opposite over hypotenuse
        - Unit circle: $\frac{y}{1} = y$
    - Cosine
        - $\cos(\theta)$
        - $\frac{\text{adj}}{\text{hyp}}$: adjacent over hypotenuse
        - Unit circle: $\frac{x}{1} = x$
    - Tangent
        - $\tan(\theta)$
        - $\frac{\text{opp}}{\text{adj}}$: opposite over adjacent
        - Unit circle: $\frac{y}{x}$
    - Cosecant
        - Reciprocal of sine
        - $\csc(\theta)$
        - $\frac{\text{hyp}}{\text{opp}}$: hypotenuse over opposite
        - Unit circle: $\frac{1}{y}$
    - Secant
        - Reciprocal of cosine
        - $\sec(\theta)$
        - $\frac{\text{hyp}}{\text{adj}}$: hypotenuse over adjacent
        - Unit circle: $\frac{1}{x}$
    - Cotangent
        - Reciprocal of tangent
        - $\cot(\theta)$
        - $\frac{\text{adj}}{\text{opp}}$: adjacent over opposite
        - Unit circle: $\frac{x}{y}$
    - The opposite side is the side that is "subtended" (contained in) by $\theta$
    - The adjacent side is "next to" $\theta$
    - Hypotenuse is always the same, this the longest side of any right triangle
```python
import numpy as np
import matplotlib.pyplot as plt

# Set the angle (in radians)
theta = np.pi / 4  # 45 degrees
# Compute coordinates on the unit circle
x = np.cos(theta)
y = np.sin(theta)

fig, ax = plt.subplots(figsize=(6, 6))

# Draw the unit circle
circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
ax.add_artist(circle)

# Draw the triangle (from origin to (x, 0) to (x, y))
ax.plot([0, x], [0, y], color='green', linewidth=2)  # hypotenuse
ax.plot([x, x], [0, y], color='red', linewidth=2)    # opposite
ax.plot([0, x], [0, 0], color='blue', linewidth=2)   # adjacent

# Draw axes
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Plot the point (x, y)
ax.plot(x, y, 'ro')
ax.text(x + 0.05, y, f"({x:.2f}, {y:.2f})", color='red', fontsize=12)

# Add labels
ax.text(x / 2, -0.08, 'x', color='blue', fontsize=14, ha='center')
ax.text(x + 0.08, y / 2, 'y', color='red', fontsize=14, va='center')
ax.text(x / 2, y / 2, 'hyp', color='green', fontsize=14, va='center', ha='center')
ax.text(0.1, 0.1, r'$\theta$', color='green', fontsize=18)

# Mark the angle theta
angle = np.linspace(0, theta, 100)
ax.plot(0.18 * np.cos(angle), 0.18 * np.sin(angle), color='green', linewidth=2)

# Set equal aspect ratio
ax.set_aspect('equal')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.axis('off')  # Turn off the grid/axes

plt.show()
```
- Trig functions have a relationship when looking at right triangles and circles
    - "Terminal points" are the $(x, y)$ points on the circle diameter that corresponds to a particular radian length measurement
- The trig functions take a right triangle, and use the opposite side of the triangle and divides it by the hypotenuse
- Tip: To remember trig functions, use the mnemonic **S**OH-**C**AH-**T**OA
    - SOA: Sine Opposite over Adjacent
    - CAH: Cosine Adjacent over Hypotenuse
    - TOA: Tangent Opposite over Adjacent
- Note:
    - In algebra, we often used $x$ to represent our independent variable, and $f(x)$ represented our $y$ value, or dependent variable
    - In trig, our independent variable is $\theta$, and our dependent variable can be $x$ or $y$
        - We can write our dependent variable is $f(\theta)$
        - $\theta$ is our argument for our trig function
    - Our independent variable is created by our radians, the dependent variable is created by the terminal points
    - Theta ($\theta$) (independent variable) can only be a radian or a degree
    - The dependent variable is a terminal point, or some portion of the terminal point
    - $\sin \theta$ and $\sin(\theta)$ are the same thing, these do not indicate multiplication
- Examples
    - Evaluate the following radians
    1. $\sin(\frac{\pi}{2})$
        - Terminal point: $(0, 1)$
        - $\sin(\frac{\pi}{2}) = \frac{y}{1} = \frac{1}{1} = 1$
    2. $\cos(\frac{7\pi}{6})$
        - Terminal point: $(-\frac{\sqrt{3}}{2}, -\frac{1}{2})$
        - $\cos(\frac{7\pi}{6} = \frac{x}{1} = -\frac{\frac{\sqrt{3}}{2}}{1} = -\frac{\sqrt{3}}{2}$
    3. $\tan(\frac{7\pi}{4})$
        - Terminal point: $(\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2})$
        - $\tan(\frac{7\pi}{4}) = \frac{y}{x} = \frac{-\frac{\sqrt{2}}{2}}{\frac{\sqrt{2}}{2}} = -1$
    4. $\sec(-\frac{25\pi}{6})$ (this is equivalent to $\sec(-\frac{\pi}{6}$)
        - Terminal point: $(\frac{\sqrt{3}}{2}, -\frac{1}{2})$
        - $\sec(-\frac{25\pi}{6}) = \frac{1}{x} = \frac{1}{\frac{\sqrt{3}}{2}} = \frac{2}{\sqrt{3}} = \frac{2\sqrt{3}}{3}$
