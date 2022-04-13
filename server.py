from flask import Flask, render_template, request, redirect

from users import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect ('/users')

@app.route('/users')
def read_all():
    users = User.get_all_users()
    return render_template('/users.html', users = users)

@app.route('/user/new')
def new_user():
    return render_template ('/create_user.html')

@app.route('/user/create', methods=['POST'])
def create():
    # print(request.form)
    User.create_user(request.form)
    return redirect ('/users')


if __name__ == "__main__":
    app.run(debug=True, port=5001)

