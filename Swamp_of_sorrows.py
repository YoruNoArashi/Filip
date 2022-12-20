import matplotlib.pyplot as plt

k = int(input("číslem napiš hodnotu k: "))
q = int(input("číslem napiš hodnotu q: "))

x=range(-10, 11)
y=[k*xi + q for xi in x]

plt.plot(x,y)
plt.xlabel("x")
plt.xlabel("y")
plt.show()