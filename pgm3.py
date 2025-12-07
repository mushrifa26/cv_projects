import cv2

img = cv2.imread("image.jpg")
cv2.imshow("Image", img)


resized = cv2.resize(img, (300, 300))
cv2.imshow("Resized", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
