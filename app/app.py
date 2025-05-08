from flask import Flask, render_template, request
import sys
import os

# Add the ../src folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from emotion_model import predict_emotion
from recommender import get_recommendations

app = Flask(__name__)

# Route for home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['user_input']
        
        if not user_input.strip():
            return render_template(
                'index.html',
                user_input=user_input,
                emotion=None,
                message="⚠️ Please enter some text.",
                recommendations=None
            )
        
        try:
            # Predict emotion from user input
            predicted_emotion = predict_emotion(user_input)

            # Check if emotion is in supported list
            valid_emotions = ['joy', 'sadness', 'anger', 'fear', 'love', 'surprise']
            if predicted_emotion not in valid_emotions:
                return render_template(
                    'index.html',
                    user_input=user_input,
                    emotion=predicted_emotion,
                    message="😕 Sorry, we couldn't understand the emotion.",
                    recommendations=None
                )

            # Get motivational message and video recommendations
            motivational_message, recommendation_list = get_recommendations(predicted_emotion)

            if not recommendation_list:
                return render_template(
                    'index.html',
                    user_input=user_input,
                    emotion=predicted_emotion,
                    message=f"🙂 Detected emotion: {predicted_emotion}, but no activities found.",
                    recommendations=None
                )

            return render_template(
                'index.html',
                user_input=user_input,
                emotion=predicted_emotion,
                message=motivational_message,
                recommendations=recommendation_list
            )
        
        except Exception as e:
            print(f"[ERROR] {e}")
            return render_template(
                'index.html',
                user_input=user_input,
                emotion=None,
                message="❌ Oops! Something went wrong while predicting emotion.",
                recommendations=None
            )

    # For GET request, just render the form with no content
    return render_template(
        'index.html',
        user_input=None,
        emotion=None,
        message=None,
        recommendations=None
    )

if __name__ == '__main__':
    app.run(debug=True)
