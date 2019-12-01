# from PIL import Image

# def crop(image_path, coords, saved_location):
#     """
#     @param image_path: The path to the image to edit
#     @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
#     @param saved_location: Path to save the cropped image
#     """

#     image_path = "C:\\Users\\solom\\Desktop\\python_crop_images\\computer.jpg"
#     saved_location = "C:\\Users\\solom\\Desktop\\python_crop_images\\cropped_images"
#     image_obj = Image.open(image_path)
#     cropped_image = image_obj.crop(coords)
#     cropped_image.save(saved_location)
#     cropped_image.show()
 
 
# if __name__ == '__main__':
#     image = 'computer.jpg'
#     crop(image, (161, 166, 706, 1050), 'cropped.jpg')

# Improting Image class from PIL module 
from PIL import Image 
  
# Opens a image in RGB mode 
im = Image.open("C:\\Users\\solom\\Desktop\\python_crop_images\\computer.jpg") 
  
# Size of the image in pixels (size of orginal image) 
# (This is not mandatory) 
width, height = im.size 
  
# Setting the points for cropped image 
left = 155
top = 150
right = 360
bottom = 300
  
# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 
  
# Shows the image in image viewer 
im1.show() 