from flask import Flask,render_template,request
import pickle


app = Flask(__name__)
@app.route('/home')
def main():
    return render_template('home.html')

@app.route('/visualizations')
def visualizations():
    return render_template('visualizations.html')


@app.route('/predict',methods = ['POST','GET'])
def predict():
    inp = request.form.get("review")
    Sentiment = ''
    max_review_length = 500
    return render_template('home.html',message=inp)

if __name__ == '__main__':
    app.run()


