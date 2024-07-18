# select random line from text file
import random

def generate_content():
    #lines
    check_in = [
        "How did you sleep?? 🌜",
        "How was thy rest? 🙃"
        ]

    gt_sleep = [
        "Hope ya slept well ✨",
        "I hope you're feeling well ✨"
        ]
    

    gt_day = [
        "Have a great day my love 😘",
        "May your day be filled with wonders 😘"
        ]

    day_events = [
        "What are the plans for today? 🌚",
        "And what are we doing for the aujourd'hui? 🌝"
        ]

    content = random.choice(check_in) + random.choice(gt_sleep) + random.choice(gt_day) + random.choice(day_events)
    return content