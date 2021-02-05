import os
import re

from PIL import Image
import pytest

from meme_engine import MemeGenerator


def test_meme_generator():
    output_dir = 'OUTPUT_DIR'
    meme_gen = MemeGenerator(output_dir)
    assert isinstance(meme_gen, MemeGenerator)


def test_image_resize():
    img_path = './_data/photos/resize_test.jpg'
    output_dir = './tmp'
    meme_name = 'test_meme'

    meme_gen = MemeGenerator(output_dir)
    expected = f'{output_dir}/{meme_name}.jpg'
    try:
        assert meme_gen.make_meme(img_path, 'TEXT', 'AUTHOR',
                                  meme_file_name=meme_name) == expected
        with Image.open(expected) as im:
            assert im.size[0] == 500

        target_width = 600
        assert meme_gen.make_meme(img_path, 'TEXT', 'AUTHOR',
                                  width=target_width,
                                  meme_file_name=meme_name) == expected
        with Image.open(expected) as im:
            assert im.size[0] == target_width

    finally:
        os.remove(expected)


@pytest.mark.parametrize('ext', ['jpg', 'png', 'any_ext'])
def test_make_output_path(ext):
    output_dir = 'TEST_DIR'
    img_path = f'./TEST_DIR/TEST_IMAGE.{ext}'
    meme_gen = MemeGenerator(output_dir)

    actual = meme_gen._make_output_path(img_path, None)
    assert re.match(fr'TEST_DIR\/meme_[0-9]{{7}}\.{ext}', actual)

    meme_name = 'TEST_MEME_NAME'
    actual = meme_gen._make_output_path(img_path, meme_name)
    assert actual == f'TEST_DIR/TEST_MEME_NAME.{ext}'


def test_meme_generator_make_meme():
    output_dir = './tmp'
    img_path = './_data/photos/dog/xander_1.jpg'
    text = 'TEST_QUOTE_BODY'
    author = 'Tester'
    meme_name = 'TEST_MEME_NAME'

    meme_gen = MemeGenerator(output_dir)
    expected = f'{output_dir}/{meme_name}.jpg'

    try:
        actual = meme_gen.make_meme(img_path, text, author,
                                    meme_file_name=meme_name)
        assert actual == expected
        assert os.path.exists(expected)
    finally:
        os.remove(expected)
