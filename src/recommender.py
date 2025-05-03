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

# ✅ Fixed function
def recommend_fitness(emotion):
    return emotion_fitness_map.get(emotion, [{"activity": "Walking", "video": "https://www.youtube.com/watch?v=I8RR-uP6D6k"}])

# ✅ Example usage
emotion = "anger"
recommendations = recommend_fitness(emotion)

for rec in recommendations:
    print(f"{rec['activity']}: {rec['video']}")
