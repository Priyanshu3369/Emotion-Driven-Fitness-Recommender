# Sweet motivational messages for each emotion
sweet_messages = {
    'joy': "You're radiating joy! Let's dance it out and keep the good vibes flowing!",
    'sadness': "It's okay to feel down. Let's uplift your spirit with something soothing.",
    'anger': "Take a deep breath — let's channel that energy into something powerful.",
    'fear': "You're safe and strong. Gentle movements will help ease your mind.",
    'love': "You're surrounded by love. Let's embrace it with mindful exercises.",
    'surprise': "Something unexpected? Let’s turn that surprise into an adventure!"
}

# Utility function to detect if a video is a Shorts link
def is_shorts_link(link):
    return "shorts" in link

# Fitness activities and YouTube video links for each emotion
emotion_fitness_map = {
    'joy': [
        {"activity": "Dance Workout", "video": "https://youtu.be/eM1E6FFnuZ8?si=nxfILuSWo3qWwGQ2"},
        {"activity": "Outdoor Running", "video": "https://youtu.be/kVnyY17VS9Y?si=ON-Drbs3qu-kElze"},
        {"activity": "Zumba", "video": "https://youtu.be/e5rW7qjd3BY?si=fin2GCD_K2ag1N-3"}
    ],
    'sadness': [
        {"activity": "Yoga", "video": "https://youtu.be/tA8E4l8Dj34?si=pETmdu9Dxvc1zRov"},
        {"activity": "Walk in Nature", "video": "https://youtu.be/ynLpZGegiJE?si=BCqG7Tn4JL3xlceb"},
        {"activity": "Stretching", "video": "https://youtu.be/L_xrDAtykMI?si=usYqYwBjmw4Dr_yT"}
    ],
    'anger': [
        {"activity": "Boxing", "video": "https://youtu.be/kKDHdsVN0b8?si=nN7l6y0Q4Vuems-u"},
        {"activity": "HIIT Workout", "video": "https://www.youtube.com/watch?v=ml6cT4AZdqI"},
        {"activity": "Kickboxing", "video": "https://youtu.be/sbNhd0JLQXA?si=H_SCpLq1wJrqtx5q"}
    ],
    'fear': [
        {"activity": "Breathing Exercises", "video": "https://youtu.be/lPJAtHWq08k?si=5sjJXGJePCwqvmPT"},
        {"activity": "Meditation", "video": "https://youtu.be/inpok4MKVLM?si=zW3-AEMvbs2EnnoM"},
        {"activity": "Light Yoga", "video": "https://youtu.be/C2RAjUEAoLI?si=IAme2u4vveekSEEX"}
    ],
    'love': [
        {"activity": "Couple Yoga", "video": "https://youtu.be/ptKO_Md_CWY?si=qJFhpiDwHfEAlnoF"},
        {"activity": "Partner Dance", "video": "https://youtu.be/Pafpi4OrMvA?si=Qy1EI32EA-NrobYM"},
        {"activity": "Pilates", "video": "https://youtu.be/tov0o3mi5h8?si=7GI_HzbCSl5XBi1o"}
    ],
    'surprise': [
        {"activity": "Fun Cardio", "video": "https://youtu.be/LphBXB0KfxU?si=rpGsN7LhnIxfCsa4"},
        {"activity": "Adventure Sports Suggestions", "video": "https://youtu.be/86L6vuhcN_c?si=yjixs70cY8s1nkc1"}
    ]
}

import re

# Function to extract YouTube video ID
def extract_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    return match.group(1) if match else ""

# Function to get message and video recommendations
def get_recommendations(emotion):
    message = sweet_messages.get(emotion, "Let's move and feel better!")
    raw_videos = emotion_fitness_map.get(emotion, [])
    videos = []

    for item in raw_videos:
        video_url = item['video']
        is_short = is_shorts_link(video_url)
        video_id = extract_video_id(video_url)

        videos.append({
            "activity": item['activity'],
            "video": video_url,
            "is_shorts": is_short,
            "video_id": video_id
        })

    return message, videos
