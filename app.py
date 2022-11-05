from flask import Flask, render_template, request, redirect, url_for, abort

from db import get_db_cursor, get_db

app = Flask(__name__)


@app.route("/")
def index():
    cur = get_db_cursor()
    cur.execute("select * from post order by id desc")
    posts = cur.fetchall()

    return render_template("index.html", posts=posts)


@app.route("/posts/<int:post_id>")
def post_show(post_id):
    cur = get_db_cursor()
    cur.execute("select * from post where id = ?", (post_id,))
    post = cur.fetchone()

    if post is None:
        return abort(404)

    return render_template("post_show.html", post=post)


@app.route("/new")
def post_create_get():
    return render_template("post_create.html")


@app.route("/new", methods=["POST"])
def post_create_post():
    title = request.form["title"]
    contents = request.form["contents"]

    db, cur = get_db()
    cur.execute("insert into post(title, contents) values (?, ?)", (title, contents))
    db.commit()

    return redirect(url_for("index"))


app.run(debug=True)
