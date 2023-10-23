# -*- coding: utf-8 -*-
"""
@author: YASH
"""

from PIL import Image, ImageDraw, ImageFont

#Original image
original_image = Image.open("C:/2-dataset/IMG_20230212_231443.jpg")

#watermark image
watermark_image = Image.open("C:/2-dataset/output-onlinepngtools.png") #.convert("RGBA")

# Define the position to place the watermark (e.g., bottom-right)
watermark_position = (original_image.width - watermark_image.width, original_image.height - watermark_image.height)

# Add the watermark to the original image
original_image.paste(watermark_image, watermark_position, watermark_image)
# Save the watermarked image to a file
original_image.save("C:/2-dataset/output-onlinepngtools.png")

# Display the watermarked image on social media
# You can use libraries like tweepy or pytweet to post the image on Twitter, or similar libraries for other social media platforms.
# Please note that posting on social media usually involves additional authentication and authorization steps, which are not covered in this code.

# Optionally, you can also specify the opacity/transparency of the watermark:
# watermark_image = watermark_image.convert("RGBA")
# watermark_with_transparency = Image.new("RGBA", watermark_image.size)
# for x in range(watermark_image.width):
#     for y in range(watermark_image.height):
#         r, g, b, a = watermark_image.getpixel((x, y))
#         watermark_with_transparency.putpixel((x, y), (r, g, b, 100))  # Set the alpha value (transparency)

# Then, use watermark_with_transparency in the paste function.
