## Lecture 20: More Examples for Verifying Identities
- Tips for if you are stuck when verifying a particular identity
  - Constantly trying to manipulate/substitute the trigonometric identities
  - Conjugates: $a-b;a+b$ are conjugates of each other
    - Multiplying by the conjugate can be helpful
  - Multiplying by 1
    - Example: multiplying by $\frac{\cos\theta}{\cos\theta}$
  - Adding and subtracting fractions ($\pm$)
    - You must have the same denominator when adding/subtracting
    - $\frac{1}{\sin\theta} + \frac{1}{\tan\theta}$
    - $\frac{1}{\sin\theta}\cdot \frac{\tan\theta}{\tan\theta} + \frac{1}{\tan\theta} \cdot \frac{\sin\theta}{\sin\theta}$
    - $\frac{\tan\theta + \sin\theta}{\sin\theta\tan\theta}$
  - Dividing fractions
    - When dividing fractions, you have to multiply by the reciprocal of the denominator
  - Look at both sides

#### Examples
1. $\frac{\cot\theta}{\csc\theta} = \cos\theta$
   - We have more to work with on the left-hand side, so we can start there
   - Think about identities that use $\cos$ and $\sin$
   - $\frac{\cot\theta}{\csc\theta} \to \frac{\frac{\cos\theta}{\sin\theta}}{\frac{1}{\sin\theta}}$
   - $\frac{\cos\theta}{\sin\theta} \cdot \frac{\sin\theta}{1} \to \cos\theta$
2. $\frac{1 + \tan{u}}{1 + \cot{u}} = \tan{u}$
   - Again, we have more to work with on the left hand side
   - $\frac{1 + \tan{u}}{1 + \frac{1}{\tan{u}}}$
   - $\frac{1 + \tan{u}}{\frac{\tan{u}}{\tan{u}} + \frac{1}{\tan{u}}}$
   - $\frac{1 + \tan{u}}{\frac{\tan{u} + 1}{\tan{u}}}$
   - $\frac{1 + \tan{u}}{1} \cdot \frac{\tan{u}}{\tan{u} + 1} \to \tan{u}$
3. $\frac{\sin\theta}{1 + \cos\theta} + \frac{1 + \cos\theta}{\sin\theta} = 2\csc\theta$
   - Because we have fractions, we want to try and get a common denominator
   - $\frac{\sin\theta}{1 + \cos\theta} \cdot \frac{\sin\theta}{\sin\theta} + \frac{1 + \cos\theta}{\sin\theta} \cdot \frac{1 + \cos\theta}{1 + \cos\theta}$
   - $\frac{\sin^2\theta}{(1 + \cos\theta)\sin\theta} + \frac{(1 + \cos\theta)^2}{(1 + \cos\theta)\sin\theta} \to \frac{\sin^2\theta + (1 + \cos\theta)(1 + \cos\theta)}{\sin\theta(1 + \cos\theta)}$
   - In this instance, it makes sense to distribute the $(1 + \cos\theta)$ terms
   - $\frac{\sin^2\theta + 1 + \cos\theta + \cos\theta + \cos^2\theta}{\sin\theta(1 + \cos\theta)}$
     - Looking at this, see that we have $\sin^2\theta$ and $\cos^2\theta$, remember the Pythagorean identity property $\cos^2\theta + \sin^2\theta = 1$
   - $\frac{2 + 2\cos\theta}{\sin\theta(1 + \cos\theta)}$
     - Can factor out the GCF of the numerator
   - $\frac{2(1 + \cos\theta)}{\sin\theta(1 + \cos\theta)} \to \frac{2}{\sin\theta} \to 2 \cdot \frac{1}{\sin\theta} \to 2 \cdot \csc\theta$