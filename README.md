# Implementation-of-Erosion-and-Dilation
## Aim
To implement Erosion and Dilation using Python and OpenCV.
## Software Required
1. Anaconda - Python 3.7
2. OpenCV
## Algorithm:
### Step1:
Import the necessary pacakages
### Step2:
Create the text using cv2.putText
### Step3:
Create the structuring element
### Step4:
Erode the image
### Step5:
Dilate the Image
 
## Program:

``` Python
# Import the necessary packages
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Create the Text using cv2.putText
# Create a blank image
image = np.zeros((500, 500, 3), dtype=np.uint8)


# Create the structuring element
# Add text on the image using cv2.putText
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'Hello World', (100, 250), font, 1, (255, 255, 255), 2, cv2.LINE_AA)


# Erode the image
# Create a simple square kernel (3x3)
kernel = np.ones((3, 3), np.uint8)
# Apply erosion (shrinking effect)
eroded_image = cv2.erode(image, kernel, iterations=1)
# Display the eroded image
plt.imshow(cv2.cvtColor(eroded_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
plt.title("Eroded Image")
plt.axis('off')



# Dilate the image

# Display the eroded image
plt.imshow(cv2.cvtColor(eroded_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
plt.title("Eroded Image")
plt.axis('off')



```
## Output:

### Display the input Image
![Screenshot 2025-05-17 142106](https://github.com/user-attachments/assets/4e3d179d-acf7-4839-92d6-2b961287ac6e)


### Display the Eroded Image
![Screenshot 2025-05-17 143131](https://github.com/user-attachments/assets/beac4a13-bf9a-4bbe-b2f0-cb3c46f11cbb)


### Display the Dilated Image
![Screenshot 2025-05-17 143150](https://github.com/user-attachments/assets/15c9a73d-9eca-4aa8-99df-14928455a9e6)


## Result
Thus the generated text image is eroded and dilated using python and OpenCV.
