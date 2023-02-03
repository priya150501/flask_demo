from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!!'

# @app.route('/priya')
# def priya():
#     return "Priya Chaudhary!!"

# @app.route('/roohi')
# def roohi():
#     return "Reshma Roohi!!"

app.run(host='0.0.0.0', port=81)