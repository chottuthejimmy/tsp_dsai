import os
import requests
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image, Spacer
from reportlab.lib.units import inch

# Create the PDF document
pdf_path = 'xkcd_comics.pdf'
doc = SimpleDocTemplate(pdf_path, pagesize=letter)
elements = []

# Iterate through all the XKCD comic strips
for comic_num in range(1, 3):  # The latest XKCD comic strip as of August 2023 is #2546
    # Construct the URL for the comic
    comic_url = f'https://xkcd.com/{comic_num}/info.0.json'

    # Download the comic data
    response = requests.get(comic_url)
    comic_data = response.json()

    # Extract the relevant information
    comic_title = comic_data['safe_title']
    comic_img_url = comic_data['img']

    # Download the comic image
    comic_img_response = requests.get(comic_img_url)
    with open(f'comic_{comic_num}.png', 'wb') as f:
        f.write(comic_img_response.content)

    # Add the comic image to the PDF
    comic_img = Image(f'comic_{comic_num}.png', width=6*inch, height=4.5*inch)
    elements.append(comic_img)
    elements.append(Spacer(1, 0.5*inch))  # Add some space between comics

# Build the PDF
doc.build(elements)

# Clean up the downloaded comic images
for i in range(1, 2):
    os.remove(f'comic_{i}.png')

print('PDF book created successfully!')