import math

theta = float(input("enter Theta in degrees "))
radius = float(input("enter radius "))

def chord(r, t):
  a = (t / 360) * math.pi * r * r
  b = 0.5 * r * r * math.sin(t * (math.pi / 180))

  return a - b

print("chord of the circe is " + str(chord(radius, theta)))
