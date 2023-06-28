from PIL import Image

#ovo je za promjenu gdje se terminal otvara
import os

#os.chdir("m3/datoteke/pillow/")
#NIJE RELEVANTNO ZA PREDAVANJE

fotografija_putanja = r"slika.jpg"
#fotografija_putanja = r"slika2.jpg"
fotografije_varijabla = Image.open(fotografija_putanja)

red = Image.open(r"red.jpg")
yellow = Image.open(r"yellow.jpg")
blue = Image.open(r"blue.jpg")
p10 = Image.open(r"10p.jpg")
p25 = Image.open(r"25p.jpg")
odabrano = Image.open(r"odabrano.jpg")

red_resize_vertical=int(round(fotografije_varijabla.size[0]*0.05,0))
red_vert = red.resize((fotografije_varijabla.size[0] - (red_resize_vertical * 2),10))

red_resize_horizontal=int(round(fotografije_varijabla.size[1]*0.05,0))
red_hor = red.resize((10, fotografije_varijabla.size[1] - (red_resize_horizontal * 2)))

yellow_resize_vertical=int(round(fotografije_varijabla.size[0]*0.125,0))
yellow_vert = yellow.resize((fotografije_varijabla.size[0] - (yellow_resize_vertical * 2),10))

yellow_resize_horizontal=int(round(fotografije_varijabla.size[1]*0.125,0))
yellow_hor = yellow.resize((10, fotografije_varijabla.size[1] - (yellow_resize_horizontal * 2)))

odabir=int(50)
#odabir=int(input('Unesite željeni postotak za micanje ruba slike (cijeli broj bez %): '))
odabir_step= odabir/200

blue_resize_vertical=int(round(fotografije_varijabla.size[0]*odabir_step,0))
blue_vert = blue.resize((fotografije_varijabla.size[0] - (blue_resize_vertical * 2),10))

blue_resize_horizontal=int(round(fotografije_varijabla.size[1]*odabir_step,0))
blue_hor = blue.resize((10, fotografije_varijabla.size[1] - (blue_resize_horizontal * 2)))


#print(odabir_step)

#fotografije_varijabla_converted = fotografije_varijabla.convert('RGBA')

#print(f"mod slike orig: {fotografije_varijabla.mode}")
#print(f"mod slike conv: {fotografije_varijabla_converted.mode}")
#print(f"mod slike preko: {red.mode}")

print(red_resize_vertical)
print(red.size)
print(red_vert.size)
print(fotografije_varijabla.size[0])

#blended = Image.blend(fotografije_varijabla_converted, fotografija_preko, alpha=0.5)
#blended.show()

fotografije_varijabla.paste(red_vert,(red_resize_vertical,red_resize_horizontal))
fotografije_varijabla.paste(red_hor,(red_resize_vertical,red_resize_horizontal))
fotografije_varijabla.paste(red_vert,(red_resize_vertical,fotografije_varijabla.size[1] - red_resize_horizontal - 10))
fotografije_varijabla.paste(red_hor,(fotografije_varijabla.size[0] - red_resize_vertical,red_resize_horizontal))
fotografije_varijabla.paste(p10,(red_resize_vertical,red_resize_horizontal))

fotografije_varijabla.paste(yellow_vert,(yellow_resize_vertical,yellow_resize_horizontal))
fotografije_varijabla.paste(yellow_hor,(yellow_resize_vertical,yellow_resize_horizontal))
fotografije_varijabla.paste(yellow_vert,(yellow_resize_vertical,fotografije_varijabla.size[1] - yellow_resize_horizontal - 10))
fotografije_varijabla.paste(yellow_hor,(fotografije_varijabla.size[0] - yellow_resize_vertical,yellow_resize_horizontal))
fotografije_varijabla.paste(p25,(yellow_resize_vertical,yellow_resize_horizontal))

fotografije_varijabla.paste(blue_vert,(blue_resize_vertical,blue_resize_horizontal))
fotografije_varijabla.paste(blue_hor,(blue_resize_vertical,blue_resize_horizontal))
fotografije_varijabla.paste(blue_vert,(blue_resize_vertical,fotografije_varijabla.size[1] - blue_resize_horizontal - 10))
fotografije_varijabla.paste(blue_hor,(fotografije_varijabla.size[0] - blue_resize_vertical,blue_resize_horizontal))
fotografije_varijabla.paste(odabrano,(blue_resize_vertical,blue_resize_horizontal))

fotografije_varijabla.show()