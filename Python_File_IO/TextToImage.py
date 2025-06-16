from PIL import Image,ImageDraw, ImageFont
sample = Image.new('RGB',(600,50),color = 'black')
draw = ImageDraw.Draw(sample)
s = ImageDraw.Draw(sample)
text = "Hello World of bunnies and stuff"
font = ImageFont.truetype("arial.ttf", 30)
text_width, text_height = draw.textsize(text, font=font)
position = ((sample.width - text_width) // 2, (sample.height - text_height) // 2)
draw.text(position, text, fill= "white", font=font)
sample.save('sampleTextToImage.png')
