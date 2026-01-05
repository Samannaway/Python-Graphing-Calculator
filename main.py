import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore
import matplotlib.ticker as ticker # type: ignore
import interface as interface
import matplotlib.pyplot as plt # type: ignore
import matplotlib.ticker as tck # type: ignore


fix, ax = plt.subplots(figsize=(9, 8), dpi=100)
finalVariableList = interface.interFaceOutput.finalListReturn()


x = np.linspace(-10000, 10000, 100000)
y = 0


for i in finalVariableList:

    print(finalVariableList)

    if len(i) == 2:  
        if i[1] != "c":
            y += ( (x**int(i[1]))  *int(i[0]))
        else:
            y+= int(i[0])
    else:
        y += (x*int(i[0]))

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

ax.plot(x,y)

plt.show()
