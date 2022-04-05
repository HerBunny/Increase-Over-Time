import math

qty = int(input("Please enter your initial value: "))
time = 365
val = qty
print()

count = []

while time > 0:
  val = math.ceil(val * 1.05)
  count.append(val)
  time = time - 1
  if val > 24000:
    print()
    print(len(count))
    break 
  else:
    print(val)
