selection = str(input("Would you like to convert Celsius to Fahrenheit (a) or the other way around(b)? (a/b) "))

if selection == "a":
    c = int(input("Enter a temperature in Celsius: "))
    f = round((c * (9/5)) + 32, 2)
    print(c, "Celsius =", f, "Fahrenheit")

if selection == "b":
    f = int(input("Enter a temperature in Fahrenheit: "))
    c = round((f - 32) * 5/9, 2)
    print(f, "Fahrenheit =", c, "Celsius")
