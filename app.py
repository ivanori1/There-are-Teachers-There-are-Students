from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html')


@app.route('/teacher')
def teacher_page():
    return render_template('teacher.html')


@app.route('/student')
def student_page():
    return render_template('student.html')

if __name__ == '__main__':
    app.run()