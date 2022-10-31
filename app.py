from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Our model needs three entries: An id, a title, and a flag if the task 
# is completed or not. We also call db.create_all()before running our app.
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# For each url/route we want, we have to create a function and decorate it with 
# @app.route('path/to/your/url'). In this case we only use a forward slash 
# because this is going to be our start page.
@app.route('/')
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))
    
if __name__ == "__main__":
   # Note that we set debug=True so we don't have to reload our server 
   # each time we make a change in our code.
    with app.app_context():
        db.create_all()
    app.run(debug=True)
