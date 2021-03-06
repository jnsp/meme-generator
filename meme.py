import argparse
import os
import random

from meme_engine import MemeGenerator
from quote_engine import Ingestor, QuoteModel


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, _, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = [
            './_data/DogQuotes/DogQuotesTXT.txt',
            './_data/DogQuotes/DogQuotesDOCX.docx',
            './_data/DogQuotes/DogQuotesPDF.pdf',
            './_data/DogQuotes/DogQuotesCSV.csv'
        ]
        quotes = []
        for quote_file in quote_files:
            quotes.extend(Ingestor.parse(quote_file))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeGenerator('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Make a meme image.')
    parser.add_argument('--body', type=str, help='a quote body text')
    parser.add_argument('--author', type=str, help='an author of quote')
    parser.add_argument('--path', type=str, help='a path of image directory')

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
