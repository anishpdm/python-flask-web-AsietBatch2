from flask import Flask,render_template
from data import Faculties 

app=Flask(__name__)

myFaculties=Faculties()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/faculty')
def faculty():
    return render_template('faculty.html',facultyList=myFaculties)


if(__name__=='__main__'):
    app.run(debug=True)