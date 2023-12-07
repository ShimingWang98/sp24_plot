
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# # Placeholder data for 'xi' and 'epsilon' values
# # high privacy
# epsc_values = [0, 0, 0]
# xi_values = [0.016, 0.036, 0.09]
# epsilon_values = [0.25 - 0.016, 0.5 - 0.036, 1 - 0.09]
# epsilon_values_show = [0.25, 0.5, 1]
# experiments = [r'$\widetilde{\theta_1}=19$', r'$\widetilde{\theta_1}=10$', r'$\widetilde{\theta_1}=5.1$']
# vertical_line_positions = [0.05, 0.10, 0.2]
# vertical_line_labels = ['0.05', '0.1', '0.2']
#
# # medium privacy
# epsc_values = [0, 0, 0]
# xi_values = [0.37,
# 0.423,
# 0.792]
# epsilon_values = [3.5-0.37,
# 5-0.423,
# 7.5-0.792]
# epsilon_values_show = [3.5,
# 5,
# 7.5]
# experiments = [r'$\widetilde{\theta_1}=19$', r'$\widetilde{\theta_1}=10$', r'$\widetilde{\theta_1}=5.1$']
# vertical_line_positions = [0.7,
# 1,
# 1.5]
# vertical_line_labels = ['0.7', '1.0', '1.5']


# high privacy
epsc_values = [0, 0, 0]
xi_values = [1.45,
2.496,
2.91]
epsilon_values = [15-1.45,
25-2.496,
35-2.91]
epsilon_values_show = [15,
25,
35]
experiments = [r'$\widetilde{\theta_1}=19$', r'$\widetilde{\theta_1}=10$', r'$\widetilde{\theta_1}=5.1$']
vertical_line_positions = [3,5,7]
vertical_line_labels = ['3.0', '5.0', '7.0']

# Set the height of the bars
bar_height = 0.2
# Define the y positions to increase spacing
y_positions = [0, 0.25, 0.5]  # Increase the gaps by adjusting these values

plt.rcParams.update({'font.size': 18})
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.default'] = 'rm'
# Create the figure and the horizontal bar plot
fig, ax = plt.subplots(figsize=(10, 2.5))

# yellow ffc046
# red AE3C22


# Plotting 'xi' values
xi_bars = ax.barh(y_positions, xi_values, height=bar_height, color='#AE3C22', edgecolor='none', label=r'$\xi^*(\widetilde{\theta})$')

# Plotting 'epsilon' values starting where 'xi' values end
epsilon_bars = ax.barh(y_positions, epsilon_values, left=xi_values, height=bar_height, color='#ffc046', edgecolor='none', label=r'$\epsilon^*(\widetilde{\theta})$')

# Plotting 'epsc' values as transparent bars to create gaps
epsc_bars = ax.barh(y_positions, epsc_values, left=epsilon_values, height=bar_height, color='none', edgecolor='none', label=r'$\epsilon_c$')

# Add text labels for 'xi' values to the right of the bars
# for y, xi in zip(y_positions, xi_values):
#     if xi < 0.03:
#         continue
#     plt.text(xi + 0.001, y, f'{xi:.2f}', ha='left', va='center', color='#ffc046', rotation=0, fontsize=18)

# Add text labels for 'epsilon' values to the right of the bars
for y, epsilon in zip(y_positions, epsilon_values_show):
    plt.text(epsilon + 0.01, y, f'{epsilon:.2f}', ha='left', va='center', color='#ffc046', rotation=0, fontsize=20)

for y_pos, line_x, label in zip(y_positions, vertical_line_positions, vertical_line_labels):
    plt.plot([line_x, line_x], [y_pos - bar_height / 2, y_pos + bar_height / 2], color='#4480d1', linewidth=4)
    # Adding labels next to the vertical lines
    plt.text(line_x + 0.4, y_pos, label, color='#4480d1', ha='left', va='center',rotation=0, fontsize=20)
# ax.legend(loc='lower right', ncol=6, bbox_to_anchor=(1, 0), fontsize=14)


ax.set_title(r'Adapted SVT mechanism $M^{svt}_{\tilde{\theta}}$ against DP-Sniper')
ax.set_yticks(y_positions)
ax.set_yticklabels(experiments)

# Adding a grid in x-axis to make the data points easier to read
plt.grid(axis='x', linestyle='--', linewidth=0.5)

# Removing the top and right spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adjust the subplot params so the text doesn't go off the image
plt.tight_layout()

# Save the figure and return the path
plt.savefig('plot/adapted_svt_sniper_3.pdf')
