import os

from PIL import Image

from meme_engine import MemeGenerator


def test_meme_generator():
    output_dir = 'OUTPUT_DIR'
    meme_gen = MemeGenerator(output_dir)
    assert isinstance(meme_gen, MemeGenerator)


def test_image_resize():
    img_path = './_data/photos/resize_test.jpg'
    output_dir = './_data/photos/resized.jpg'
    meme_gen = MemeGenerator(output_dir)

    try:
        assert meme_gen.make_meme(img_path, 'TEXT', 'AUTHOR') == output_dir
        with Image.open(output_dir) as im:
            assert im.size[0] == 500

        target_width = 600
        assert meme_gen.make_meme(img_path, 'TEXT', 'AUTHOR',
                                  target_width) == output_dir
        with Image.open(output_dir) as im:
            assert im.size[0] == target_width

    finally:
        os.remove(output_dir)


def test_meme_generator_make_meme():
    output_dir = './_data/photos/dog/example_output.jpg'
    img_path = './_data/photos/dog/xander_1.jpg'
    text = 'TEST_QUATE_BODY'
    author = 'Tester'
    meme_gen = MemeGenerator(output_dir)

    try:
        assert meme_gen.make_meme(img_path, text, author) == output_dir
        assert os.path.exists(output_dir)
    finally:
        os.remove(output_dir)
