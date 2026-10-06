# a) numarul de pasi ai jocului urmeaza distributia geometrica cu probabilitatea p (probabilitatea de a pica stema)
# b)
import numpy as np
import matplotlib.pyplot as plt
def simulate_game(p: float=0.5) -> (int, float):
    coin = np.random.rand()>=p
    if coin: # cap/ban
        runs, money_delta = simulate_game()
        return (runs+1, money_delta-0.5)
    else: # stema
        return (1, np.random.randint(1,7)-3)

print(simulate_game())
# c)

def simulate_games(p: float=0.5, iter_cnt=1000000):
    sums = []
    steps = []
    for _ in range(iter_cnt):
        step_cnt, sum = simulate_game(p)
        sums.append(sum)
        steps.append(step_cnt)

    plt.hist(sums, bins=15, alpha=0.7, color='lightgreen', edgecolor='black')
    plt.title('Distributia sumelor')
    plt.xlabel('Suma')
    plt.ylabel('Frecventa')
    plt.show()

    avg = 0
    for it in sums:
        avg += it
    avg /= len(sums)
    print("Mean sum: ", avg)


simulate_games()

# d)
simulate_games(p=0.3)
simulate_games(p=0.7)

