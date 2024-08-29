import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('manager.csv')
df.index = [1,2,3,4]
df['model'].plot(kind = 'hist')

plt.show()