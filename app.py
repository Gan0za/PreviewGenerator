from PIL import Image, ImageDraw, ImageFont

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

template = Image.new("RGB", (1120, 480), color=('#ffffff'))
logo = Image.open("./template/logo.png")
gitLogo = Image.open("./template/gitLogo.png")
projectLogo = Image.open("./template/projectLogo.png")

logo = logo.resize((200, 200))
logo = add_corners(logo, 30)
gitLogo = gitLogo.resize((85, 85))
projectLogo = projectLogo.resize((190, 190))

draw_text = ImageDraw.Draw(template)
draw_text.text(
    (30, 30),
    'Gan0za/PreviewGenerator',
    font = ImageFont.truetype('./font/OpenSans.ttf', size=62),
    fill = '#26263e')

draw_text.text(
    (50, 110),
    'Генератор превью для проектов',
    font = ImageFont.truetype('./font/OpenSans.ttf', size=25),
    fill = '#26263e')

template.paste(logo, (890, 30), logo)
template.paste(gitLogo, (1006, 365), gitLogo)
template.paste(projectLogo, (60, 190), projectLogo)

template.save("result.png")