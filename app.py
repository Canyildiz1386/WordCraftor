from instagrapi import Client
from PIL import Image, ImageDraw, ImageFont
import os

def generate_image(output_path, text):
    width, height = 1080, 1920
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    
    # Customize the font
    font_path = "/path/to/your/font.ttf"  # Replace with a valid .ttf font path
    try:
        font = ImageFont.truetype(font_path, 100)
    except IOError:
        font = ImageFont.load_default()

    text_width, text_height = draw.textsize(text, font=font)
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    draw.text((text_x, text_y), text, fill="black", font=font)

    image.save(output_path)

def upload_story(username, password, image_path):
    client = Client()
    client.login(username, password)
    client.photo_upload_to_story(image_path, "Check out my story!")
    client.logout()

if __name__ == "__main__":
    # Set your Instagram credentials
    username = "Canyildiz1386"
    password = "Rahyab1357"

    # Generate image with custom text
    output_image_path = "story_image.jpg"
    dynamic_text = "Hello, this is my dynamic story!"  # Replace with your script result
    generate_image(output_image_path, dynamic_text)

    # Upload the generated image as a story
    upload_story(username, password, output_image_path)

    # Clean up
    if os.path.exists(output_image_path):
        os.remove(output_image_path)
