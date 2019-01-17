# Rust Detection Algorithm Tutorial

This tutorial aims at explaining some key concepts of `image processing` using `opencv` with python.
We will try to understand each line of the [code](Air_Drums.py)

> ###### Note for someone using python for the first time:
> anything written after '#' will be treated as a comment. 
> it is a good practice to add comments in your code. 
> It makes the code easy to understand.


### Importing all the required libraries

```python
import cv2
from sys import argv
import numpy as np
import os
import glob
```

### Understanding the rust_detect() function 

First we import the image and save it in form of an array.
Since the setup for analysis and image capturing is fixed 
we do not need to worry about image resolution issue.

```python
# Importing the image
A = cv2.imread(file)
```

#### Converting image from BGR to HSV

We convert the image into HSV colour space using the following line of code.
```python
img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```
`Why transform the image into HSV colour space ??`
Because the algorithm detects the rust based on its property of colour.
Rusted area for this specific metal had a specific colour range
(`grey-brown` represent lower level of rust while `Dark reddish-brown` 
represent sever rusting). Using HSV(Hue-Saturation-Value) colour space we can distinguish 
between different colours much accurately that we can in RGB colour space.

#### Setting range of HSV values for rust detection
Below code is used to detect pixels corresponding to rusted metal surface.
```python
# Range for lower red
lower_red = np.array([0,70,70])
upper_red = np.array([20,255,150])
mask0 = cv2.inRange(img_hsv, lower_red, upper_red)
	
# range for upper red
lower_red = np.array([220,70,70])
upper_red = np.array([255,255,150])
mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
mask = mask0+mask1
```

Hue range | 0-20 | 170-180
---|---|---

>The Hue values actually range between 0-360 degrees but
>in OpenCV to fit into 8bit value the range is from 0-180.
>Red colour is represented by 0-20 and 170-180 values.


Saturation range | 70-200
---|---
> Saturation represents purity of colour. Pure Red, Green and Blue
>are considered to be true saturated colours. As saturation decreases the effect of the other two
>colour component increases.

Value range | 70-150
---|---
> Value corresponds to the brightness of the image. For a given pixel if the value is increased or 
> decreased then values of R,G and B will increase or decrease respectively but their percentage 
>contribution will remain unchanged.

Now we understand why we need to convert to HSV colour space.

The below command returns an array with pixel value = 255  for pixels 
having HSV values within upper and lower value range and 0 otherwise.
This way we generate a mask.
```python
mask = cv2.inRange(img_hsv, lower_red, upper_red)
```

And finally we `OR` both the masks (mask0 and mask1) to get 
our final mask. 
```python
mask = mask0 + mask
```
This is also a simple example of operator overloading of `+`.




#### Calculating the number of rust pixels
To calculate the total pixesl corresponding to rusted metal region 
we simply find the number of white pixels in the final mask.
