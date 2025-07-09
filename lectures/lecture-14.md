## Lecture 14: Inverse Composition
- In some cases with inverse compositions (such as $\sin^{-1}(\sin(\frac{\pi}{3}))$), the functions seem to cancel, while in other instances (such as $\cos^{-1}(\cos(\frac{5\pi}{3}))$), this does not seem to be the case
- When evaluating inverse functions, we always need to take the first step of 

| Expression              | Implies            |
|-------------------------|--------------------|
| $\theta = \sin^{-1}(x)$ | $\sin(\theta) = x$ |
| $\theta = \cos^{-1}(x)$ | $\cos(\theta) = x$ |
| $\theta = \tan^{-1}(x)$ | $\tan(\theta) = x$ |
| $\theta = \arcsin(x)$   | $\sin(\theta) = x$ |
| $\theta = \arccos(x)$   | $\cos(\theta) = x$ |
| $\theta = \arctan(x)$   | $\tan(\theta) = x$ |
| $\theta = \csc^{-1}(x)$ | $\csc(\theta) = x$ |
| $\theta = \sec^{-1}(x)$ | $\sec(\theta) = x$ |
| $\theta = \cot^{-1}(x)$ | $\cot(\theta) = x$ |

#### Cancellation Property for Inverses
- This is also a way to verify if two functions are inverses of each other
  - $f^{-1}(f(x)) = x$
  - $f(f^{-1}(x)) = x$
- Sometimes called the "1:1 property"
- As long as the functions are inverses of each other, they can cancel out

- Recall **SohCahToa**
  - $\sin(\theta) = \frac{\text{opp}}{\text{hyp}}$
    - $\csc(\theta) = \frac{\text{hyp}}{\text{opp}}$
  - $\cos(\theta) = \frac{\text{adj}}{\text{hyp}}$
    - $\sec(\theta) = \frac{\text{hyp}}{\text{adj}}$
  - $\tan(\theta) = \frac{\text{opp}}{\text{adj}}$
    - $\cot(\theta) = \frac{\text{adj}}{\text{opp}}$
  - In the unit circle, the terminal point is our theta that is plugged into each function
    - Remember that the unit circle has a radius of 1, but we may be dealing with points that are not on the unit circle
#### Examples
- Need to be able to find values on the exams without a calculator
1. $\cos(\sin^{-1}(-\frac{1}{2}))$
   - $\sin^{-1}(-\frac{1}{2}) = -\frac{\pi}{6}$ (or $-30^\circ$ in degrees)
     - The y-value in this argument is negative, so using our knowledge that the domain can only be $[\frac{\pi}{2}, -\frac{\pi}{2}]$
     - Remember that the outputs, or dependent variables are radians or degrees
   - $\cos(-\frac{\pi}{6}) = \frac{\sqrt{3}}{2}$
2. $\sin(\tan^{-1}(\frac{1}{2}))$
   - You want to make sure that you double check each input of inverse functions
   - $\tan^{-1}(\frac{1}{2}) = \theta$
     - Since $\tan$ is the opposite over the adjacent, we can use the pythagorean theorem to find the hypotenuse
       - $x^2 + y^2 = r^2$
       - $2^2 + 1^2 = r^2$
       - $\sqrt{5} = r$
   - $\sin(\theta)$
     - Since $\sin$ is the opposite over the hypotenuse, we can take our previous information to find the answer
       - $\frac{1}{\sqrt{5}} = \frac{\sqrt{5}}{5}$ (remember to rationalize the denominator)
3. $\cos(\sin^{-1}(-\frac{1}{3}))$
   - We know that the domain of $\sin^{-1} = [-1, 1]$ so our input here is acceptable
   - $\sin^{-1}(-\frac{1}{3})$
     - Because the terminal point is negative, we must be in quadrant IV
     - Inverse of sine can only be in quadrant I and IV
     - Because sine is opposite over hypotenuse, our opposite is -1 and our hypotenuse is 3
       - The hypotenuse will not be negative, so the y-value (opposite) will have to be negative
     - To find our x-value, we use the pythagorean theorem
       - $3^2 = x^2 + (-1)^2$
       - $9 = x^2 + 1$
       - $x = \sqrt{8}$
       - $x = \pm2\sqrt{2}$
         - Because we are in quadrant IV, the x-value is positive, so $x = 2\sqrt{2}$
   - $\cos(\theta)$ is adjacent over hypotenuse
     - $\cos(\theta) = \frac{2\sqrt{2}}{3}$

- If we do not know the radians for a particular point, we create a triangle and use the trig functions/pythagorean theorem to evaluate the answer
