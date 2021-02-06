import random
import os

from flask import Flask, render_template, request
import requests

from meme_engine import MemeGenerator
from quote_engine import Ingestor

app = Flask(__name__)

meme = MemeGenerator('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = list()
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"
    imgs = [images_path + file for file in os.listdir(images_path)]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    image_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    r = requests.get(image_url)
    ext = image_url.split('.')[-1]
    img_path = f'./tmp/downloaded.{ext}'

    try:
        with open(img_path, 'wb') as f:
            f.write(r.content)
        path = meme.make_meme(img_path, body, author)
    finally:
        os.remove(img_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
