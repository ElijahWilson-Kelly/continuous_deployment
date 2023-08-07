from main import session
import logging

def add_post(blog_post):
    old_posts = session.get("blog_posts", [])
    session["blog_posts"] = old_posts + [blog_post]

def generate_post_id():
    blog_posts = session.get("blog_posts", [])
    if (len(blog_posts) == 0):
        return 0

    return blog_posts[-1]["id"] + 1