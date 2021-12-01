import cv2
import numpy as np
import requests
import io
import json
import os
from gtts import gTTS

# img = cv2.imread("ss.jpg")
# height, width, _ = img.shape

# # Cutting image
# # roi = img[0: height, 400: width]
# roi = img

# # Ocr
# url_api = "https://api.ocr.space/parse/image"
# _, compressedimage = cv2.imencode(".jpg", roi, [1, 90])
# file_bytes = io.BytesIO(compressedimage)

# result = requests.post(url_api,
#               files = {"ss.jpg": file_bytes},
#               data = {"apikey": "helloworld",
#                       "language": "eng"})

# result = result.content.decode()
# result = json.loads(result)

# parsed_results = result.get("ParsedResults")[0]
# text_detected = parsed_results.get("ParsedText")
# print(text_detected)
language = 'en'
myobj = gTTS(text="यह हिंदी में एक उदाहरण है", lang='hi', slow=False)
myobj.save("test.mp3")

# cv2.imshow("roi", roi)
# cv2.imshow("Img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

###      bookname_pg%d.txt 
###      readOutLoud(bookname_pg%d.txt )