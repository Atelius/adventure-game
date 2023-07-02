screen game_over:
   modal True
   key "K_SPACE" action [Function(reset_chest_puzzle), Hide("game_over")]
   key "mousedown_1" action [Function(reset_chest_puzzle), Hide("game_over")]
   frame:
      background "#00000080"
      xfill True
      yfill True
      frame:
         background "#FFFFFFE6"
         xfill True
         padding (15, 0)
         align (0.5, 0.5)
         text "Game Over" color "#000000" size 34 xalign 0.5