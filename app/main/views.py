from flask import Blueprint,render_template

main = Blueprint('main',__name__)

@main.route('/index/',methods=['POST','GET'])
def index():
    return render_template('index.html')

@main.route('/submit',methods = ['POST','GET'])
def submit():
    return render_template('result.html')
