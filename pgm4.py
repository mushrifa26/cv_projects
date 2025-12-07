# Image Blurring (Smoothing)
import cv2

img = cv2.imread("image.jpg")
cv2.imshow("Image", img)
blur = cv2.GaussianBlur(img, (45, 45), 0)
cv2.imshow("Blurred", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
