from PIL import Image, ImageDraw, ImageFont

W, H = (2400, 1000)
img = Image.new('RGB', (W,H), color = (0, 0, 0))

draw = ImageDraw.Draw(img)

txt = "Chris" # text to be generated
fontsize = 1  # starting font size

# portion of image width you want text width to be
img_fraction = 0.70

font = ImageFont.truetype("arial.ttf", fontsize)
while font.getsize(txt)[0] < img_fraction*img.size[0]:
    # iterate until the text size is just larger than the criteria
    fontsize += 1
    font = ImageFont.truetype("arial.ttf", fontsize)

# optionally de-increment to be sure it is less than criteria
fontsize -= 1
font = ImageFont.truetype("arial.ttf", fontsize)

w, h = draw.textsize(txt, font=font)

# print ('final font size',fontsize)
# print ('dimensions', W, H, w, h )
draw.text(((W-w)/2,(H-h)/2), txt, font=font) # put the text on the image
img.save('chris.png') # save it
