import sys

#checks for OS
platform=sys.platform

#imports for MacOS
if platform=="darwin":
    import threading
    from Quartz.CoreGraphics import *
    from Quartz import *
    from random import *
    import subprocess
    import time

#imports for Windows
elif platform=="win32":
    print "Not done yet"

#imports for Linux
elif platform=="linux2":
    print "Not done yet"

#moves mouse to random position in screen boundaries
def moveMouse (platform):
    if (platform=="darwin"):
        mainMonitor = CGDisplayBounds(CGMainDisplayID())
        theEvent = CGEventCreateMouseEvent(None, kCGEventMouseMoved, (randint(0,mainMonitor.size.width),randint(0,mainMonitor.size.height)), kCGMouseButtonLeft)
        CGEventPost(kCGHIDEventTap, theEvent)
        return

while (1):
    time.sleep(randint(0,10))
    moveMouse(platform)
