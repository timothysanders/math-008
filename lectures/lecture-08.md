## Lecture 8: Graphs of tangent and cosine
- See above for a graph of the cosine function
    - The graph can be considered slightly "shifted" from the sine function
    - Remember that cosine pertains to the $x$-coordinates
    - $\cos(0) = 1$
    - $\cos(\pi) = -1$
    - $\cos(\frac{\pi}{2}) = 0$
- The domain of the cosine function goes from $(-\infty, \infty)$ or $\{\theta|\theta\text{ is }\mathbb{R}\}$
- The range of the cosine functions is $[-1, 1]$
- Remember that cosine is an "even" function
    - $f(-\theta) = f(\theta)$
    - $\cos(-\theta) = \cos(\theta)$
    - Example: $\cos(-\frac{\pi}{3}) = \cos(\frac{\pi}{3})$
    - These cosine function results are not in the same position, but give you the same values
- Tangent function is $f(\theta) = \tan(\theta) = \frac{y}{x}$
- Code below shows the graph of the tangent function, there are vertical asymptotes (the function is undefined) at points where $x = 0$ (such as $\frac{\pi}{2}$ and $\frac{3\pi}{2}$) because the function is $\frac{y}{x}$
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)

y = np.tan(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label=r'y = $\tan(\theta)$', color='blue', linewidth=2)

asymptotes = [np.pi/2, 3*np.pi/2]
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
```
- The domain of the tangent function needs to exclude independent variables where $x = 0$
- At the vertical asymptote, our graph approaches the asymptote, but does not ever reach it
- The tangent function (like sine and cosine) is a periodic function, so the same shape repeats over and over
- Similar to sine, this is not an even function, but is an "odd"
    - $\tan(-\theta) = -\tan(\theta)$
- The domain of tangent function is $\{\theta\mid\theta\in\mathbb{R}, \theta \ne \frac{\pi}{2} + \pi k,k\in\mathbb{Z}\}$ (where K is an integer)
- The range of tangent function is $(-\infty, \infty)$
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
