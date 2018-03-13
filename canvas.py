import numpy as np
import cv2
import random


class canvas():

    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.new_canvas = np.zeros((self.height, self.width, 3), np.uint8)
        self.randx = np.linspace(10,580)
        self.randy = np.linspace(10,380)
        #white,red, green, blue, yellow, purple, orange
        self.colorlist = [(255,255,255), (0,0,255), (0,255,0), (255,0,0), (0,255,255), (255,0,188), (0,15,255)]
        self.points = 0
        self.value = 10

    def set_color(self, B, G, R):
        self.color = (B, G, R)

    def set_bgColor(self):
        self.new_canvas[:, :] = self.color

    def show_canvas(self):
        cv2.imshow('newCanvas', self.new_canvas)

    def save_drawing(self):
        """This function allows users to save their drawing with a name of
        their choice.
        """
        file_name = input('Please name your drawing: ')
        cv2.imwrite(file_name+'.jpg', self.new_canvas)

    def clear(self):
        """This function clears the screen.
        """
        canvas.new_canvas = np.zeros((self.height, self.width, 3), np.uint8)

    def rectangle(self):
        self.xpos = int(random.choice(self.randx))
        self.ypos = int(random.choice(self.randy))
        color = random.choice(self.colorlist)
        cv2.rectangle(self.new_canvas, (self.xpos, self.ypos), (self.xpos+20,self.ypos+20), color,-1)

    def in_rect(self,pointx,pointy):
        if self.xpos<pointx<self.xpos and self.ypos<pointy<self.ypos:
            self.points += self.value
            return True

if __name__ == "__main__":
    canvas1 = canvas(1280, 960)
    canvas1.set_color(0, 0, 0)
    canvas1.set_bgColor()
    # cam = cv2.VideoCapture(0)
    # print(cam.get(3), cam.get(4))
    while True:
        canvas1.show_canvas()
        if cv2.waitKey(1) & 0xFF == ord('s'):
            canvas1.save_drawing()
            break
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
