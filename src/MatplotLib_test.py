import matplotlib.pyplot as plt
w = 8
h = 6
d = 70
plt.figure(figsize=(w, h), dpi=d)
y1 = [2, 3, 4.5]
y2 = [1, 1.5, 5]
plt.plot(y1)
plt.plot(y2)
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*1, box.height])
legend_x = 1
legend_y = 0.5
plt.legend(["blue", "green"], loc='center left', bbox_to_anchor=(legend_x, legend_y))
plt.savefig("out.png")
plt.show()