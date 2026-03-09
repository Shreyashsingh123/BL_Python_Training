import math
t = float(input("Enter temperature: "))
v = float(input("Enter wind speed: "))

def wind_chill(t, v):
    return 35.74 + 0.6215*t - 35.75*math.pow(v, 0.16) + 0.4275*t*math.pow(v, 0.16)

if t > 50 or v < 3 or v > 120:
    print("Invalid value")
else:
    w = wind_chill(t, v)
    print("Wind Chill is :", w)