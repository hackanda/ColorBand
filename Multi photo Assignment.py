import PIL
from PIL import Image , ImageDraw , ImageFont
from PIL import ImageEnhance

image=Image.open("MyImage.jpg")
image=image.convert('RGB')

def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image

def get_pixel(image, i, j):
    width, height = image.size
    if i > width or j > height:
      return None

    pixel = image.getpixel((i, j))
    return pixel

def changepixel(image , m):
    width,height = image.size
    new = create_image(width,height)
    pixels = new.load()
    for x in range(width):
        for y in range(height):
            pixel = get_pixel(image, x, y)
            red =   pixel[0]
            green = pixel[1]
            blue =  pixel[2]
            if m in [1,4,7]:
                if m == 1:
                    red = red/10
                if m == 4:
                    green = green/10
                if m == 7 :
                    blue = blue/10
            elif m in [2,5,8]:
                if m == 2:
                    red = red/2
                if m == 5:
                    green = green/2
                if m == 8:
                    blue = blue/2
            else:
                if m == 3:
                    red = (red*9)/10
                if m == 6:
                    green = (green*9)/10
                if m == 9:
                    blue = (blue*9)/10
            pixels[x,y] = (int(red),int(green),int(blue))
    return new          


def Text_on_image(image,m):
    width , height = image.size
    new = Image.new("RGB", (width,height+75), "black")
    new.load()
    text = Image.new("RGB", (width,75), "black")
    text.load()
    d = ImageDraw.Draw(text)
    fnt = ImageFont.truetype('/home/rishu/Downloads/Amatic-Bold.ttf', 80)
    if m in [1,4,7]:
        intensity = 0.1
    if m in [2,5,8]:
        intensity = 0.5
    if m in [3,6,9]:
        intensity = 0.9
    if m in [1,2,3]:
        d.text((0,0), f'channel 0 intensity {intensity}',font = fnt , fill=(255,255,255))
    if m in [4,5,6]:
        d.text((0,0), f'channel 1 intensity {intensity}',font = fnt , fill=(255,255,255))
    if m in [7,8,9]:
        d.text((0,0), f'channel 2 intensity {intensity}',font = fnt , fill=(255,255,255))
    new.paste(image,(0,0))
    new.paste(text,(0,height))
    return new


images=[]
for i in range(1, 10):
    images.append(Text_on_image(image , i))

for i in range(1,10):
    images[i-1] = changepixel(images[i-1] , i)

first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    contact_sheet.paste(img, (x, y) )

    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
contact_sheet.save('ScriptEdited.jpg')
contact_sheet.show()
