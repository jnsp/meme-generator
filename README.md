# Meme generator

This is a multimedia application to dynamically generate memes, including an image with an overlaid quote.

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

## Modules

### Quote engine

The `quote_engine` module is responsible for ingesting many types of files that contain quotes.
The `Ingestor` class can read different kinds of file formats such as 'csv', 'docx', 'pdf', and 'txt'.

#### Quote format

Any quote have follow the format below.

> "This is quote body" - author

### Meme engine

The `meme_engine` module is responsible for manipulating and drawing text onto images.
The `MemeGenerator` class accepts the path of image and converts meme image with a quote.

## Notes

This is a class project from [the Intermediate Python Nanodegree Program](https://www.udacity.com/course/intermediate-python-nanodegree--nd303) on [Udacity](https://www.udacity.com/).
