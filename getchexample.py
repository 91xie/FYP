#getch()-like unbuffered c haracter reading from stdin on Unix Python
#look up code.activestate.com/

class _Getch:
    def __init__(self):
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, terminos
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch=sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd,termios.TCSADRAIN, old_settings)
        return ch


getch = _Getch()
print getch
