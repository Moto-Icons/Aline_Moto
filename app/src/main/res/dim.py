from PIL import Image
import os

# Directories
source_dir = "dummy"
output_dir = "drawable-nodpi"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Desired dimensions for the output canvas
canvas_size = 512  # Canvas size for adaptive icons
padding = 40  # Padding in pixels (space around the image)

# Function to add padding
def add_padding(image_path, output_path, canvas_size, padding):
    # Open the image
    img = Image.open(image_path).convert("RGBA")
    
    # Calculate the maximum dimensions for the image (canvas size minus padding on all sides)
    max_image_size = canvas_size - 2 * padding

    # Resize the image to fit within the maximum allowed dimensions
    img = img.resize(
        (
            min(img.width, max_image_size),
            min(img.height, max_image_size),
        ),
        Image.Resampling.LANCZOS
    )

    # Create a transparent canvas of the desired size
    canvas = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))

    # Calculate the position to paste the image centered with padding
    paste_x = (canvas_size - img.width) // 2
    paste_y = (canvas_size - img.height) // 2

    # Paste the resized image onto the transparent canvas
    canvas.paste(img, (paste_x, paste_y), img)

    # Save the resulting image
    canvas.save(output_path, "PNG")

# Process all PNG files in the source directory
for file_name in os.listdir(source_dir):
    if file_name.endswith(".png"):
        # Input and output paths
        input_path = os.path.join(source_dir, file_name)
        output_path = os.path.join(output_dir, file_name)

        # Add padding and save the new image
        add_padding(input_path, output_path, canvas_size, padding)
        print(f"Padded image saved: {output_path}")