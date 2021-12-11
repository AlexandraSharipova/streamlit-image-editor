from utils import *


def adjust_hsv(state, block):
    DEFAULT_HUE = .5
    DEFAULT_Value = .5
    DEFAULT_Saturation = .5
    hsv_img = rgb2hsv(state['image'])

    h = block.slider('Hue', min_value=0., max_value=1., value=DEFAULT_HUE)
    hsv_img[:, :, 0] += (h - DEFAULT_HUE) % 1.
    v = block.slider('VAL', min_value=0., max_value=1., value=DEFAULT_HUE)
    hsv_img[:, 0, :] += (v - DEFAULT_Value) % 1.
    s = block.slider('SAT', min_value=0., max_value=1., value=DEFAULT_HUE)
    hsv_img[0, :, :] += (s - DEFAULT_Saturation) % 1.
    state['image'] = hsv2rgb(hsv_img)
