import cv2
import pytesseract
import numpy as np

print("Actual License Plate", "\t", "Predicted License Plate", "\t", "Accuracy")
print("--------------------", "\t", "-----------------------", "\t", "--------")


def calculate_predicted_accuracy(actual_list, predicted_list):
    for actual_plate, predict_plate in zip(actual_list, predicted_list):
        accuracy = "100 %"
        num_matches = 0
        if actual_plate == predict_plate:
            accuracy = "100 %"
        else:
            if len(actual_plate) == len(predict_plate):
                print("test")
                for a, p in zip(actual_plate, predict_plate):
                    if a == p:
                        num_matches += 1
                accuracy = str(round((num_matches / len(actual_plate)), 2) * 100)
                accuracy += "%"
        print("	 ", actual_plate, "\t\t\t", predicted_list, "\t\t\t\t\t", accuracy)


pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
plate = cv2.imread('img0006.jpg')
plate = cv2.cvtColor(plate, cv2.COLOR_RGB2GRAY)
plate = cv2.resize(plate, None, fx=3, fy=3)
remove_noise = cv2.GaussianBlur(plate, (3, 3), 0)
ret3, th3 = cv2.threshold(remove_noise, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
img_dilation = cv2.dilate(th3, kernel, iterations=2)
img_erosion = cv2.erode(img_dilation, kernel, iterations=1)
edges = cv2.Canny(img_erosion, 100, 200)
contours, d = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros(img_erosion.shape[:2], dtype=np.uint8)
for c in contours:
    if cv2.contourArea(c) > plate.shape[0] * plate.shape[1] * 7 / 1000:
        x, y, w, h = cv2.boundingRect(c)
        cv2.drawContours(mask, [c], 0, (255), -1)
erode = cv2.threshold(img_erosion, 1, 255, cv2.THRESH_BINARY_INV)[1]
result = cv2.bitwise_and(erode, erode, mask=mask)
result = cv2.threshold(result, 1, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Image", result)
data = pytesseract.image_to_string(result, lang='eng', config='--psm 6')
PERMITTED_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
data = "".join(c for c in data if c in PERMITTED_CHARS)

#print("The plate number : " + data)
predicted_license_plates = data
list_license_plates = ["6239030"]
calculate_predicted_accuracy(list_license_plates, predicted_license_plates)

cv2.waitKey(0)
