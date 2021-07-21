
selection = str(input("Would you like to convert kmh to mph (a) or the other way around(b)? (a/b) "))

if selection == "a":
    kmh = int(input("Enter a speed in km/h: "))
    mph = round(0.6214 * kmh, 1)
    print(kmh, "km/h =", mph, "mph")

if selection == "b":
    mph = int(input("Enter a speed in mph: "))
    kmh = round(mph / 0.6214, 1)
    print(mph, "mph =", kmh, "km/h")
