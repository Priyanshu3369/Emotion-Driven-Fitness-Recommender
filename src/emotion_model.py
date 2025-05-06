import pickle

# Load model and vectorizer
with open('../models/emotion_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('../models/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

def predict_emotion(text):
    X = vectorizer.transform([text])
    prediction = model.predict(X)
    return prediction[0]