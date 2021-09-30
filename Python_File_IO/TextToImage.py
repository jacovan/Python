from PIL import Image,ImageDraw
sample = Image.new('RGB',(220,30),color = 'black')
s = ImageDraw.Draw(sample)
s.text((10,10),"Hello World of bunnies and stuff",fill=('white'))
sample.save('sampleTextToImage.png')
