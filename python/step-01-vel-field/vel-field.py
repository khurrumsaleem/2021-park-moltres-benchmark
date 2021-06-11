import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
sys.path.append(
        os.path.dirname(
                os.path.dirname(
                        os.path.abspath(__file__))))
from common_func import get_disc

# Data
aa = pd.read_csv('vel-field_csv_aa_0002.csv')
bb = pd.read_csv('vel-field_csv_bb_0002.csv')
benchmark_aa_ux = pd.read_csv('ux_AA', delim_whitespace=True, header=None)
benchmark_aa_uy = pd.read_csv('uy_AA', delim_whitespace=True, header=None)
benchmark_bb_ux = pd.read_csv('ux_BB', delim_whitespace=True, header=None)
benchmark_bb_uy = pd.read_csv('uy_BB', delim_whitespace=True, header=None)

# Calculate % discrepancy
disc_aa_ux = get_disc(aa['vel_x'] / 100, benchmark_aa_ux)
disc_aa_uy = get_disc(aa['vel_y'] / 100, benchmark_aa_uy)
disc_bb_ux = get_disc(bb['vel_x'] / 100, benchmark_bb_ux)
disc_bb_uy = get_disc(bb['vel_y'] / 100, benchmark_bb_uy)

print("Discrepancy in ux along AA' = " + str(disc_aa_ux*100) + " %")
print("Discrepancy in uy along AA' = " + str(disc_aa_uy*100) + " %")
print("Discrepancy in ux along BB' = " + str(disc_bb_ux*100) + " %")
print("Discrepancy in uy along BB' = " + str(disc_bb_uy*100) + " %")

ave_aa_ux = 0
ave_aa_uy = 0
ave_bb_ux = 0
ave_bb_uy = 0
for i in range(4):
    ave_aa_ux += get_disc(benchmark_aa_ux[:][i+1], benchmark_aa_ux)
    ave_aa_uy += get_disc(benchmark_aa_uy[:][i+1], benchmark_aa_uy)
    ave_bb_ux += get_disc(benchmark_bb_ux[:][i+1], benchmark_bb_ux)
    ave_bb_uy += get_disc(benchmark_bb_uy[:][i+1], benchmark_bb_uy)
ave_aa_ux /= 4
ave_aa_uy /= 4
ave_bb_ux /= 4
ave_bb_uy /= 4

print("Benchmark average discrepancy in ux along AA' = " +
      str(ave_aa_ux*100) + " %")
print("Benchmark average discrepancy in uy along AA' = " +
      str(ave_aa_uy*100) + " %")
print("Benchmark average discrepancy in uy along BB' = " +
      str(ave_bb_ux*100) + " %")
print("Benchmark average discrepancy in uy along BB' = " +
      str(ave_bb_uy*100) + " %")

# %% Plot
y = np.linspace(0, 2, 201)
code = ['Moltres', 'CNRS', 'Polimi', 'PSI', 'TUD']

plt.rc('font', size=12)          # controls default text sizes
plt.rc('axes', titlesize=12)     # fontsize of the axes title
plt.rc('axes', labelsize=12)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=11)    # fontsize of the tick labels
plt.rc('ytick', labelsize=11)    # fontsize of the tick labels
plt.rc('legend', fontsize=12)    # legend fontsize
plt.rc('figure', titlesize=12)  # fontsize of the figure title

fig, ax = plt.subplots(figsize=[6, 5])
ax.plot(bb['vel_x'] / 100, y, label='Moltres', color='tab:blue')
ax.plot(benchmark_bb_ux[:][1], y, label='CNRS', color='tab:orange',
        linestyle='--')
ax.plot(benchmark_bb_ux[:][2], y, label='Polimi', color='tab:green',
        linestyle=':')
ax.plot(benchmark_bb_ux[:][3], y, label='PSI', color='tab:red',
        linestyle='-.')
ax.plot(benchmark_bb_ux[:][4], y, label='TUD', color='tab:purple',
        linestyle=(0, (3, 1, 1, 1, 1, 1)))
ax.legend()
ax.grid()
ax.set_xlim(-0.2, 0.6)
ax.set_ylim(0, 2)
ax.set_xlabel(r'$u_x$ [m$\cdot$s$^{-1}$]')
ax.set_ylabel(r'$y$ [m]')
plt.savefig('0-1-vel-plot.png', dpi=400)

# %% Table data

x = np.arange(0, 201, 25)
aa_ux = np.zeros(len(x))
aa_uy = np.zeros(len(x))
bb_ux = np.zeros(len(x))
bb_uy = np.zeros(len(x))

for i in range(len(x)):
    aa_ux[i] = aa['vel_x'][x[i]]
    aa_uy[i] = aa['vel_y'][x[i]]
    bb_ux[i] = bb['vel_x'][x[i]]
    bb_uy[i] = bb['vel_y'][x[i]]

print(aa_ux)
print(aa_uy)
print(bb_ux)
print(bb_uy)
