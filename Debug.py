import cv2
import matplotlib.pyplot as plt

class debug():
    def __init__(self, torf, size = (20, 15), num = 10):
        self.enable = torf
        self.__debug_img_size = size
        self.__debug_img_num = num
    def initialize(self):
        self.__debug_num = 1
        self.fig = plt.figure(figsize=self.__debug_img_size) #Debug
        self.fig.subplots_adjust(left=0, right=1, bottom=0, top=0.5, hspace=0.05, wspace=0.05)  #Debug
    def setFigSize(size):
        self.__debug_img_size = size
    def setFigNum(num):
        self.__debug_img_num = num
    def draw(self, img, name):
        if self.enable == False:
            return
        self.ax = self.fig.add_subplot(1, self.__debug_img_num, self.__debug_num, xticks=[], yticks=[]) #Debug
        self.__debug_num += 1 #Debug
        self.ax.set_title(name) #Debug
        self.ax.imshow(img, cmap = 'gray') #Debug