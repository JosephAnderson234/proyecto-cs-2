#1
from sklearn.datasets import load_digits
import numpy as np
digits = load_digits()
#2
digit_means = []
for i in range(10):
    mask = digits.target == i
    digit_means.append(np.mean(digits.images[mask], axis=0))
#3
digit_means = np.array(digit_means)


#B
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 10, figsize=(10, 1))
for i, ax in enumerate(axs):
    ax.imshow(digit_means[i], cmap='gray')
    ax.axis('off')
plt.show()
