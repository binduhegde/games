from PIL import Image

#RESISES THE IMGAES PUT IN 

desired_dimension_x = 1200
desired_dimension_y = 700

# returns the file name without the extention
# calling this while saving an image
# without this, file name will be "image.jpeg_resized.png"
# with this, file name will be "image_resized.png"
def file_name(name):
    for i in range(len(name)):
        if name[i] == '.':
            return name[:i]
    return name

def image_resize(name):
    image = Image.open(name)
    new_image = image.resize((desired_dimension_x, desired_dimension_y))
    new_image.save(f'{file_name(name)}_resized.png')

image_resize('images/blank_image.jpg')