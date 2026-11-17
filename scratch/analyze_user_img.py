from PIL import Image

im = Image.open(r'C:/Users/jason/.gemini/antigravity/brain/57113af5-d036-4ac2-b466-04469390b932/.user_uploaded/media_1794893836000_e50e838f.png')
print('Size:', im.size)

# Find rows that have non-white pixels below the pagination
w, h = im.size
for y in range(0, h, 20):
    row_colors = [im.getpixel((x, y))[:3] for x in range(0, w, 50)]
    non_white = [c for c in row_colors if c != (255, 255, 255)]
    if non_white:
        print(f'y={y}: non-white sample:', non_white[0])
    else:
        print(f'y={y}: all white')
