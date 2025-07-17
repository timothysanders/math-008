## Lecture 24: Half Angles
- Each step of these identities have been building on each other
  - Sum identity formulas
  - Double angle identity formulas built from sum identities
  - Half angle identity formulas built from double angle identities
- In the double angle formulas, we are replacing $\theta$ with $\frac{\alpha}{2}$
  - For example, $2\cos^2\theta - 1$ becomes $2\cos^2\frac{\alpha}{2} - 1$
### Converting Degrees and Radians
- To convert degrees to radians, take the degrees and multiply it by $\frac{\pi}{180^\circ}$
- To convert radians to degrees, take the radian and multiply it by $\frac{180^\circ}{\pi}$
### Half angle identity formulas
- $\cos(\frac{\alpha}{2}) = \pm \sqrt{\frac{1 + \cos\alpha}{2}}$
- $\sin(\frac{\alpha}{2}) = \pm \sqrt{\frac{1 - \cos\alpha}{2}}$
- $\tan(\frac{\alpha}{2}) = \pm \sqrt{\frac{1 - \cos\alpha}{1 + \cos\alpha}}$
#### Examples
1. Find the exact value (without using a calculator)
   - $\cos(15^\circ)$ (can be written as $\frac{\pi}{12}$)
   - When we are doing our manipulation, we are not changing the value, we may manipulate it to look different, but we don't change its value
   - We can determine whether we take the positive or negative value of the square root by looking at which quadrant the radian or degree is in
   - $\cos(\frac{30^\circ}{2})$ or $\cos(\frac{\frac{\pi}{6}}{2})$
   - $\cos(\frac{30^\circ}{2}) = \sqrt{\frac{1 + \cos30}{2}}$
   - $\cos(\frac{30^\circ}{2}) = \sqrt{\frac{1 + \frac{\sqrt{3}}{2}}{2}}$
   - $ = \sqrt{\frac{\frac{2+\sqrt{3}}{2}}{2}} = \sqrt{\frac{2+\sqrt{3}}{2} \cdot \frac{1}{2}}$
   - $ = \sqrt{\frac{2 + \sqrt{3}}{4}} = \frac{\sqrt{2 + \sqrt{3}}}{\sqrt{4}} = \frac{\sqrt{2 + \sqrt{3}}}{2}$
2. $\sin(22.5^\circ) = \sin(\frac{45}{2})$
   - $ = \sqrt{\frac{1 - \cos(45^\circ)}{2}} = \sqrt{\frac{1 - \frac{\sqrt{3}}{2}}{2}}$
   - $ = \sqrt{\frac{2 - \sqrt{2}}{2} \cdot \frac{1}{2}}$
   - $ = \sqrt{\frac{2 - \sqrt{2}}{4}}$
   - $ = \sqrt{\frac{2 - \sqrt{2}}{2}}$

#### Codex notes
- **Multiple tangent half-angle formulas**: Several equivalent forms exist (e.g., $\displaystyle\sqrt{\frac{1-\cos\alpha}{1+\cos\alpha}}$ or $\displaystyle\frac{1-\cos\alpha}{\sin\alpha}$); use whichever matches your source.
- **Maintain original angle value**: Rewrite the half-angle argument to match the formula structure without altering its actual value (e.g., use a “form of 1” to adjust numerator/denominator rather than dividing by 2 directly).
- **Divide by a fraction by multiplying by its reciprocal**: When dividing by a number or fraction (e.g., by 2), multiply the denominator by the reciprocal to preserve equivalence.
- **Create common denominators**: Multiply numerator and denominator by the same factor to combine fractions before simplifying.
- **Split radicals in a fraction**: Use $\displaystyle\sqrt{\frac{a}{b}}=\frac{\sqrt a}{\sqrt b}$ to simplify nested radicals.
- **Determine sign via quadrants**: Use the original angle’s quadrant (not the halved argument) to choose the correct $\pm$ sign in half-angle formulas.
- **Recall special angle values**: $\cos30^\circ=\frac{\sqrt3}{2}$ and $\sin45^\circ=\frac{\sqrt2}{2}$.
- **Radian half-angle trick**: For radian inputs, multiply numerator and denominator by 2 (a “form of 1”) to match the half-angle argument without changing its value.
- **Example focus**: Apply half-angle identities to find exact values without a calculator, rather than verifying identities.
- **Next topic**: Polar coordinates and polar equations.