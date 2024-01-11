from PIL import Image, ImageFilter
import colorsys
import sys
from lib import *

"""
uses:
isolate path_in path_out k
impose path_pal path_in path_out k interpolate

"""

def isolate():
    image_path = sys.argv[2]
    output_path = sys.argv[3]
    k = int(sys.argv[4])
    print("opening image")
    img = Image.open(image_path).convert("RGB")
    print("extracting target colors")
    colors = k_means(img,k)
    print("generating output")
    img = transform(img, colors, colors)
    print("saving")
    img.convert("RGB").save(output_path)
    print("complete")

def impose():
    pal_image = sys.argv[2]
    image_path = sys.argv[3]
    output_path = sys.argv[4]
    k = int(sys.argv[5])
    print("opening palette image")
    img = Image.open(pal_image).convert("RGB")
    print("extracting palette colors")
    target = k_means(img,k)
    print("opening target image")
    img = Image.open(image_path).convert("RGB")
    print("extracting target colors")
    colors = k_means(img,k)
    print("generating output")
    if len(sys.argv) > 6:
        img = transform_interpolate(img, colors, target)
    else:
        img = transform(img, colors, target)
    print("saving")
    img.convert("RGB").save(output_path)
    print("complete")

if __name__ == "__main__":
    if sys.argv[1] == "isolate":
        isolate()
    elif sys.argv[1] == "impose":
        impose() 
    else:
        print("undefined command")
