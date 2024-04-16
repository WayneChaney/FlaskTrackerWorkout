from flask import Flask, render_template, request, redirect, url_for, flash

import sqlite3
app = Flask(__name__)
app.route('/')
def home():
   return " ok wer online"

# Supporting functions
def db_create():
   with sqlite3.connect("overtime.db") as connection:
      cursor = connection.cursor()
      try:
         cursor.execute("CREATE TABLE overtime_list (id INTEGER PRIMARY KEY, Date TEXT, Start TEXT, End TEXT)")
      except Exception:
         pass
def ot_put(data):
  with sqlite3.connect("overtime.db") as connection:
      cursor = connection.cursor()
      cursor.execute("INSERT INTO overtime_list (Date, Start, End)VALUES(?, ?, ?)", data)
def ot_get():
  with sqlite3.connect("overtime.db") as connection:
      cursor = connection.cursor()
      ot_list = cursor.execute("SELECT * from overtime_list")
      return ot_list
def ot_remove(id):
  with sqlite3.connect("overtime.db") as connection:
    cursor = connection.cursor()
    try:
      cursor.execute("DELETE FROM overtime_list WHERE id = ?", (id,))
    except Exception:
      pass

    # Routes
@app.route("/", methods=["GET", "POST"])
def index():
    data = []
    if request.method == "POST":
        date = request.form.get("date")
        start = request.form.get("start")
        end = request.form.get("end")
        for i in (date, start, end):
            data.append(i)
        ot_put(data)
        flash("Record added", "success")
        return redirect(url_for("index"))
    ot_list = ot_get()
    return render_template("index.html",
                           data=data,
                           ot_list=ot_list)

@app.route("/delete", methods=["POST"])
def db_delete():
    if request.method == "POST":
        id = request.form["id"]
        ot_remove(id)
        flash("Record removed", "danger")
        return redirect(url_for("index"))
    
if __name__ == "__main__":
    app.run(debug=True)
