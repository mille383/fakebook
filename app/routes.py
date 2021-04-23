from app import app
from flask import render_template
from app.models import Post


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')  # this is a flask route decorator. 'listens in' on a route being hit in the browser, then executes code beneath
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    p1 = Post(1, 'http://via,placeholder.com/1000/500', 'email1@email.com', 'Blog Post 1', 'body tesssssssssssssstttt')
    p2 = Post(2, 'http://via,placeholder.com/1000/500', 'email2@email.com', 'Blog Post 2', 'body tewfi2ifj2i4g24igj24i')
    p3 = Post(3, 'http://via,placeholder.com/1000/500', 'email3@email.com', 'Blog Post 3', 'bofh9u2hf9u42h924hg9284hg24')
    return render_template('blog.html', posts=[p1.to_dict(), p2.to_dict(), p3.to_dict()])

@app.route('/events')
def events():
    return render_template('events.html')