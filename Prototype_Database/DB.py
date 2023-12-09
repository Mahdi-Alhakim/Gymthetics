"""

This is a temporary storage for the prototype app, and by no means would this be used for production of the application.

"""

ExerciseQuotes = [
    "Of course it’s hard. It’s supposed to be hard.\n If it were easy, everybody would do it.\n Hard is what makes it great.",
    "No pain, no gain. Shut up and train.",
    "Your body can stand almost anything. It’s\n your mind that you have to convince.",
    "Success isn’t always about greatness.\n It’s about consistency. Consistent hard\n work gains success. Greatness will come.",
    "Train insane or remain the same.",
    "Definition of a really good workout:\n when you hate doing it, but\n you love finishing it.",
    "Push yourself because no\n one else is going to do it for you.", "Success starts with self-discipline.",
    "Good things come to those who sweat.", "Motivation is what gets you started.\n Habit is what keeps you going.",
    "A one hour workout is 4% of your day.\n No excuses.", "The body achieves what the mind believes.",
    "What seems impossible today will\n one day become your warm-up.",
    "Never give up on a dream just\n because of the time it will take to\n accomplish it. The time will pass anyway.",
    "Someone busier than you is\n working out right now.", "Hustle for that muscle.",
    "Work hard in silence. Let success be your noise.",
    "If you still look good at the end\n of your workout, you didn’t\n train hard enough.",
    "When you feel like quitting think\n about why you started.",
    "A good workout is when you make your\n dry fit shirt look like false advertising.",
    "I don’t count my sit-ups. I only start\n counting when it starts hurting because\n they’re the only ones that count.",
    "It comes down to one simple thing:\n how bad do you want it?", "Making excuses burns zero calories per hour."]

GYMSET = {"Cardio": ["The treadmill", "Rowing machine", "Elliptical machine", "Upright bike", "Stair mill",
                     "Recumbent exercise bike", "Spin bike"],
          "Lower Body": ["Leg press machine", "Hack squat machine", "Leg extension machine", "Leg curl machine",
                         "Seated calf machine", "Standing calf machine", "Leg abduction machine",
                         "Leg adduction machine", "Lat pulldown machine", "Exercise mat", "Flat bench",
                         "Adjustable bench"],
          "Upper Body": ["Cable crossover machine", "Chest press machine", "Ab crunch machine",
                         "Pilates reformer machine", "Standard barbell", "Olympic barbell", "Fixed weight dumbbell",
                         "Adjustable dumbbell", "Standard weight plate", "Olympic weight plate", "Climbing rope",
                         "Kettlebell", "Exercise mat", "EZ curl bar", "Triceps bar", "Flat bench", "Adjustable bench"]}

# Later: integrate mySQL or Oracle database
# {username:[password, status, [sessions], Registered Gym, Membership]}
tempDatabase = {"Admin": ["admin123", "Admin", [], "GYM1", 1],
                "MahdiAlhakim": ["password123", "Client",
                                 [(0, 7, 9, "Upper Body"), (1, 8, 10, "Lower Body"), (2, 16, 17, "Cardio"),
                                  (3, 8, 10, "Upper Body"), (4, 7, 9, "Lower Body")], "GYM1", 1],
                "Bob": ["pass321", "Client",
                        [(0, 8, 10, "Full Body"), (2, 10, 12, "Full Body"), (5, 9, 13, "Full Body")], "GYM2", 0],
                "John": ["test55", "GYM", [], "GYM3", 0],
                "Moussa": ["test55", "GYM", [], "GYM2", 0],
                "Ali": ["test55", "Coach", [(0, 7, 11, "Supervision"), (3, 13, 16, "Supervision")], "GYM1", 0]}

# [Gym Capacity, (opens, closes), [client list], [time_exceptions], contact_info, {available machines/devices/exercises/..}, [schRequest], [callRequest]]
GymDatabase = {
    "GYM1": [25, [(7, 18) for i in range(7)], ["MahdiAlhakim"], [(6, 7, 18)], "XXXXX@XXX.XXX", GYMSET, [], []],
    "GYM2": [30, [(8, 14) for i in range(7)], ["Bob"], [(1, 10, 12)], "XXXXX@XXX.XXX", GYMSET, [], []],
    "GYM3": [20, [(10, 20) for i in range(7)], [], [], "XXXXX@XXX.XXX", GYMSET, [], []]}