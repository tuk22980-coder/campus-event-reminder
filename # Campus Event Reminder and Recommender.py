# Campus Event Reminder and Recommender


events = []

def add_event():
    name = input("Enter event name: ")
    category = input("Enter category: ")
    date = input("Enter event date: ")

    event = {
        "name": name,
        "category": category,
        "date": date,
        "rating": 0
    }

    events.append(event)

    print("Event added successfully")


def view_events():

    if len(events) == 0:
        print("No events available")
        return

    print("Upcoming Events:")

    for i, event in enumerate(events, start=1):
        print(i, event["name"], event["category"], event["date"], "Rating:", event["rating"])


def recommend_events():

    interest = input("Enter interest category: ")

    print("Recommended Events:")

    found = False

    for event in events:
        if event["category"] == interest:
            print(event["name"], event["date"])
            found = True

    if found == False:
        print("No matching events found")


def rate_event():

    if len(events) == 0:
        print("No events to rate")
        return

    view_events()

    choice = int(input("Enter event number to rate: "))

    if choice >= 1 and choice <= len(events):

        rating = int(input("Enter rating 1-5: "))

        if rating >= 1 and rating <= 5:
            events[choice-1]["rating"] = rating
            print("Rating saved")

        else:
            print("Invalid rating")

    else:
        print("Invalid event number")


def top_rated_event():

    if len(events) == 0:
        print("No events available")
        return

    highest = events[0]

    for event in events:
        if event["rating"] > highest["rating"]:
            highest = event

    print("Top Rated Event:")
    print(highest["name"], highest["rating"])


# starter events
events.append({
"name":"Career Fair",
"category":"career",
"date":"May 3",
"rating":4
})

events.append({
"name":"Spring Festival",
"category":"social",
"date":"May 8",
"rating":5
})


while True:

    print("Campus Event Recommender")
    print("1 Add Event")
    print("2 View Events")
    print("3 Get Recommendations")
    print("4 Rate Event")
    print("5 Top Rated Event")
    print("6 Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_event()

    elif choice == "2":
        view_events()

    elif choice == "3":
        recommend_events()

    elif choice == "4":
        rate_event()

    elif choice == "5":
        top_rated_event()

    elif choice == "6":
        break

    else:
        print("Invalid choice")