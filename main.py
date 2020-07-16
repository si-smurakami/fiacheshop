from flask import Flask
from flask import Response
from flask import request
from flask import abort

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'FiachShop Top Page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'user1' and password == 'pass':
            return '''
            <ul>
             <li>What is Fiache.Shop? 1000Yen</li>
             <li>Scrum Story 500Yen</li>
             <li>How to use Jira 700Yen</li>
            </ul>
             '''
        else:
            return abort(401)
    else:
        return Response('''
            <form action="" method="post">
                <p>Username: <input type=text name=username></p>
                <p>Password: <input type=password name=password></p>
                <p><input type=submit></p>
            </form>
        ''')


if __name__ == '__main__':
    app.run()