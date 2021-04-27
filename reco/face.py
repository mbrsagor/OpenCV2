import cv2

image_name = "mbr-sagor.jpeg"
image = cv2.imread(image_name)
cv2.imshow("Bozlur Rosid Sagor", image)

keyboard = cv2.waitKey(0)
if keyboard == 27:
    cv2.destroyAllWindows()
elif keyboard == ord('s'):
    cv2.imwrite('New.jpg', image)
    cv2.destroyAllWindows()
