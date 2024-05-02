import matplotlib.pyplot as plt

x_value = range(1, 5001)
y_vallue = [x**3 for x in x_value]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.scatter(x_value, y_vallue, c = y_vallue, cmap = plt.cm.spring, s = 10)
ax.axis([0, 5100, 0, 5100**3])
ax.set_title("Cubic Numbers", fontsize = 24)
ax.set_xlabel("Input", fontsize = 14)
ax.set_ylabel("Output", fontsize = 14)

ax.tick_params(labelsize = 10)

plt.show()