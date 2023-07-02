screen UI:
    zorder 1
    image "ui/inventory-icon-bg.png" xpos 0 ypos 0.8 at half_size
    imagebutton auto "ui/inventory-icon-%s.png" action If(renpy.get_screen("inventory") == None, true = Show("inventory"), false= Hide("inventory")) xpos 0.03 ypos 0.825 at half_size

screen inventory:
    image "ui/inventory-bg.png" xpos 0.17 ypos 0.8 at half_size
    image "ui/inventory-slots.png" xpos 0.274  ypos 0.845 at half_size

    imagebutton idle If(inventory_rb_enabled == True, true = "ui/inventory-arrow-right-enabled-idle.png", false = "ui/inventory-arrow-right-disabled.png" ) hover If(inventory_rb_enabled == True,  true = "ui/inventory-arrow-right-enabled-idle.png", false = "ui/inventory-arrow-right-disabled.png" ) action Function(inventoryArrows,button = "right" ) xpos 0.921 ypos 0.86 at half_size
    imagebutton idle If(inventory_lb_enabled == True, true = "ui/inventory-arrow-left-enabled-idle.png", false = "ui/inventory-arrow-left-disabled.png" ) hover If(inventory_lb_enabled == True,  true = "ui/inventory-arrow-left-enabled-idle.png", false = "ui/inventory-arrow-left-disabled.png" ) action Function(inventoryArrows,button = "left" ) xpos 0.202 ypos 0.86 at half_size