## Lecture 22: Double Angle Formulas
- The double angle comes from the sum and difference
- If the degrees or radians that are plugged into your sum formula (see lecture 21), you will get two of one of the angles
- Remember from our pythagorean identities, where we can turn $\cos^2\theta$ into $1 - \sin^2\theta$
  - Version 1: $\cos(2\theta) = \cos^2\theta - \sin^2\theta$
  - Version 2: $\cos(2\theta) = 1 - 2\sin^2\theta$
  - Version 3: $\cos(2\theta) = 2\cos^2\theta - 1$
  - These three versions are all equivalent
- We can do the same for sine and tangent
- $\sin(2\theta) = 2\sin\theta\cos\theta$
- $\tan(2\theta) = \frac{2\tan\theta}{1 - \tan^2\theta}$

#### Examples
1. Prove $\frac{\sin 3x}{\sin x \cos x} = 4\cos x - \sec x$
   - Sometimes you will not have a clear step of what you should do next, a trick is writing
   - $\frac{\sin 3x}{\sin x \cos x} \to \frac{\sin(x + 2x)}{\sin x \cos x} \to \frac{\sin x \cos 2x + \cos x \sin 2x}{\sin x \cos x}$
   - You may also be able to separate terms from the numerator, which allows you to simplify
   - $\frac{\sin x\cos 2x}{\sin x \cos x} + \frac{\cos x \sin 2x}{\sin x \cos x} = \frac{\cos 2x}{\cos x} + \frac{\sin 2x}{\sin x}$
   - $\frac{2\cos^2{x} - 1}{\cos x} + \frac{2\sin x \cos x}{\sin x} = \frac{2\cos^2{x} - 1}{\cos x} + 2\cos x$
   - To simplify the first term, you can split the single term into two separate fractions with the same denominator
   - $\frac{2\cos^2x}{\cos x} - \frac{1}{\cos x} + 2\cos x$
   - $2\cos x - \frac{1}{\cos x} + 2\cos x = 4\cos x - \sec x$
   - Think about the possible steps where you separate arguments/fractions/etc.
2. Find all solutions for $\sin\theta\cos\theta = -\frac{1}{2}\text{ within }0 \leq \theta \lt 2\pi$
   - Trick here is noticing that $\sin\theta\cos\theta$ is almost equal to our double angle property
   - Multiply both sides by two, you get $2\sin\theta\cos\theta = -1$
   - $\sin(2\theta) = -1$
   - $\sin(A) = -1$ think about what radian will give me -1? Remember our restriction from the problem
   - $A = \frac{3\pi}{2}$ (note that we don't add $2\pi k$ here because we have to stay in the restriction)
   - $2\theta = \frac{3\pi}{2}$ - isolate theta by multiplying both sides by two
   - $\theta = \frac{3\pi}{4}$
3. Solve $\cos(2t) = \cos(t)$ for all solutions within $0 \leq t \lt 2\pi$
   - $\cos(2t) = \cos(t)$
   - $2\cos^2(t) - 1 = \cos(t)$
     - We rewrite it in this version because we already have a cosine on the right hand side
     - This starts to look like a quadratic equation..
   - $2\cos^2(t) - \cos(t) - 1 = 0$
   - $(2\cos(t) + 1)(\cos(t) - 1) = 0$
   - $2\cos(t) + 1 = 0$ and $\cos(t) - 1 = 0$
   - $\cos(t) = -\frac{1}{2}$ or $\cos(t) = 1$
   - $\cos(t) = -\frac{1}{2}$ happens at $\frac{2\pi}{3}, \frac{4\pi}{3}$
   - $\cos(t) = 1$ happens at $0$
   - Note that these are not general solutions, but solutions just within that interval.
   - $\theta = \frac{2\pi}{3}, \frac{4\pi}{3}, 0$ or in set notation $\{\frac{2\pi}{3}, \frac{4\pi}{3}, 0\}$
