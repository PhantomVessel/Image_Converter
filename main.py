from PIL import Image

img = Image.open("Images/black.png")



img.save("your_icon.ico", format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])

print("✅ Converted to ICO successfully!")

