## Lecture 9: Graphs of cotangent and secant
- Code below shows the graph of the cotangent function, there are vertical asymptotes (the function is undefined) at points where $y = 0$ (such as $\pi$ and $2\pi$) because the function is $\frac{x}{y}$
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)

y = 1/np.tan(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label=r'y = $\cot(\theta)$', color='blue', linewidth=2)

asymptotes = [0, np.pi, 2 * np.pi]
for a in asymptotes:
    plt.axvline(a, color='red', linestyle='--', linewidth=1.5, label='Asymptote' if a==asymptotes[0] else "")

plt.ylim(-5, 5)
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.title(r'Graph of y = $\cot(\theta)$')
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
- There are terminal points where $(x, y)$ are the same values, just with different signs
- Compared to tangent, the graph of cotangent has asymptotes at the multiples of $\pi$, tangent has asymptotes at multiples of $\frac{\pi}{2}$
- Cotangent is a periodic function, as well as an odd function (similar to tangent)
- Domain: $\{\theta\mid\theta\in\mathbb{R}, \theta \ne 0 +\pi k,k\in\mathbb{Z}\}$
- Range: $(-\infty, \infty)$
- Code below shows the graph of secant (reciprocal of cosine)
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)

y = 1/np.cos(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label=r'y = $\sec(\theta)$', color='blue', linewidth=2)

asymptotes = [np.pi/2, 3*np.pi/2]
for a in asymptotes:
    plt.axvline(a, color='red', linestyle='--', linewidth=1.5, label='Asymptote' if a==asymptotes[0] else "")

plt.ylim(-5, 5)
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.title(r'Graph of y = $\sec(\theta)$')
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
- Domain: $\{\theta\mid\theta\in\mathbb{R}, \theta \ne \frac{\pi}{2} +\pi k,k\in\mathbb{Z}\}$
- Range:
- Because secant is $\frac{1}{x}$, we cannot have $x$ values that equal 0
- This means that secant has vertical asymptotes wherever cosine = 0
- Code below shows the graph of cosecant (reciprocal of sine)
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)

y = 1/np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label=r'y = $\csc(\theta)$', color='blue', linewidth=2)

plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.title(r'Graph of y = $\csc(\theta)$')
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
