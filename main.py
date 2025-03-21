import matplotlib.pyplot as plt
import numpy as np

# data:
frequencies1 = [1000.00, 100.00, 10.00, 3.00, 2.00, 1.10, 1.00, 0.9, 0.8, 0.50, 0.10]
H_values1 = [1.10, 1.09, 1.09, 1.11, 1.10, 0.86, 0.77, 0.69, 0.57, 0.27, 0.06]

frequencies2 = [1, 5, 10, 30, 35, 40, 45, 50, 100]
H_values2 = [1.84, 1.84, 1.84, 1.74, 1.70, 1.41, 1.08, 0.28, 0.05]

H1_dB = 20 * np.log10(H_values1)
H2_dB = 20 * np.log10(H_values2)


# choose which data to plot
H_dB = H1_dB
frequencies = frequencies1


print(H_dB)

# -3 dB line:
H_dB_minus3 = max(H_dB)-3

# plot the graph
plt.plot(frequencies, H_dB, marker='o', label='K_v [dB]')


# find the closest point from the H_db to -3 dB
index_closest = np.argmin(np.abs(H_dB - H_dB_minus3))
frequency_at_minus3dB = frequencies[index_closest]

# add -3 dB horizontal line
plt.axhline(y=H_dB_minus3, color='r', linestyle='--', label='-3 dB')

# -3 dB vertical line
plt.axvline(x=frequency_at_minus3dB, color='g', linestyle=':', label=f'-3 dB: {frequency_at_minus3dB} Hz')

# labels
plt.xlabel('f [Hz]')
plt.ylabel('K_v [dB]')

# display
plt.yticks([-25, -20, -15, -10, H_dB_minus3, -5 ,0, 5]) # choose
plt.xscale('log')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()

#save as png in current folder
plt.savefig("graph.png")