from flask import Flask
from matplotlib import projections

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "Starting ML project"

if __name__=="__main__":
    app.run(debug=True)


