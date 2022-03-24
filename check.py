from flask import Flask, render_template
check = Flask(__name__)

@check.route('/')
def table():
    return render_template('index.html')

if __name__=="__main__":
    check.run(debug =True)