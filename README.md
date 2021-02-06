# Meme generator

This is a multimedia application to dynamically generate memes, including an image with an overlaid quote.

![meme_exmaple](./tmp/meme_example.jpg)

## Requirements

### Python 3.9

```bash
$ python --version
Python 3.9.1

$ pip install requirements.txt
```

### pdftotext

[pdftotext](https://www.xpdfreader.com/pdftotext-man.html) CLI utility

### How to test
$ pytest -v --disable-warnings

## How to use

### CLI

```bash
$ python meme.py --help
optional arguments:
  -h, --help       show this help message and exit
  --body BODY      a quote body text
  --author AUTHOR  an author of quote
  --path PATH      a path of image directory
```

### Flask app

Flask provides a run command to run the application with a development server.
In development mode, this server provides an interactive debugger and will reload when code is changed.

```bash
$ export FLASK_APP=app
$ export FLASK_ENV=development
$ python flask run
```

## Modules

### Quote engine

The `quote_engine` module is responsible for ingesting many types of files that contain quotes.
The `Ingestor` class can read different kinds of file formats such as 'csv', 'docx', 'pdf', and 'txt'.

#### Quote format

Any quote have follow the format below.

> "This is quote body" - author

### Meme engine

The `meme_engine` module is responsible for manipulating and drawing text onto images.
The `MemeGenerator` class accepts the path of image and converts it to a meme image with a quote.

### CLI

`meme.py` provides a CLI tool.

### Flask app

`app.py` provides a Flask app.

## Notes

This is a class project from [the Intermediate Python Nanodegree Program](https://www.udacity.com/course/intermediate-python-nanodegree--nd303) on [Udacity](https://www.udacity.com/). Thanks to @grutt for his great lecture.
