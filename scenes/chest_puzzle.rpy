screen scene_cofre: 
      image "background.png" at half_size
      on "show" action Function(reset_chest_puzzle)
      imagebutton auto "chest-closed-%s.png" action [Hide("scene_cofre"), Show("chest_puzzle")] at chest_transform

screen chest_puzzle:
      # Siempre que inicie el puzzle, resetea los valores y selecciona una zona segura aleatoria
      on "show" action Function(reset_chest_puzzle)
      key ["K_SPACE", "mousedown_1"] action If(chest_unlocked, true = [Hide("chest_puzzle", transition = Fade(1,1,1)), Show("scene_cofre")], false= Function(check_slider_safe_zone))
      image "background.png" at half_size   
      if not chest_unlocked:
                  frame:
                        background "#FFFFFF"
                        padding (5,5)
                        align (0.5, 0.3)
                        text "Attempts left: [chest_unlock_tries]" size 18 color "#000000"  text_align 0.5
                  frame:
                        background None
                        align (0.5, 0.4)
                        xysize slider_bar_size
                        image "slider-bar.png" at half_size
                        add slider_SM
                  image "chest-closed-idle.png" align (0.5, 0.7) at half_size
      else:
                  image "chest-opened.png" align (0.5, 0.7) at chest_unlocked_anim