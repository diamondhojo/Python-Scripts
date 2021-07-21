import time

raining = input("Is it raining right now? ")

if raining == "yes":
    umbrella = input("Do you have an umbrella? ")
    if umbrella == "yes":
        print("Go outside")
    elif umbrella == "no":
        while raining == "yes":
            print("Waiting for it to stop raining...")
            time.sleep(2)
            raining = input("Is it still raining? ")
            if raining == "no":
                print("Go outside")
elif raining == "no":
    print("Go outside")
else:
    print("Answer yes or no")
