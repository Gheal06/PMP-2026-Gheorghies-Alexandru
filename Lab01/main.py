import numpy as np
import pymc as pm
import numpy as np
import matplotlib.pyplot as plt
import arviz as az

np.random.seed(998244353)

def run():
    r = 3 # rosii
    a = 4 # albastre
    n = 2 # negre
    dice = np.random.randint(1,6)
    if dice in (2, 3, 5):
        n = n + 1
    elif dice == 6:
        r = r + 1
    else:
        a = a + 1

    choice = np.random.randint(1, n+r+a)
    if choice <= r:
        return 0 # rosu
    elif choice <= r+a:
        return 1 # albastru
    else:
        return 2

def runs(iter_cnt):
    results = (run() for i in range(iter_cnt))
    plt.hist(results, bins=3, alpha=0.7, color='lightgreen', edgecolor='black')
    plt.title('Distribuția culorilor')
    plt.xlabel('Culoare')
    plt.ylabel('Număr de Experimente')
    plt.show()

runs(1000)