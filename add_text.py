import io
import time
import requests
from PIL import Image, ImageDraw, ImageFont
from flask import Flask, request, send_file

app = Flask(__name__)


def text_wrap(text, font, max_width, lines):
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        words = text.split(' ')
        i = 0
        while i < len(words):
            line = ''
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width :
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            lines.append(line)
    return


@app.route("/AddText")
def AddText():
    if request.args.__contains__("url"):
        url = request.args['url']
        title = request.args['title']
        if request.args.__contains__(("subtitle")):
            subtitle = request.args['subtitle']
        else:
            subtitle = None
        start = time.time()
        response = requests.get(url)
        end = time.time()
        print("Time for getting response is: {}".format(end - start))
        image = Image.open(io.BytesIO(response.content))
        x1 = time.time()
        print("Time in opening image is: {}".format(x1 - end))
        if image.mode != 'RGBA':
            image = image.convert('RGBA')
        x2 = time.time()
        print("Time in converting to RGBA is: {}".format(x2 - x1))
        width, height = image.size
        gradient = 2.
        initial_opacity = 1.
        gradient_position = "bottom"
        alpha_gradient = Image.new('L', (1, height), color=0xFF)
        for x in range(height):
            if gradient_position == "bottom":
                gradient_coordinate = height - x - 1
            else:
                gradient_coordinate = x
            a = int(((initial_opacity * 255.) / 1.8) * (1. - gradient * float(x) / height))
            if a > 0:
                alpha_gradient.putpixel((0, gradient_coordinate), a)
            else:
                alpha_gradient.putpixel((0, gradient_coordinate), 0)
        alpha = alpha_gradient.resize(image.size)
        black_im = Image.new('RGBA', (width, height), color=0)  # i.e. black
        black_im.putalpha(alpha)
        x3 = time.time()
        print("Time in creating a gradient image is: {}".format(x3 - x2))
        image = Image.alpha_composite(image, black_im)
        x4 = time.time()
        print("Time in composite two images is: {}".format(x4 - x3))
        x, y = image.size
        image_editable = ImageDraw.Draw(image)
        title_font_size = int(y / 30)
        subtitle_font_size = int(y / 40)
        title_font = ImageFont.truetype("Poppins-Regular.ttf", title_font_size)
        subtitle_font = ImageFont.truetype("Poppins-Regular.ttf", subtitle_font_size)
        count = 0
        length = 1
        title_lines = []
        text_wrap(title, title_font, x - x / 20, title_lines)
        title = title_lines[0]
        if len(title_lines) > 1:
            title = title[:-3]
            title += "..."
        if subtitle is not None:
            text_lines = subtitle.split('/')
            lines = []
            for text in text_lines:
                text_wrap(text, subtitle_font, x - x / 20, lines)
            length = len(lines)
            for text in lines:
                image_editable.text((x / 30, y - y / 15 + (count - length + 1) * subtitle_font_size * 1.1), text,
                                    (255, 255, 255), font=subtitle_font)
                count += 1
            count = -1
        image_editable.text((x / 30, y - y / 15 + (count - length + 1) * subtitle_font_size - subtitle_font_size),
                            title, (255, 255, 255), font=title_font)
        x5 = time.time()
        print("Time in adding text is: {}".format(x5 - x4))
        image = image.convert('RGB')
        x6 = time.time()
        print("Time in converting to RGB is: {}".format(x6 - x5))
        textadded_images_bytes = io.BytesIO()
        image.save(textadded_images_bytes, format='jpeg')
        textadded_images_bytes.seek(0)
        x7 = time.time()
        print("Time in saving as bytes is: {}".format(x7 - x6))
        print("Total time is: {}".format(x7 - start))

        return send_file(textadded_images_bytes, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=True)
