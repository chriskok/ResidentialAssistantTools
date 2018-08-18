from PIL import Image, ImageDraw, ImageFont

nameArray = ['Kelly','Maria']

count = 1
for x in nameArray:
    bottomspace = 200
    W, H = (2500, 1000 + bottomspace)
    img = Image.new('RGB', (W,H), color = (0, 0, 0))

    draw = ImageDraw.Draw(img)

    txt = x # text to be generated
    if (len(x) == 3) or (len(x) == 4):
        txt = ' ' + x + ' '
    fontsize = 1  # starting font size

    # portion of image width you want text width to be
    img_fraction = 0.60

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
    draw.text(((W-w)/2,(H-h-bottomspace)/2), txt, font=font) # put the text on the image
    img.save('names/' + str(count) + '.png') # save it
    count = count + 1
