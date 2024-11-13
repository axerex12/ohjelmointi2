from matplotlib import pyplot as plt, patches
import numpy as np

# Luo yksikköympyrän kuvaaja
fig = plt.figure()
ax = fig.subplots()

# Piirretään ympyrä keskipisteessä (0, 0) ja säde = 1
ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

# Keskitetään koordinaatisto
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.axis('equal')

# Asetetaan asteikot
plt.xticks([-1, 0, 1])
plt.yticks([-1, 0, 1])

# Määritetään kulmat radiaaneina
angles_deg = [30, 45, 60, 90, 120, 150, 180, 270]
angles_rad = np.radians(angles_deg)
labels = [r"$30^\circ$", r"$45^\circ$", r"$60^\circ$", r"$90^\circ$",
          r"$120^\circ$", r"$150^\circ$", r"$180^\circ$", r"$270^\circ$"]

# Lasketaan kulmien sini- ja kosini-arvot
x = np.cos(angles_rad)
y = np.sin(angles_rad)

# Piirretään pisteet ja merkitään kulmien nimet
plt.scatter(x, y, color='blue', marker='X')
for i, label in enumerate(labels):
    plt.annotate(label,
                 (x[i], y[i]),
                 textcoords="offset points",
                 xytext=(5,5),
                 ha='center')

plt.title("Yksikköympyrä tärkeimmillä kulmilla")
plt.show()
