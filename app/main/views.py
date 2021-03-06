from flask import render_template
from app.requests import get_articles, get_news
from . import main

# /sources
@main.route('/')
def home():
    return render_template('home.html')
 
@main.route('/sources')
def index():
    title = "Home|newsrun"
    all_news = get_news()
    general_news = get_news()
    tech_news = get_news()
    bis_news = get_news()
    ent_news = get_news()

    return render_template('index.html', title=title, all=all_news, general=general_news, technology=tech_news, business=bis_news, entertainment=ent_news,)

@main.route('/news/<int:id>')
def news():
    news = get_news(id)
    return render_template('index.html', news=news)

@main.route('/articles/<source_id>')
def about(source_id):
    articles = get_articles()
    return render_template('about.html',  articles = articles)
