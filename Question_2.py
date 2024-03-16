#Task 1
attendees = float(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#Task 2
audio_system = "surround sound" if attendees >= 50 else "JBL speakers"
print(audio_system)

projector = "fun" if attendees <= 20 else "Why are we watching movies?"
print(projector)

#Task 3
food = input("Would you like to have vegatarian food served? ")

if food == "veg":
    print("Well then I recommend Veggie Delight Caterers!")
else:
    print("Well then I recommend Gourmet Meals Caterers")