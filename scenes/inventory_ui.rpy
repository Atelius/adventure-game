screen UI:
    zorder 1
    image "ui/inventory-icon-bg.png" xpos 0 ypos 0.8 at half_size
    imagebutton auto "ui/inventory-icon-%s.png" action If(renpy.get_screen("inventory") == None, true = Show("inventory"), false= Hide("inventory")) xpos 0.03 ypos 0.825 at half_size

screen inventory:
    zorder 3
    image "ui/inventory-bg.png" xpos 0.17 ypos 0.8 at half_size
    image "ui/inventory-slots.png" xpos 0.274  ypos 0.845 at half_size

    imagebutton idle If(inventory_rb_enabled == True, true = "ui/inventory-arrow-right-enabled-idle.png", false = "ui/inventory-arrow-right-disabled.png" ) hover If(inventory_rb_enabled == True,  true = "ui/inventory-arrow-right-enabled-idle.png", false = "ui/inventory-arrow-right-disabled.png" ) action Function(inventoryArrows,button = "right" ) xpos 0.921 ypos 0.86 at half_size
    imagebutton idle If(inventory_lb_enabled == True, true = "ui/inventory-arrow-left-enabled-idle.png", false = "ui/inventory-arrow-left-disabled.png" ) hover If(inventory_lb_enabled == True,  true = "ui/inventory-arrow-left-enabled-idle.png", false = "ui/inventory-arrow-left-disabled.png" ) action Function(inventoryArrows,button = "left" ) xpos 0.202 ypos 0.86 at half_size

    add inventory_SM

screen inventoryItemMenu(item):
    zorder 7
    frame:
        xysize (inventory_slot_size[0], inventory_slot_size[1])
        background "#FFFFFF30"
        xpos int(item.x)
        ypos int(item.y)
        imagebutton auto "ui/view-inventory-item-%s.png" align (0.0, 0.5) at half_size action [Show("inspectItem", items =[item.type]),Hide("inventoryItemMenu")]
        imagebutton auto "ui/use-inventory-item-%s.png" align (1.0, 0.5) at half_size action [Function(startDrag, item = item),Hide("inventoryItemMenu")]

screen inspectItem(items):
    modal True
    zorder 4
    button:
        xfill True
        yfill True
        action If(len(items) > 1, true = RemoveFromSet(items, items[0]), false = [Hide("inspectItem"), If(len(dialogue) > 0, true = Show("characterSay"), false = NullAction())] )
        image "popup/items-pop-up-bg.png" align(0.5, 0.5) at half_size

        python:
            item_name = ""
            for name in inventory_item_names:
                temp_name = name.replace(" ","-")
                if temp_name.lower() ==  items[0]:
                    item_name = name

        text "{}".format(item_name) size 20 align (0.5,0.25)
        if items[0] == "lantern":
            $lantern_state = inventory_sprites[inventory_items.index("lantern")].state
            image "popup/{}-{}-pop-up.png".format("lantern",lantern_state) align (0.5,0.55) at half_size
        else:
            image "popup/{}-pop-up.png".format(items[0]) align (0.5,0.55) at half_size
