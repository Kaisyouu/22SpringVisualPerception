import cv2
import numpy as np

# Read image
image = cv2.imread("car.jpg")

# Select ROI
r = cv2.selectROI("select the area", image)
print(r)
r1, r2, r3, r4 = r[0], r[1], r[2], r[3]
y = np.array([[r1], [r2], [r3], [r4]])

print(y)

