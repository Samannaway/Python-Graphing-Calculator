import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk


root = tk.Tk()
root.title("Graphing calculator ")


label = tk.Label(root, text="Test program", font=32)
label.pack()


fig, ax = plt.subplots(figsize=(10, 8))


x = np.linspace(-10000, 10000, 100000)
y1 = x**2
y2 = np.sin(x)
y3 = np.cos(x)


ax.plot(x, y1, label="x²")
ax.plot(x, y2, label="sin(x)")
ax.plot(x, y3, label="cos(x)")


ax.grid(True)
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_title("Multi Function")
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)


ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')


ax.spines['left'].set_color("#000000")
ax.spines['bottom'].set_color("#000000")


ax.xaxis.set_minor_locator(tck.AutoMinorLocator())
ax.yaxis.set_minor_locator(tck.AutoMinorLocator())


ax.grid(which='minor',linestyle='-', linewidth=0.5, color="#b7e1a1")
ax.grid(which='major',linestyle='-', linewidth=1, color="#2a7319")


ax.tick_params(which='minor', length=4, width=0.5, color='grey')




ax.tick_params(axis='x', colors="#2E2B28")
ax.tick_params(axis='y', colors="#2E2B28")


ax.xaxis.label.set_color("#A058FF")
ax.yaxis.label.set_color("#A058FF")


ax.legend()


canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
toolbar.pack(side=tk.TOP, fill=tk.X)


root.mainloop()
