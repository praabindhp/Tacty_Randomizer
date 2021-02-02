import random
from flask import Flask, render_template, request

app=Flask(__name__)

cnl=[] # Capacity Number List
listOriginal=[] # initializing The 1st List
listRandom=[] # initializing The 2nd List

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=["POST"])
def get_value():
    n=request.form["count"]
    num=int(n)

    cnl=request.form["objects"]
    listOriginal=cnl.split()

    listRandom=random.sample(listOriginal, num)
    print(listRandom)
    return render_template('results.html', randomlist=listRandom, num=num)

@app.route('/results', methods=["POST"])
def results():
    render_template('results.html')

if __name__=='__main__':
    app.debug=True
    app.run()
    app.run(debug=True)