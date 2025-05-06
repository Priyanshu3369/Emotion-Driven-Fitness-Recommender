from flask import Flask, render_template, request
import sys
import os

# Add the ../src folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from emotion_model import predict_emotion
from recommender import get_recommendations

app = Flask(__name__)

# Route for home page (where users input their feelings)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['user_input']
        
        # Predict emotion from user input
        predicted_emotion = predict_emotion(user_input)
        
        # Get fitness recommendations based on predicted emotion
        recommendations = get_recommendations(predicted_emotion)

        return render_template('index.html', 
                               user_input=user_input, 
                               emotion=predicted_emotion, 
                               recommendations=recommendations)
    
    return render_template('index.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)