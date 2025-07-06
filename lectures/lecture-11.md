## Lecture 11: More Transformations
- You can break down the functions into three steps
  1. Period
  2. Phase shift
  3. Amplitude
- $g(x) = \tan(2x - \pi) + 1$
  - Period: $\frac{\pi}{2}$
  - Phase shift: $\frac{\pi}{2}$
  - Amplitude: $|1|$ (though technically tangent has no amplitude)
  - Because it is tangent, the period is only $\pi$, but because it is $2x$ in the function, our period is $\frac{pi}{2}$
  - Tangent has vertical asymptotes at $\frac{\pi}{2}$ and $-\frac{\pi}{2}$
  - $\tan(2x)$
    - Because we are multiplying by 2 inside the function, we do the opposite and divide by 2
    - Vertical asymptotes become $\frac{\pi}{4}$ and $-\frac{\pi}{4}$
    - This does not shift the graph, but rather shrinks it horizontally
  - $\tan(2x - \pi) \to \tan(2(x - \frac{\pi}{2}))$
    - Because we are subtracting inside the function, we are shifting **right** by $\frac{\pi}{2}$
    - Vertical asymptotes shift right by $\frac{\pi}{2}$ and are $\frac{\pi}{4}; \frac{3\pi}{4}$
  - $\tan(2x - \pi) + 1$
    - Vertical asymptotes are in the same place, but the graph shifts upward by one
```python
import numpy as np
import matplotlib.pyplot as plt

# Graph initial parent function
x = np.linspace(-np.pi/2, 2 * np.pi, 1000)
y = np.tan(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label=r'y = $\tan(\theta)$', color='blue', linewidth=2)

asymptotes = [-np.pi/2, np.pi/2]
for a in asymptotes:
  plt.axvline(a, color='red', linestyle='--', linewidth=1.5, label='Asymptote' if a==asymptotes[0] else "")

plt.ylim(-5, 5)
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.title(r'Graph of y = $\tan(\theta)$')
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.legend()

xticks = np.arange(0, 2 * np.pi + 0.1, np.pi / 2)
xtick_labels = ['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']
plt.xticks(xticks, xtick_labels)

plt.show()


x = np.linspace((-np.pi)/4, 2 * np.pi, 1000)
y = np.tan(2*x - np.pi) + 1

plt.figure(figsize=(8, 4))
plt.plot(x, y, label=r'y = $\tan(2\theta - \pi) + 1$', color='blue', linewidth=2)

asymptotes = [(-np.pi)/4, np.pi/4, (3 * np.pi)/4]
for a in asymptotes:
    plt.axvline(a, color='red', linestyle='--', linewidth=1.5, label='Asymptote' if a==asymptotes[0] else "")

plt.ylim(-5, 5)
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.title(r'Graph of y = $\tan(2\theta - \pi) + 1$')
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.legend()

xticks = np.arange(0, 2 * np.pi + 0.1, np.pi / 2)
xtick_labels = ['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']
plt.xticks(xticks, xtick_labels)

plt.show()
```
- $y = 1 - \frac{1}{2}\csc(3x + \frac{\pi}{2})$
  - Period: $\frac{2\pi}{3}$
  - Phase shift: $\frac{\pi}{6}$
  - Amplitude: $|-\frac{1}{2}|$
  - Note: $\csc(\theta) = \frac{1}{y}$; cannot have zero in your denominator
    - Therefore, vertical asymptotes occur at $0, \pi, 2\pi$
  - $\csc(3x)$
    - Period becomes $\frac{2\pi}{3}$
  - $\csc(3x + \frac{\pi}{2}) \to \csc(3(x + \frac{\pi}{6}))$
    - Because there is addition inside the function, we move left by $\frac{\pi}{6}$
    - Vertical asymptotes are at $-\frac{\pi}{6}; \frac{\pi}{6}; \frac{\pi}{2}$
  - $-\frac{1}{2}\csc(3(x + \frac{\pi}{6}))$
    - We have a reflection happening and a vertical shrinking
  - $1-\frac{1}{2}\csc(3(x + \frac{\pi}{6}))$
    - Points move up one