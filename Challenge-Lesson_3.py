from PIL import Image, ImageDraw

# Create a new image with white background
width, height = 2000, 1000
image = Image.new("RGB", (width, height), "white")

# Create a draw object
draw = ImageDraw.Draw(image)

# Draw the flag
draw.rectangle([5, 5, 1995, 200], fill="blue")
draw.rectangle([5, 800, 1995, 995], fill="blue")
draw.line([1000,300,700,600], fill="blue", width=50)
draw.line([1000,265,1300,600], fill="blue", width=50)
draw.line([686,600,1315,600], fill="blue", width=50)
draw.line([1000,700,700,400], fill="blue", width=50)
draw.line([1000,731,1300,400], fill="blue", width=50)
draw.line([686,400,1315,400], fill="blue", width=50)

# Save the image
image.save("flag.png")