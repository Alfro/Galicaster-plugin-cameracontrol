# WARNING: THIS IS HACKISH
# Example: v4l2-ctl --set-ctrl=zoom_absolute=500
# Variables:
# ----------------------
# pan_absolute (int)    : min=-36000 max=36000 step=3600 default=0 value=-18000
# tilt_absolute (int)    : min=-36000 max=36000 step=3600 default=0 value=36000
# zoom_absolute (int)    : min=100 max=500 step=1 default=100 value=150

import subprocess
from subprocess import call

MIN_ZOOM = 100
MAX_ZOOM = 200 # The v4l2-ctl --list-ctrls returns 500, but tests disagree with this
MIN_TILT = -36000
MAX_TILT = 36000
MIN_PAN = -36000
MAX_PAN = 36000

class VPTZ:
    def __init__(self):
        self.device = "/dev/video0"
        self.zoom = MIN_ZOOM
        self.pan = MIN_PAN
        self.tilt = MIN_TILT

        self.zoom_step = 20
        self.pan_step = 6000
        self.tilt_step = 6000
        self.set_ctrl('pan_absolute', self.pan)
        self.set_ctrl('tilt_absolute', self.tilt)
        self.set_ctrl('zoom_absolute', self.zoom)

    def move_right(self):
        self.pan += self.pan_step
        if( self.pan > MAX_PAN):
            self.pan = MAX_PAN
        self.set_ctrl('pan_absolute', self.pan)

    def move_left(self):
        self.pan -= self.pan_step
        if( self.pan < MIN_PAN):
            self.pan = MIN_PAN
        self.set_ctrl('pan_absolute', self.pan)

    def move_down(self):
        self.tilt -= self.tilt_step
        if( self.tilt < MIN_TILT):
            self.tilt = MIN_TILT
        self.set_ctrl('tilt_absolute', self.tilt)

    def move_up(self):
        self.tilt += self.tilt_step
        if( self.tilt > MAX_TILT):
            self.tilt = MAX_TILT
        self.set_ctrl('tilt_absolute', self.tilt)

    def zoom_in(self):
        self.zoom += self.zoom_step
        if( self.zoom > MAX_ZOOM):
            self.zoom = MAX_ZOOM
        self.set_ctrl('zoom_absolute', self.zoom)

    def zoom_out(self):
        self.zoom -= self.zoom_step
        if( self.zoom < MIN_ZOOM):
            self.zoom = MIN_ZOOM
        self.set_ctrl('zoom_absolute', self.zoom)

    def set_ctrl(self, ctrl, value):
        ctrl = ctrl+"="+str(value)
        call(["v4l2-ctl", "-d", self.device, "--set-ctrl", ctrl], stdout=subprocess.PIPE)

    def set_zoom_speed(self, zoom_step):
        pass

    def set_zoom_speed(self, zoom_step):
        pass
