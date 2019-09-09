import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np

x = np.linspace(0, 5, 11)
x

y = x * x
y

# funcional

plt.plot (x, y, 'r--')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Título')
plt.show()

# com 2 gráficos

plt.subplots(nrows=1, ncols=2)
plt.show()