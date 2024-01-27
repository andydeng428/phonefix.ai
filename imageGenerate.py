# from PIL import Image
# from openai import OpenAI
# import sys
# import requests

# api_key = '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'
# client = OpenAI(api_key=api_key)

# original_image = sys.argv[0]

# def resize_and_fill_image(input_image_path, final_output_path, color):
#     desired_width = 512
#     desired_height = 1024
#     final_width = 1024
#     final_height = 1024

#     image = Image.open(input_image_path)

#     # Calculate the dimensions for the resized image
#     original_width, original_height = image.size
#     aspect_ratio = min(desired_width / original_width, desired_height / original_height)
#     new_width = int(original_width * aspect_ratio)
#     new_height = int(original_height * aspect_ratio)

#     # Resize the image without stretching
#     image = image.resize((new_width, new_height))

#     # Create a new image with the desired dimensions filled with transparency
#     new_image = Image.new("RGBA", (desired_width, desired_height), color)

#     # Calculate the position to paste the resized image
#     x_offset = (desired_width - new_width) // 2

#     # Paste the resized image onto the new image, with transparent areas at the top and bottom
#     new_image.paste(image, (x_offset, (desired_height - new_height) // 2))


#     # Create the final image with a size of 1024x1024 filled with transparency
#     final_image = Image.new("RGBA", (final_width, final_height), color)

#     # Calculate the position to paste the previous image onto the final image
#     x_final_offset = (final_width - desired_width) // 2

#     # Paste the previously created image onto the final image
#     final_image.paste(new_image, (x_final_offset, (final_height - desired_height) // 2))

#     # Save the final image
#     final_image.save(final_output_path)


# resize_and_fill_image(r"original_image.png", r"image.png", "BLACK")


# resize_and_fill_image(r"original_image.png", r"mask.png", (0,0,0,0))

# response = client.images.edit(
#   model="dall-e-2",
#   image=open("image.png", "rb"),
#   mask=open("mask.png", "rb"),
#   prompt="make this image into a 16 by 9 aspect ratio",
#   n=1,
#   size="1024x1024"
# )
# image_url = response.data[0].url

# im = Image.open(requests.get(image_url, stream=True).raw)
# im.save("output_image.png", "PNG")


# from PIL import Image

# def crop_and_resize_image(input_image_path, output_image_path):
#     # Open the image file
#     img = Image.open(input_image_path)
#     width, height = img.size

#     # Ensure the image is square
#     assert width == height, "Image must be square (1:1 aspect ratio)"

#     # Calculate dimensions for a 9:16 crop
#     new_height = height
#     new_width = int((9/16) * new_height)

#     # Calculate the area to crop
#     left = (width - new_width)/2
#     top = 0
#     right = (width + new_width)/2
#     bottom = height

#     # Crop the image
#     img_cropped = img.crop((left, top, right, bottom))

#     # Resize the image to the final dimensions
#     desired_width = 512
#     desired_height = 1024
#     img_resized = img_cropped.resize((desired_width, desired_height))

#     # Save the resized image
#     img_resized.save(output_image_path)

# crop_and_resize_image('output_image.png', 'finalfinal.png')









# import base64


# def image_to_data_url(image_path):
#     try:
#         with open(image_path, 'rb') as image_file:
#             # Read the image file in binary mode
#             image_binary = image_file.read()

#             # Encode the binary data using base64
#             image_base64 = base64.b64encode(image_binary).decode('utf-8')

#             # Create the data URL
#             data_url = f'data:image/png;base64,{image_base64}'

#             return data_url
#     except FileNotFoundError:
#         print(f"Error: File '{image_path}' not found.")
#         return None


# if __name__ == "__main__":
#     # Replace 'your_image.png' with the path to your PNG image file
#     image_path = 'finalfinal.png'
#     data_url = image_to_data_url(image_path)

#     if data_url:
#         # Print the clickable link directly to the console
#         clickable_link = f'<a href="{data_url}" target="_blank">Click here to view the image</a>'
#         print("Clickable Image Link:")
#         print(clickable_link)
