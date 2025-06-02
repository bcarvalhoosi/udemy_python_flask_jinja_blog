import requests

def get_posts():
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    post_objects = []
    for post in posts:
        post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
        post_objects.append(post_obj)
    return post_objects

class Post:
    def __init__(self, post_id, title, subtitle, body):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body

