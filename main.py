from kb import KMKKeyboard
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.keys import KC
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData

from kmk.modules.holdtap import HoldTap
holdtap = HoldTap()
keyboard = KMKKeyboard()

keyboard.modules.append(holdtap)
#keyboard.debug_enabled = True

layers = Layers()
keyboard.modules.append(Layers())

#多功能切层按键HOLDTAP
SPC_1 = KC.LT(1, KC.SPC)#按住切到层1，点击为SPC
ENT_2 = KC.LT(2, KC.ENT)
#多功能HOLDTAP
TAB_ESC=KC.HT(KC.TAB, KC.ESC, prefer_hold=False)

KMKKeyboard.keymap = [
    [  #基础层0
            KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,                         KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,\
            KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.G,                         KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,\
            KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,                         KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,\
                                             KC.TRNS,  KC.TRNS, SPC_1 ,       ENT_2,  KC.MO(3), KC.TRNS,
        ],
        [  #1
              KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,                         KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,\
              KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,                         KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,\
              KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,                         KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,\
                                                KC.TRNS, KC.TRNS,KC.TRNS,    KC.TRNS,  KC.TRNS, KC.TRNS,
        ],
        [  #2
              KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,                         KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,\
              KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,                         KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,\
              KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,                         KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,\
                                                KC.TRNS, KC.TRNS,KC.TRNS,    KC.TRNS,  KC.TRNS, KC.TRNS,
        ],
        [  #3
              KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,                         KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,\
              KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,                         KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,\
              KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,                         KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,\
                                                KC.TRNS, KC.TRNS,KC.TRNS,    KC.TRNS,  KC.TRNS, KC.TRNS,
        ],

        
        
    ]



oled = Oled(OledData(image={0:OledReactionType.LAYER,1:["0.bmp","1.bmp","2.bmp","3.bmp"]}),toDisplay=OledDisplayMode.IMG,flip=False)
keyboard.extensions.append(oled)

split = Split(split_type=SplitType.BLE, split_side=SplitSide.LEFT,split_target_left=False,)
keyboard.modules.append(split)

if __name__ == '__main__':
    keyboard.go()