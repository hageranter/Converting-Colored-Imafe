from PIL import Image

# Converting image
def convert_to_bw(image_path, output_path, threshold=128):
    with Image.open(image_path) as img:
        
        # Convert image to grayscale first  
        grayscale_img = img.convert('L')
        
        # Apply a binary threshold to the image, so i can detect what if every pixel will change to black or white
        # if the pixel's threshold smaller than the default threshold which is 128 it will change to 0 >(white) else will apply 1>>(black)
        
        bw_img = grayscale_img.point(lambda x: 255 if x > threshold else 0, mode='1')
        bw_img.save(output_path)

        
        # Count the number of black and white pixels in the BW image
        # Easily, if the pixel is 0 I will count it as a black one 
        # and iif it's a 255 >> count it as a white one 
        black_pixels = sum(1 for pixel in bw_img.getdata() if pixel == 0)  # Black pixel (0)
        white_pixels = sum(1 for pixel in bw_img.getdata() if pixel == 255)  # White pixel (255)

        # Count the number of colored pixels in the original image
        # Convert original image to RGB to ensure proper counting
        # Easily, if the pixel is 255. So, It colorful one>> I will count it.
        colored_pixels = sum(1 for pixel in img.convert('RGB').getdata() if pixel != (255, 255, 255) and pixel != (0, 0, 0))
        total_pixels = img.width * img.height

        print(f"Total pixels: {total_pixels}")
        print(f"Black pixels in BW image: {black_pixels}")
        print(f"White pixels in BW image: {white_pixels}")
        print(f"Colored pixels in original image: {colored_pixels}")
        
        return black_pixels, white_pixels, colored_pixels



input_image = input("Enter the path to the input image: ")  # Takes image path from user input

output_image = "output_bw_image.jpg" 
convert_to_bw(input_image, output_image)
# Firstly, I downlod python on my PC so I can code with this language
# Then, I have used some of python's libraries to deal with image like( open, save , read,etc)
# And with some commands line, so code runed
