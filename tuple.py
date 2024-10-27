# Create a tuple named weather with these elements - (1, 0, 0, 0, 1, 1, 0). If the element is 1 then the value of rainy increases by 1 otherwise the value of sunny increases by 1. On the basis of the value of rainy and sunny, predict the weather.
weather = (1, 0, 0, 0, 1, 1, 0)
sun = 0
ran = 0
for u in weather:
    if u == 1:
        ran = ran+1
    else:
        sun = sun+1
if ran > sun:
    print("its will rain ok yes finall7x")
else:
    print("no rain todaiy :(")