# To-do App with Flask

$\textcolor{ForestGreen}{\textbf{\emph{Completed:}}} \text{\emph{ Sunday, Oct 30, 2022}}$

## Demo
To access the software, run the following commands:

```bash
python3 -m venv venv
. venv/bin/activate
pip install Flask
pip install Flask-SQLAlchemy
python app.py
```

## Code Source 
The code for this project is adapted from Patrick Loeber's [Python Flask Beginner Tutorial - Todo App](https://www.python-engineer.com/posts/flask-todo-app/) website, with a few additions as noted in the [Improvements section](#improvements) below.

## Features  
- Type a task in the text box and press the "Enter" key or the "Add item" button to register it to local storage. The task persists when the browser tab is refreshed or reopened later.
- When you have some tasks to work over, you can click on the "Mark as Complete" button next to each item to mark them as completed. 
- Click at the "Mark as Incomplete" button to undo.
- You can also delete tasks by clicking on the "Delete" button next to each item.

## Improvements  
1. Changed the way the Completed/Incomplete workflow works, and added new colored buttons to make it clearer what the effect of the action will be (green: will mark as complete; gray: will mark as incomplete).
1. Changed the language of the app to make it more intuitive.
1. Added comments to demonstrate comprehension.
