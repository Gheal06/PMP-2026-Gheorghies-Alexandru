import numpy as np
import matplotlib.pyplot as plt
import arviz as az
import math
print(az.__version__)
# de ce probabilitatile la frizeri sunt asa:
# presupunand ca frizerii sunt ocupati la fel de mult timp T,
# timpul expected de a termina un client este 1/lambda
# numarul expected de clienti este T/(1/lambda) = T*lambda
# cum numarul expected de clienti este proportional cu lambda (iar T este constant),
# decurge natural ca probabilitatea ca un client sa fie assignat la un frizer 
# sa fie egala cu rata medie a acestuia de lucru
def run():
    frizer = np.random.randint(13)
    if frizer < 3:
        l = 3
    elif frizer < 3+6:
        l = 6
    else:
        l = 4
    return np.random.exponential(1.0/l)

def runs(iter_cnt: int = 10000):
    outcomes = [run()*60 for _ in range(iter_cnt)] # ore -> minute

    print("Mean: ", np.mean(outcomes))
    print("Stdev: ", np.std(outcomes))
    az.plot_kde(np.array(outcomes))
    plt.xlabel("Values")
    plt.title("Kernel Density Estimate")
    plt.show()

runs()