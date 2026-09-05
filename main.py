from flask import Flask
app = Flask(__name__)
@app.get('/')
def Palop():
    return  "你好，我是palop"