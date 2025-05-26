'''This function initiates the application of emotion detection.
   It is executed over the Flask channel and deployed on
   localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector', template_folder = 'templates')

@app.route('/emotionDetector')
def sent_analyzer():
    '''This function receives an input text from the HTML interface and 
        runs emotion detection over it using the emotion_detector() function. 
        The function return the emotion label and its score for the
        input text. 
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return 'Invalid text! Please try again!'

    return f'''For the given statement, the system response is {response}.
    The dominant emotion is {dominant_emotion}'''

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)
