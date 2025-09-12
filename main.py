import math

x = 2*math.pi/3
y = abs(x * ((math.sin(x**3) / math.tan(2 * x**2)) + (math.cos(x) * math.cos(x) / (math.atan2( x ** 3,1) ** 3))))

print(y)
