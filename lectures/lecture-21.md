## Lecture 21: Sum and Difference Formulas

### Sum and Difference Identities
- Within each family of formulas, the only things that are changing are the signs in each of the formulas
- These formulas can also be used to further manipulate formulas for verifying identities
#### Sine formulas
- $\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$
- $\sin(\alpha - \beta) = \sin\alpha\cos\beta - \cos\alpha\cos\beta$
#### Cosine formulas
- $\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$
- $\cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta$
#### Tangent formulas
- $\tan(\alpha + \beta) = \frac{\tan\alpha + \tan\beta}{1 - \tan\alpha\tan\beta}$
- $\tan(\alpha - \beta) = \frac{\tan\alpha - \tan\beta}{1 + \tan\alpha\tan\beta}$

#### Examples
1. $\cos(\frac{\pi}{12})$ (this could also be expressed as $15^\circ$)
   - Typically we don't write these as degrees, we will usually use radians
   - $\to \cos(\frac{}{12} - \frac{}{12})$ (subtract two fractions with the same denominator)
   - $\to \cos(\frac{4\pi}{12} - \frac{3\pi}{12})$
   - $\to \cos(\frac{\pi}{3} - \frac{\pi}{4})$
   - $\cos(\frac{\pi}{3})\cos(\frac{\pi}{4}) + \sin(\frac{\pi}{3})\sin(\frac{\pi}{4})$
   - $\frac{1}{2} \cdot \frac{\sqrt{2}}{2} + \frac{\sqrt{3}}{2} \cdot \frac{\sqrt{2}}{2}$
   - $\frac{\sqrt{2}}{4} + \frac{\sqrt{6}}{4}$
   - $= \frac{\sqrt{2} + \sqrt{6}}{4}$
2. Verify $\frac{\cos(\alpha - \beta)}{\sin\alpha\sin\beta} = \cot\alpha\cot\beta + 1$
   - $\frac{\cos(\alpha - \beta)}{\sin\alpha\sin\beta} \to \frac{\cos\alpha\cos\beta + \sin\alpha\sin\beta}{\sin\alpha\sin\beta}$
   - $\frac{\cos\alpha\cos\beta}{\sin\alpha\sin\beta} + \frac{\sin\alpha\sin\beta}{\sin\alpha\sin\beta}$
   - $\frac{\cos\alpha\cos\beta}{\sin\alpha\sin\beta} + 1$
   - $\frac{\cos\alpha}{\sin\alpha} \cdot \frac{\cos\beta}{\sin\beta} + 1 = \cot\alpha\cot\beta + 1$
3. If $f(x) = \sin(x)$, show the following
   - $\frac{f(x+h) - f(x)}{h} = \sin x(\frac{\cos h - 1)}{h}) + \cos x(\frac{\sin h}{h})$
   - The first part of the equation is the difference quotient
   - $\frac{f(x+h) - f(x)}{h} = \frac{\sin(x + h) - \sin x}{h}$
     - Remember $f(x) = \sin(x)$
   - $\to \frac{\sin x \cos h + \cos x \sin h - \sin x}{h}$
   - $\to \frac{\sin x \cos h - \sin x}{h}+ \frac{\cos x \sin h}{h}$
   - $\sin x(\frac{\cos h - 1}{h}) + \cos x(\frac{\sin h}{h})$
