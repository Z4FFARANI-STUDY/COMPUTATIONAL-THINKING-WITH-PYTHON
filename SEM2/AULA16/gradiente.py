import matplotlib.pyplot as plt

r = 255
g = 255
b = 255
cor = []

for j in range(100):
    r -= 10
    g -= 10
    b -= 10
    cor.append([r,g,b] * 30)

plt.imshow(cor)
plt.axis('off')
plt.show()
