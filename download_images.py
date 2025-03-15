import os
import requests
from pathlib import Path

# Create media/products directory if it doesn't exist
MEDIA_ROOT = Path(__file__).resolve().parent / 'media' / 'products'
MEDIA_ROOT.mkdir(parents=True, exist_ok=True)

# Sample image URLs (replace with actual product images)
images = {
    'phone.jpg': 'https://ares.shiftdelete.net/2023/08/iphone-1.webp',
    'laptop.jpg': 'https://picsum.photos/400/400?random=2',
    'jeans.jpg': 'https://picsum.photos/400/400?random=3',
    'tshirt.jpg': 'https://picsum.photos/400/400?random=4',
    'python-book.jpg': 'https://picsum.photos/400/400?random=5',
    'coffee-maker.jpg': 'https://picsum.photos/400/400?random=6',
    'yoga-mat.jpg': 'https://picsum.photos/400/400?random=7',
    'face-cream.jpg': 'https://picsum.photos/400/400?random=8',
    'robot.jpg': 'https://picsum.photos/400/400?random=9',
    'necklace.jpg': 'https://picsum.photos/400/400?random=10'
}

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        file_path = MEDIA_ROOT / filename
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {filename}")

# Download all images
for filename, url in images.items():
    download_image(url, filename)