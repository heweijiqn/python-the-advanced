from PIL import Image,ImageFont,ImageDraw
img=Image.open('bjsxt.png')
print(img.size)
draw_obj=ImageDraw.Draw(img)
font=ImageFont.load_default()
draw_obj.text((30,10),'bjsxt',font=font,fill='white')
font=ImageFont.truetype('SIMYOU.TTF',18)
draw_obj.text((30,30),'北京尚学堂',font=font,fill='red')
font=ImageFont.truetype('STXINGKA.TTF',30)
draw_obj.text((30,60),'北京尚学堂',font=font,fill='blue')
img.show()