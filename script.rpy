label start:
    $config.rollback_enabled = False
    $quick_menu = False
    $environment_SM = SpriteManager(event = environmentEvents)
    $inventory_SM = SpriteManager(update = inventoryUpdate, event = inventoryEvents)
    $environment_sprites = []
    $inventory_sprites= []
    $environment_items = []
    $inventory_items= []
    $environment_item_names = []
    $inventory_item_names = ["Key", "Lantern", "Matches", "Secateur"]
    $current_scene = "scene_first_room"
    $inventory_rb_enabled = False
    $inventory_lb_enabled = False
    $inventory_slot_size = (int(215/2), int(196/2))
    $inventory_slot_padding = 22/2
    $inventory_first_slot_x = 350
    $dialogue = {}
    $inventory_drag = False
    $item_dragged = ""
    $mousepos = (0.0,0.0)
    $i_overlap = False
    $ie_overlap = False
     

    hide screen UI

    with fade
    "You have 2 paths in front of you, what path would you choose?"
    menu:
        "Room Forest":
            show screen UI
            jump lbl_inventory
        "Chest room":
            show screen UI
            jump chest_room
    return