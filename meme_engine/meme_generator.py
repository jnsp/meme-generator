from random import randint

from PIL import Image, ImageDraw, ImageFont


class MemeGenerator:
    def __init__(self, output_dir: str) -> None:
        self._output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        with Image.open(img_path) as im:
            img_widht, img_height = im.size
            height = int(width * img_height / img_widht)
            im = im.resize((width, height))

            draw = ImageDraw.Draw(im)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=30)
            position = (randint(5, width * 0.3), randint(5, height * 0.8))
            quote = f'{text}\n    - {author}'
            draw.text(position, quote, font=font, fill='black', stroke_width=2,
                      stroke_fill='white')

            im.save(self._output_dir)
        return self._output_dir
