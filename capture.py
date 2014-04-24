import cv2
import sys
import math
import curses
import signal

stdscr = curses.initscr()

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        curses.endwin()
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

width = int(sys.argv[1]) if len(sys.argv) > 1 else 50

palette = [' ', '.', '.', '/', 'c', '(', '@', '#', '8']

while True:
    # Capture the image
    img = cv2.VideoCapture(0).read()[1]

    # Resize the Image
    size = img.shape[:-1]
    height = size[0] * width / size[1]
    thumbnail = cv2.resize(img, ( height, width))
    img = thumbnail

    # Clear screen

    # Print the output
    for x in xrange(height-1):
        for y in xrange(width-1):
            b, g, r = img[y, x]
            value = 0.1145 * b + g * 0.5866 + r * 0.2989
            index = int(math.floor( value / (256.0 / (len(palette)))))
            try:
                stdscr.move(x,y)
                stdscr.addch(palette[index])
            except:
                pass
    stdscr.refresh()
