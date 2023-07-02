label chest_puzzle:
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
    $chest_unlock_tries = 2
    $chest_difficulty = 1

    call screen scene_cofre
return
