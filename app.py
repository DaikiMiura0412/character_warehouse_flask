from flask import Flask, render_template # 変更
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html') # 変更