label setupFirstRoom:
    $environment_items = ["box", "door-vines", "key", "lantern"]

    python:
        for item in environment_items:
            idle_image = Image("environment/{}-idle.png".format(item))
            hover_image = Image("environment/{}-hover.png".format(item))
            t = Transform(child = idle_image, zoom =0.5)
            environment_sprites.append(environment_SM.create(t))
            environment_sprites[-1].type = item
            environment_sprites[-1].idle_image = idle_image
            environment_sprites[-1].hove_image = hover_image

            # set image to half size (depends on file size x size)
            if item == "box":
                environment_sprites[-1].width = 157/2
                environment_sprites[-1].height = 115/2
                environment_sprites[-1].x = 780
                environment_sprites[-1].y = 420
            if item == "door-vines":
                environment_sprites[-1].width = 450/2
                environment_sprites[-1].height = 603/2
                environment_sprites[-1].x = 345
                environment_sprites[-1].y = 160
            if item == "key":
                environment_sprites[-1].width = 101/2
                environment_sprites[-1].height = 55/2
                environment_sprites[-1].x = 1020
                environment_sprites[-1].y = 430
            if item == "lantern":
                environment_sprites[-1].width = 123/2
                environment_sprites[-1].height = 181/2
                environment_sprites[-1].x = 1200
                environment_sprites[-1].y = 355

    scene scene-forest-bg at half_size
    call screen scene_first_room
    return

label inventory:
   
    jump setupFirstRoom
    return