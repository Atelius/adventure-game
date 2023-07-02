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

    hide screen UI

    with fade
    "You have 2 paths in front of you, what path would you choose?"
    menu:
        "Room Forest":
            show screen UI
            jump inventory
        "Chest room":
            show screen UI
            jump chest_puzzle
    return