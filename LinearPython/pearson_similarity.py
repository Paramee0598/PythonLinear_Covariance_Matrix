import numpy as np
import matplotlib.pyplot as plt

x_simple = np.array([-2, -1, 0, 1, 2])
y_simple = np.array([4, 1, 3, 2, 0])
my_rho = np.corrcoef(x_simple, y_simple)

seed = 13
rand = np.random.RandomState(seed)

x = rand.uniform(0,1,100)
x = np.vstack((x,x*2+1))
x = np.vstack((x,-x[0,]*2+1))
x = np.vstack((x,rand.normal(1,3,100)))

fig, ax = plt.subplots(nrows=2, ncols=4, figsize=(15, 8))

for noise, i in zip([0.05, 0.2, 0.8, 2], [0, 1, 2, 3]):
    # Add noise
    x_with_noise = x + rand.normal(0, noise, x.shape)

    # Compute correlation
    rho_noise = np.corrcoef(x_with_noise)

    # Plot column wise. Positive correlation in row 0 and negative in row 1
    ax[0, i].scatter(x_with_noise[0,], x_with_noise[1,], color='magenta')
    ax[1, i].scatter(x_with_noise[0,], x_with_noise[2,], color='green')
    ax[0, i].title.set_text('Correlation = ' + "{:.2f}".format(rho_noise[0, 1])
                            + '\n Noise = ' + "{:.2f}".format(noise))
    ax[1, i].title.set_text('Correlation = ' + "{:.2f}".format(rho_noise[0, 2])
                            + '\n Noise = ' + "{:.2f}".format(noise))
    ax[0, i].set(xlabel='x', ylabel='y')
    ax[1, i].set(xlabel='x', ylabel='y')

fig.subplots_adjust(wspace=0.3, hspace=0.4)
plt.show()
