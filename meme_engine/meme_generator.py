from random import randint

from PIL import Image, ImageDraw, ImageFont


class MemeGenerator:
    def __init__(self, output_dir: str) -> None:
        self._output_dir = output_dir

    def make_meme(self, img_path: str, text: str, author: str,
                  width: int = 500, meme_file_name: str = None) -> str:
        with Image.open(img_path) as im:
            img_widht, img_height = im.size
            height = int(width * img_height / img_widht)
            im = im.resize((width, height))

            draw = ImageDraw.Draw(im)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=30)
            position = (randint(5, int(width * 0.3)),
                        randint(5, int(height * 0.8)))
            quote = f'{text}\n    - {author}'
            draw.text(position, quote, font=font, fill='black', stroke_width=2,
                      stroke_fill='white')

            output_path = self._make_output_path(img_path, meme_file_name)
            im.save(output_path)

        return output_path

    def _make_output_path(self, img_path, meme_file_name):
        if meme_file_name is None:
            num = 1000000
            random_name = str(randint(0, num)).zfill(len(str(num)))
            meme_file_name = f'meme_{random_name}'

        ext = img_path.split('.')[-1]
        return f'{self._output_dir}/{meme_file_name}.{ext}'
