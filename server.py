from flask import Flask, render_template
from post import get_posts

post_objects = get_posts()

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
