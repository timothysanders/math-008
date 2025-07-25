## Lecture 23: More on Double Angles
#### Examples
- These problems will be tailored to continued practice for double angle identities
- These will resemble problems we did for inverses, where we are given the terminal point, not the radian
1. Find the exact value of $\sin{2\theta}, \cos{2\theta},\text{ and }\tan{2\theta}\text{ given }\sin\theta = \frac{3}{5}, \frac{\pi}{2} \leq \theta \lt \pi$
   - Because we know we need to be between $\frac{\pi}{2}$ and $\pi$, we know we need to be in quadrant II
   - We can create a right triangle, sine is equal to opposite (3) over hypotenuse (5)
   - Use the pythagorean theorem to find the x-coordinate, $x^2 + 3^2 = 5^2$
     - $x = \pm \sqrt{16} \to x = \pm 4$
     - Because we are in quadrant II, we use the negative
     - $x = -4$
   - $\sin{2\theta} = 2\sin\theta\cos\theta$
   - $ = 2(\frac{3}{5})\cos\theta$
     - Use the triangle that was created to find the value of $\cos\theta$ (adjacent over hypotenuse)
   - $ = 2(\frac{3}{5})(-\frac{4}{5})$
   - $\sin{2\theta} = -\frac{24}{25}$
   - $\cos{2\theta}$
     - You want to think if there are ways you can avoid having to recalculate all of your values from scratch
     - Fortunately, an identity of $\cos{2\theta} = 1 - 2\sin^2\theta$ exists and we have sine already
   - $1 - 2\sin^2\theta = 1 - 2\sin(\theta)^2$
   - $ = 1 - 2(\frac{3}{5})^2$
   - $ = 1 - 2(\frac{9}{25})$
   - $ = 1 - \frac{18}{25}$
   - $\cos{2\theta} = \frac{7}{25}$
   - $\tan{2\theta} = \frac{2\tan\theta}{1 - \tan^2\theta}$
     - Tangent is opposite over adjacent, so $-\frac{3}{4}$
   - $ = \frac{2 \cdot -\frac{3}{4}}{1 - (-\frac{3}{4})^2}$
   - $ = \frac{-\frac{6}{4}}{1 - (\frac{9}{16})}$
   - $ = \frac{-\frac{6}{4}}{\frac{7}{16}}$
   - $ = -\frac{6}{4} \cdot \frac{16}{7} = -\frac{96}{28} = -\frac{24}{7}$
2. Find the exact value of $\sin 2\theta, \cos 2\theta, and \tan 2\theta$ given $\tan \theta = -\frac{12}{5}, \frac{3\pi}{2} \leq \theta < 2\pi$
   - Because we are in quadrant IV ($\frac{3\pi}{2} \leq \theta \lt 2\pi$), we know that our x-coordinate/adjacent side (5) will be positive, but our y-coordinate/opposite side (-12) will be negative
   - Use the pythagorean theorem to find the hypotenuse
   - $5^2 + (-12)^2 = h^2$
   - $h^2 = 169$
   - $h = 13$
   - $\sin 2\theta = 2\sin\theta\cos\theta$
   - $ = 2(-\frac{12}{13})(\frac{5}{13}) = \frac{96}{169}$
   - $\cos 2\theta = 2\cos^2\theta - 1$
   - $ = 2(\frac{5}{13})^2 - 1$
   - $ = -\frac{119}{169}$
   - $\tan 2\theta = \frac{2\tan\theta}{1 - \tan^2\theta}$
   - $ = \frac{2(-\frac{12}{5})}{1 - (-\frac{12}{5})^2}$
   - $ = \frac{-\frac{24}{5}}{-\frac{119}{25}}$
   - $ = -\frac{24}{5} \cdot -\frac{25}{119} = \frac{600}{595} = \frac{120}{119}$

#### Codex notes
- **Square-root property**: When solving $x^2=a$, include both roots: $x=\pm\sqrt{a}$.
- **Equivalent forms of $\cos2\theta$**: $\cos2\theta=\cos^2\theta-\sin^2\theta=1-2\sin^2\theta=2\cos^2\theta-1$; choose the form involving only one trig function to simplify.
- **Exponent rule on fractions**: $(\frac{a}{b})^2=\frac{a^2}{b^2}$ (e.g., $(\frac{3}{5})^2=\frac{9}{25}$).
- **Viewing numeric coefficients as fractions**: Write coefficients as $\frac{n}{1}$ to combine with other fractions seamlessly (e.g., $2=\frac{2}{1}$).
- **Next topic**: The lecture will continue with half-angle identities.