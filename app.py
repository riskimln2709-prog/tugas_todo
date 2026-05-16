from flask import Flask, render_template, request, redirect
from service import TaskService

app = Flask(__name__)

task_service = TaskService()

@app.route("/")
def index():
    tasks = task_service.get_all()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("task")
    date  = request.form.get("date")

    if title and date:
        task_service.add_task(title, date)

    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    task_service.delete_task(index)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
