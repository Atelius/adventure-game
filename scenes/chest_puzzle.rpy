screen scene_cofre: 
      image "background.png" at half_size
      on "show" action Function(reset_chest_puzzle)
      if vines_open:
            imagebutton auto "chest-closed-%s.png" action [Hide("scene_cofre"), Show("chest_puzzle")] at chest_transform
            
      else:
            imagebutton auto "chest-closed-%s.png" action [] at chest_transform
            add environment_SM
            
      

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
                 


label setupChestRoom:
      $environment_items = ["chest-vines"]
      $environment_sprites = [];
      python:
            for item in environment_items:
                  idle_image = Image("environment/{}-idle.png".format(item))
                  hover_image = Image("environment/{}-hover.png".format(item))
                  t = Transform(child = idle_image, zoom =0.5)
                  environment_sprites.append(environment_SM.create(t))
                  environment_sprites[-1].type = item
                  environment_sprites[-1].idle_image = idle_image
                  environment_sprites[-1].hover_image = hover_image

            if item == "chest-vines":
                  environment_sprites[-1].width = 450/2
                  environment_sprites[-1].height = 603/2
                  environment_sprites[-1].x = 950/2
                  environment_sprites[-1].y = 500/2
                  environment_sprites[-1].z = 1

      #scene scene-forest-bg at half_size
      $slider_SM = SpriteManager(update = slider_update)
      $slider_sprites = []

      # Safe zone variables
      $safe_zone_image = Image("safe-zone.png")
      $safe_zone_transform = Transform( child = safe_zone_image, zoom = 0.5)
      $safe_zone_size = (int(149/2), int(70/2))
      $slider_sprites.append(slider_SM.create(safe_zone_transform))
      $slider_sprites[-1].type = "safe-zone"

      # Slider variables
      $slider_bar_size = (int(545 / 2), int(70/2))
      $slider_image = Image("slider.png")
      $slider_transform = Transform (child = slider_image, zoom = 0.5)
      $slider_sprites.append(slider_SM.create(slider_transform))
      $slider_sprites[-1].type = "slider" 
      $slider_sprites[-1].direction = "right"
      $slider_size = (int(48/2), int(66/2))
      $slider_speed = 2
      $stop_slider = False
      
      # Chest Variables
      $chest_unlocked = False
      $chest_unlock_tries = 5
      $chest_difficulty = 1
      $vines_open = False

      call screen scene_cofre
      #jump chest_puzzle
      return

label chest_room:
      jump setupChestRoom
      return