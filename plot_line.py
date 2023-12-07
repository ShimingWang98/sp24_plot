
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(4, 4))
plt.subplots_adjust(bottom=0.18)

# # print the first line
# f_values = np.array([1, 2, 3, 4, 5, 6, 7])
# xi_hat = np.array([0.996, 1.973, 3, 3.99, 4.42, 4.57, 4.6])
# epsc = np.array([1, 2, 3, 3.99, 4.7, 5.5, 6])
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.default'] = 'rm'
f_values = np.array([1, 2, 3, 4, 5, 6])
xi_hat = np.array([0.998,	1.99,	2.71,	2.9,	2.96,	2.97])
epsc = np.array([1, 2, 2.9, 3.2, 4, 4.7])

epsilon_star = f_values
plt.plot(f_values, xi_hat, marker='o', color='#AE3C22', markersize=9,linewidth=3,label=r'${\xi}$')

plt.plot(f_values, epsc, marker='',color='#4480d1', markersize=9, linewidth=3,label=r'$\epsilon_c$')

# print the second line
plt.plot(f_values, epsilon_star, marker='s',color='#ffc046', markersize=9, linewidth=3,label=r'$\epsilon^*$')

# print the third line
# plt.plot(f_values, xi_star_hat, marker='*', markersize=9,linewidth=3,label=r'$\hat{\xi}^*$')
plt.grid(axis='x', linestyle='--', linewidth=0.5)
plt.fill_between(f_values, xi_hat, epsilon_star, color='#4480d1', alpha=0.3)
plt.legend(fontsize=20)
plt.xlabel(r'$\theta$', fontsize=20)
# plt.ylabel('Value', fontsize=22)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
# plt.legend(fontsize=22)
plt.grid(True)
plt.savefig('plot/benchmark_lap.pdf')