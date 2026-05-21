import os
from PIL import Image

# Target your static images directory
# Adjust this path if your images are in static/services or static/images
TARGET_DIR = 'static'

def compress_to_webp(directory):
    # Walk through all folders and subfolders
    for root, _, files in os.walk(directory):
        for file in files:
            # Look for uncompressed or heavy formats
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                filepath = os.path.join(root, file)
                base_name = os.path.splitext(filepath)[0]
                new_filepath = f"{base_name}.webp"

                try:
                    with Image.open(filepath) as img:
                        # Save as WebP with 80% quality (excellent balance of size and visual fidelity)
                        img.save(new_filepath, 'webp', quality=80)

                    # Get file sizes to see the improvement
                    old_size = os.path.getsize(filepath) / 1024
                    new_size = os.path.getsize(new_filepath) / 1024
                    print(f"Compressed {file}: {old_size:.1f}KB -> {new_size:.1f}KB")

                    # Uncomment the next line if you want the script to automatically delete the old heavy images
                    # os.remove(filepath)

                except Exception as e:
                    print(f"Failed to compress {file}: {e}")

if __name__ == '__main__':
    print("Starting compression...")
    compress_to_webp(TARGET_DIR)
    print("Optimization complete!")