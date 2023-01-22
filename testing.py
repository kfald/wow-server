import pyautogui
import cv2
import pyautogui
import pytesseract
from PIL import Image
import time




def main():
    sequence = 0
    queue()
    print('done')


def queue():
    print('help')

    img = pyautogui.screenshot(region=(100,100, 500, 500))
    img.save('screenshot.png')

    #img = 'server queue.png'
    img2 = Image.open('test.png')
    pytesseract.image_to_boxes('test.png',None,)
    result = pytesseract.image_to_string(img2)
    while sequence == 0:
        if "reverb" in result:

            print("its in there")
            sequence = 1


        else:
            print("its not in there")
            sequence = 0
    print('still running')

    while sequence == 1:
        time.sleep(5)
        print('...')


    #print(result)
if __name__=="__main__":
    main()
    




