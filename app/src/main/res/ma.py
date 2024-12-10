import os

# Directories
source_dir = "drawable-nodpi"
target_dir = "mipmap-anydpi"

# Ensure the target directory exists
os.makedirs(target_dir, exist_ok=True)

# Iterate over all PNG files in the source directory
for file_name in os.listdir(source_dir):
    if file_name.endswith(".png"):
        # Extract the image name without extension
        image_name = os.path.splitext(file_name)[0]

        # Define the XML content
        xml_content = f"""<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon
  xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/{image_name}" /> 
    <foreground android:drawable="@drawable/{image_name}" /> 
</adaptive-icon>
"""

        # Write the XML content to the target directory
        xml_file_path = os.path.join(target_dir, f"{image_name}.xml")
        with open(xml_file_path, "w", encoding="utf-8") as xml_file:
            xml_file.write(xml_content)

        print(f"Generated {xml_file_path}")
