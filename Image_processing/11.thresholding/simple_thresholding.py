# USAGE
# python simple_thresholding.py opencv_logo.png

# import the necessary packages
import sys
import cv2

#Get the image

img = sys.argv[1]

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(img)
blurred = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#blurred = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow("Image", image)

# apply basic thresholding -- the first parameter is the image
# we want to threshold, the second value is is our threshold
# check; if a pixel value is greater than our threshold (in this
# case, 200), we set it to be BLACK, otherwise it is WHITE.
(T, threshInv) = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)

# using normal thresholding (rather than inverse thresholding),
# we can change the last argument in the function to make the coins
# black rather than white.
(T, thresh) = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

# finally, we can visualize only the masked regions in the image
cv2.imshow("Output", cv2.bitwise_and(image, image, mask=threshInv))
cv2.waitKey(0)