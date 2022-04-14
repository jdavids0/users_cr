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

@app.route('/users/new')
def new_user():
    return render_template ('/create_user.html')

# need to figure out how to redirect create new user to show
@app.route('/users/create', methods=['POST'])
def create():
    # print(request.form)
    User.create_user(request.form)
    return redirect ('/users')

@app.route('/users/show/<int:id>')
def show_user(id):
    data = {
        "id": id
    }
    user = User.one_user(data)
    return render_template ('show_user.html', user = user)

@app.route('/users/edit/<int:id>', methods=['GET'])
def edit_user(id):
    data = {
        "id":id
    }
    user = User.one_user(data)
    return render_template('edit_user.html', user = user)

@app.route('/users/update', methods=['POST'])
def update_user():
    User.update(request.form)
    return redirect ('/users')

@app.route('/users/destroy/<int:id>')
def destroy (id):
    data = {
        "id": id
    }
    User.destroy(data)
    return redirect ('/users')    



if __name__ == "__main__":
    app.run(debug=True, port=5001)

