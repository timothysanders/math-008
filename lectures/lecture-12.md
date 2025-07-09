## Lecture 12: Intro to Inverses
- One-to-one function: a function that has an inverse
- To tell if a function is one-to-one, we use the horizontal line test
  - If a horizontal line intersects the graph of a function more than one time, then it is not a one-to-one function
- For a function to have an inverse, it needs to be symmetric with another function over the $y=x$ line
- The graphs of all trig functions are intersected by a horizontal an infinite amount of times, so these are not one-to-one functions
  - This means that to make an inverse of these functions, we need to restrict the domain of the function
  - This allows our trig function to pass the horizontal line test
- Steps for finding inverse
  1. $f(x) = y$
  2. swap $y \leftrightarrow x$
- Notation for inverse trig functions
  - $\sin^{-1}x$
  - $\arcsin(x)$
  - These both represent the inverse of the sine function
- Ex: Find the inverse
  - $\sin(x)$
    - Restricted domain: $[-\frac{\pi}{2}, \frac{\pi}{2}]$ (this restricted domain actually becomes the range of the inverse)
    - Range: $[-1, 1]$ (this range becomes the domain of the inverse)
    - Inverse
      - Domain: $[-1, 1]$
      - Range: $[-\frac{\pi}{2}, \frac{\pi}{2}]$
      - Notation: $\sin^{-1}x$ or $\arcsin(x)$
  - $\cos(x)$
    - Restricted domain: $[0, \pi]$ (this restricted domain becomes the range of the inverse)
    - Range: $[-1, 1]$ (this range becomes the domain)
    - Inverse
      - Domain: $[-1, 1]$
      - Range: $[0, \pi]$
      - Notation: $\cos^{-1}(x)$ or $\arccos(x)$
  - $\tan(x)$
    - Restricted domain: $(-\frac{\pi}{2},\frac{\pi}{2})$
      - Note that the domain has parentheses, this is because these are asymptotes and cannot be inclusive
    - Range: $(-\infty, \infty)$
    - Inverse
      - Domain: $(-\infty, \infty)$
      - Range: $(-\frac{\pi}{2},\frac{\pi}{2})$
      - Notation: $\tan^{-1}(x)$ or $\arctan(x)$
- The argument of the original trig functions was a degree/radian and you got out a terminal point
- For the inverses, our argument is a terminal point, and we get out some degree/radian
  - **BUT** if you input a terminal point, you have to be mindful of which radian you are looking at (remember the restricted range/domain)

| Function  | Inverse Function                             | Domain of Inverse                | Range of Inverse                               |
|-----------|----------------------------------------------|----------------------------------|------------------------------------------------|
| $\sin(x)$ | $\arcsin(x)$ or $\sin^{-1}(x)$               | $[-1, 1]$                        | $[-\frac{\pi}{2}, \frac{\pi}{2}]$              |
| $\cos(x)$ | $\arccos(x)$ or $\cos^{-1}(x)$               | $[-1, 1]$                        | $[0, \pi]$                                     |
| $\tan(x)$ | $\arctan(x)$ or $\tan^{-1}(x)$               | $(-\infty, \infty)$              | $(-\frac{\pi}{2}, \frac{\pi}{2})$              |
| $\csc(x)$ | $\operatorname{arccsc}(x)$ or $\csc^{-1}(x)$ | $(-\infty, -1] \cup [1, \infty)$ | $[-\frac{\pi}{2}, 0) \cup (0, \frac{\pi}{2}]$  |
| $\sec(x)$ | $\operatorname{arcsec}(x)$ or $\sec^{-1}(x)$ | $(-\infty, -1] \cup [1, \infty)$ | $[0, \frac{\pi}{2}) \cup (\frac{\pi}{2}, \pi]$ |
| $\cot(x)$ | $\operatorname{arccot}(x)$ or $\cot^{-1}(x)$ | $(-\infty, \infty)$              | $(0, \pi)$                                     |