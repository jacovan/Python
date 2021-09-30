from PIL import Image
with Image.open ('sample.png') as sample:
    sample.save('sample2.png')