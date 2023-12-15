#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
import sys, os, subprocess,time
from TouchStyle import *
from launcher import LauncherPlugin

PLAYER = "/opt/ftc/apps/system/bad-apple/test.sh"
VIDEO = "/opt/ftc/apps/system/bad-apple/bad-apple.mp4"
FB = "/dev/fb0"

# subclass the txtwidget to catch the close event
class FTGUIBaseWidget(TouchBaseWidget):
    def __init__(self):
        TouchBaseWidget.__init__(self)

    def close(self):
        print("close called :3")
        # this used to be some manager script that took start/stop args to start/stop stuff
        #subprocess.Popen([SCRIPT])
        #time.sleep(3)
        #TouchBaseWidget.close(self)

class FtcGuiPlugin(LauncherPlugin):
    def __init__(self, application):
        LauncherPlugin.__init__(self, application)

        self.w = FTGUIBaseWidget()
        self.w.show()

        subprocess.Popen(["sudo",PLAYER,VIDEO,FB])

if __name__ == "__main__":
    class FtcGuiApplication(TouchApplication):
        def __init__(self, args):
            super().__init__(args)
            module = FtcGuiPlugin(self)
            self.exec_()
    FtcGuiApplication(sys.argv)
else:
    def createPlugin(launcher):
        return FtcGuiPlugin(launcher)

