from medical_data_visualizer import draw_cat_plot, draw_heat_map
import matplotlib.pyplot as plt

# Categorical plot
fig1 = draw_cat_plot()
fig1.savefig('catplot.png')  # save figure if you want

# Heat map
fig2 = draw_heat_map()
fig2.savefig('heatmap.png')  # save figure if you want

plt.show()  # optionally show the plots