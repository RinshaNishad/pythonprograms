user=input("is it raining (yes/no) : ").strip().lower()
if user=="yes":
    windy=input("is it windy (yes/no) : ").strip().lower()
    if windy=="yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")

