from flask import Flask
app = Flask(__name__)

@app.route('/user/<user>/')
def showVariable(user):
    return 'User %s' %user

@app.route('/user/<int:num>')
def showNum(num):
    return 'User {}'.format(num)

if __name__ == '__main__':
    app.run(debug=True)