import cv2
import time
from managers import WindowManager, CaptureManager

class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager(
            'Cameo',
            self.onKeypress
        )
        self._captureManager = CaptureManager(
            cv2.VideoCapture(0), self._windowManager , True
        )

    def run(self):
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress (self,keycode):
        """
        Handle a keypress.

        space  -> Take a screenshot
        tab    -> Start/stop recording a screencast.
        escape -> Quit

        """

        if keycode == 32: #space
            self._captureManager.writeImage('screenshot'+str(time.time())+'.png')
        elif keycode == 9:
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27:
            self._windowManager.destroyWindow()
            
oliver = Cameo() #生成实例　oliver
oliver.run() #启动程序　Bingo!!!
