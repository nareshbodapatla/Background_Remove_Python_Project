#install modules 
from rembg import remove
from PIL import Image

#input  path of the image
input_path = "D:\\Python Bg Removal Project\\carimage.png"

#output path of the image
output_path = "carimage-removebg.png"


Input_image = Image.open(input_path)

#Removes the background
result = remove(Input_image)

# Output path for the isolated person
result.save(output_path)

