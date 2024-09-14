import matplotlib.pyplot as plt

horizontal = [[[0,0,0], [255,255,255]] * 4]
vertical = [[[255,255,255], [0,0,0]] * 4]

plt.imshow((horizontal + vertical) * 4)
plt.axis('off')
plt.show()

