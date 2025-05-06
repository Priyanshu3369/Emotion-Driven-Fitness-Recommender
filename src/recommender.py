# Sweet motivational messages for each emotion
sweet_messages = {
    'joy': "You're radiating joy! Let's dance it out and keep the good vibes flowing!",
    'sadness': "It's okay to feel down. Let's uplift your spirit with something soothing.",
    'anger': "Take a deep breath — let's channel that energy into something powerful.",
    'fear': "You're safe and strong. Gentle movements will help ease your mind.",
    'love': "You're surrounded by love. Let's embrace it with mindful exercises.",
    'surprise': "Something unexpected? Let’s turn that surprise into an adventure!"
}

# Fitness activities and YouTube video links for each emotion
emotion_fitness_map = {
    'joy': [
        {"activity": "Dance Workout", "video": "https://www.youtube.com/watch?v=Qj7D4bcgYk8"},
        {"activity": "Outdoor Running", "video": "https://www.youtube.com/watch?v=9p1RcAi4xDk"},
        {"activity": "Zumba", "video": "https://www.youtube.com/watch?v=FHo9QaJ1DyI"}
    ],
    'sadness': [
        {"activity": "Yoga", "video": "https://www.youtube.com/watch?v=v7AYKMP6rOE"},
        {"activity": "Walk in Nature", "video": "https://www.youtube.com/watch?v=2pLT-olgUJs"},
        {"activity": "Stretching", "video": "https://www.youtube.com/watch?v=eZ5v2ZwCnhE"}
    ],
    'anger': [
        {"activity": "Boxing", "video": "https://www.youtube.com/watch?v=b8DZhxz0YpY"},
        {"activity": "HIIT Workout", "video": "https://www.youtube.com/watch?v=ml6cT4AZdqI"},
        {"activity": "Kickboxing", "video": "https://www.youtube.com/watch?v=2vjgN2gC5L4"}
    ],
    'fear': [
        {"activity": "Breathing Exercises", "video": "https://www.youtube.com/watch?v=nmFUDkj1Aq0"},
        {"activity": "Meditation", "video": "https://www.youtube.com/watch?v=inpok4MKVLM"},
        {"activity": "Light Yoga", "video": "https://www.youtube.com/watch?v=4pLUleLdwY4"}
    ],
    'love': [
        {"activity": "Couple Yoga", "video": "https://www.youtube.com/watch?v=cDfYrh60fBo"},
        {"activity": "Partner Dance", "video": "https://www.youtube.com/watch?v=0M_ZCbnZxaY"},
        {"activity": "Pilates", "video": "https://www.youtube.com/watch?v=lCg_gh_fppI"}
    ],
    'surprise': [
        {"activity": "Fun Cardio", "video": "https://www.youtube.com/watch?v=mn5RkDGFZnM"},
        {"activity": "Adventure Sports Suggestions", "video": "https://www.youtube.com/watch?v=AkNjF1QxzM4"}
    ]
}

# Function to get message and video recommendations
def get_recommendations(emotion):
    message = sweet_messages.get(emotion, "Let's move and feel better!")
    videos = emotion_fitness_map.get(emotion, [])
    return message, videos
