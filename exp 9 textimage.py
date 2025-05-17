#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


##reg:no 21223240152
##Name:Santhosh G


# In[ ]:





# In[2]:


# Create a blank image
image = np.zeros((500, 500, 3), dtype=np.uint8)


# In[3]:


# Add text on the image using cv2.putText
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'Hello World', (100, 250), font, 1, (255, 255, 255), 2, cv2.LINE_AA)


# In[4]:


# Display the input image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for displaying
plt.title("Input Image with Text")
plt.axis('off')


# In[5]:


# Create a simple square kernel (3x3)
kernel = np.ones((3, 3), np.uint8)


# In[6]:


# Apply erosion (shrinking effect)
eroded_image = cv2.erode(image, kernel, iterations=1)


# In[7]:


# Display the eroded image
plt.imshow(cv2.cvtColor(eroded_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
plt.title("Eroded Image")
plt.axis('off')


# In[8]:


# Display the eroded image
plt.imshow(cv2.cvtColor(eroded_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
plt.title("Eroded Image")
plt.axis('off')


# In[ ]:




