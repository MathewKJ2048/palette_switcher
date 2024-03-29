# Palette Switcher
A python script to identify and change the color palette of arbitrary images



## Pre-requisites:

- python 3
- numpy
- PIL
- scikit-learn

## Working:

- The algorithm uses k-means clustering in RGB space to identify common colors in an image.
- Each common color is mapped to a color in the target palette.
- Each pixel is replaced by the target color mapped to the common color closest to it in RGB space, where
- Closeness is measured using Manhattan distance.
- Interpolation is done on the color's projection in the plane containing the two closest common colors, followed by taking the weighted average

## Use:

Run `main.py` with one of the following arguments:

`python <path_to_main.py> isolate <path_to_input> <path_to_output> k`

This breaks an image down into k common colors.

`python <path_to_main.py> impose <path_to_palette> <path_to_input> <path_to_output> k [interpolation]`

This extracts the palette used in the palette image and applies it to the input image.

## Examples
### Original image

![](https://github.com/MathewKJ2048/palette_switcher/blob/main/test/original.png)

### Isolate
![](https://github.com/MathewKJ2048/palette_switcher/blob/main/test/cat_2.png)
![](https://github.com/MathewKJ2048/palette_switcher/blob/main/test/cat_4.png)
![](https://github.com/MathewKJ2048/palette_switcher/blob/main/test/cat_8.png)
![](https://github.com/MathewKJ2048/palette_switcher/blob/main/test/cat_16.png)

## Impose
![](https://github.com/MathewKJ2048/palette_switcher/blob/main/test/out_1.png)
![](https://github.com/MathewKJ2048/palette_switcher/blob/main/test/out_2.png)
![](https://github.com/MathewKJ2048/palette_switcher/blob/main/test/out_3.png)
![](https://github.com/MathewKJ2048/palette_switcher/blob/main/test/out_4.png)
![](https://github.com/MathewKJ2048/palette_switcher/blob/main/test/out_5.png)
![](https://github.com/MathewKJ2048/palette_switcher/blob/main/test/out_6.png)
![](https://github.com/MathewKJ2048/palette_switcher/blob/main/test/out_7.png)
![](https://github.com/MathewKJ2048/palette_switcher/blob/main/test/out_8.png)

## Acknowledgements:

- [Ivan Radik](https://www.flickr.com/photos/26344495@N05/) for the photo [Fluffy ginger cat looking away from camera](https://www.flickr.com/photos/26344495@N05/)
- [https://coolors.co/](https://coolors.co/) for the palettes used
