## Lecture 7: The graph of sine
- Remember that cosine corresponds to x and sine corresponds to y
    - Can help to remember c comes before s in the alphabet and x comes before y, so cosine corresponds to x
- Remember that radians correspond to the independent variable, the dependent variable is made up of the terminal point
- Sine function: $f(\theta) = \sin \theta$
- Trig functions are known as "periodic" functions, which means that they repeat a pattern over and over
- Sine and Cosine look exactly the same, just shifted
- The period we will use for the initial graph is from $0 \to 2\pi$
    - $\sin(\frac{\pi}{2}) = 1$
    - $\sin(\pi) = 0$
    - $\sin(\frac{\pi}{6}) = \frac{1}{2}$
- Code below graphs one period of the sine function
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)

y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label=r'y = $\sin(\theta)$', color='blue', linewidth=2)

plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.title(r'Graph of y = $\sin(\theta)$')
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
- Code below graphs one period of the cosine function
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)

y = np.cos(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label=r'y = $\cos(\theta)$', color='blue', linewidth=2)

plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.title(r'Graph of y = $\cos(\theta)$')
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
- The domain of the sine and cosine functions go from $(-\infty, \infty)$ or $\{\theta|\theta\text{ is }\mathbb{R}\}$
- The range of the sine and cosine functions are $[-1, 1]$
- The sine function is not an "even" function. This means that you cannot reflect the sine function across the y-axis. The sine function is known as an "odd" function
    - An example of this is that $\sin(-\frac{\pi}{2})$ is the same as $-\sin(\frac{\pi}{2})$
    - $\sin(-\frac{\pi}{2}) = -1$ and $-\sin(\frac{\pi}{2}) = -1$
- The cosine function is an "even" function
