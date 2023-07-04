init python:
   def slider_update(st):
      global slider_speed

      for sprite in slider_sprites:
         if sprite.type == "slider":
            if round(sprite.x) < slider_bar_size[0] - slider_size[0] and sprite.direction == "right":
               sprite.x += slider_speed * chest_difficulty
               slider_speed += 0.04
            elif round(sprite.x)   >= slider_bar_size[0] - slider_size[0] and sprite.direction == "right":
               sprite.direction = "left"
               slider_speed = 2
            elif round(sprite.x)   >0 and sprite.direction == "left":
               sprite.x -= slider_speed * chest_difficulty
               slider_speed += 0.04
            elif round(sprite.x)  == 0 and sprite.direction == "left":
               sprite.direction = "right"
               slider_speed = 2
      if not stop_slider:
         return 0
      else:
         return None      

   def check_slider_safe_zone():
      global chest_unlocked
      global chest_unlock_tries
      global stop_slider

      for slider in slider_sprites:
         if slider.type == "slider":
            for safe_zone in slider_sprites:
               if safe_zone.type == "safe-zone":
                  if safe_zone.x < slider.x < safe_zone.x + safe_zone_size[0]:
                     chest_unlocked = True
                     stop_slider = True
                     renpy.play("audio/open-door.ogg", "sound")
                  elif chest_unlock_tries > 0:
                     renpy.play("audio/error.ogg", "sound")
                     chest_unlock_tries -= 1
                  if chest_unlock_tries == 0:
                     renpy.show_screen("game_over")
                     stop_slider = True

# Resetea el juego
   def reset_chest_puzzle():
      global chest_unlocked
      global chest_unlock_tries
      global stop_slider
      global slider_speed

      chest_unlocked = False
      chest_unlock_tries = 5
      stop_slider = False
      slider_speed = 2


      for sprite in slider_sprites:
         if sprite.type == "slider":
            sprite.x = 0
         elif sprite.type == "safe-zone":
            # Aqui es donde mueve la zona a una poscion aleatoria
            random_x = renpy.random.randint(0, slider_bar_size[0] - safe_zone_size[0])
            sprite.x = random_x
      slider_SM.redraw(0)
      renpy.restart_interaction()


# Functions of inventory
   def inventoryUpdate(st):
      if inventory_drag == True:
         for item in inventory_sprites:
            if item.type == item_dragged:
               item.x = mousepos[0] - item.width/2
               item.y = mousepos[1] - item.height/2
               item.zorder = 99
         return 0
      return None

   def inventoryEvents(event,x,y,at):
      global mousepos
      global dialogue
      global inventory_drag
      global i_overlap
      global ie_overlap
      #global i_combine

      #32768 is used because the inventory is shared among the screens, and it creates a sub screen, thats why it always throws 32768  
      if event.type == renpy.pygame_sdl2.MOUSEBUTTONUP:
            if event.button == 1:
               for item1 in inventory_sprites:
                  if item1.visible == True:
                     if item1.x<= x <= item1.x + item1.width and item1.y <= y <= item1.y + item1.height:
                        inventory_drag = False
                        i_combine = False
                        ie_combine = False
                        for item2 in inventory_sprites:
                           items_overlap = checkItemsOverlap(item1,item2)
                           if items_overlap == True:
                              i_overlap = True
                              if(item1.type == "matches" or item1.type =="lantern") and (item2.type == "matches" or item2.type =="lantern"):
                                 i_combine = True
                                 if(item1.type == "matches"):
                                    removeInventoryItem(item1)
                                 else:
                                    removeInventoryItem(item2)
                                 lantern_image = Image("items/inventory-lantern-lit.png")
                                 t = Transform(child = lantern_image, zoom=0.5)
                                 inventory_sprites[inventory_items.index("lantern")].set_child(t)
                                 inventory_sprites[inventory_items.index("lantern")].item_image = lantern_image
                                 inventory_sprites[inventory_items.index("lantern")].state = "lit"
                                 renpy.show_screen("inspectItem", ["lantern"])
                                 characterSay(who ="You", what = ["The lantern is now lit!"], inspectItem = True)
                                 inventory_SM.redraw(0)
                                 renpy.restart_interaction()
                                 break
                              else:
                                 item1.x = item1.original_x
                                 item1.y = item1.original_y
                                 item1.zorder = 0
                                 renpy.hide_screen("inventoryItemMenu")
                                 renpy.restart_interaction()
                                 break
                                 #characterSay(who ="You", what = ["That doesn't seems to work.", "Try something else."])
                        if i_combine == False:
                           for item3 in environment_sprites:
                              items_overlap = checkItemsOverlap(item1,item3)
                              if items_overlap == True:
                                 ie_overlap = True
                                 if item1.type == "key" and item3.type == "box":
                                    ie_combine = True
                                    removeInventoryItem(item1)
                                    removeEnvironmentItem(item3)
                                    addToInventory(["secateur", "matches"])
                                    renpy.show_screen("inspectItem",["secateur", "matches"])
                                    characterSay(who ="You", what = ["This might be useful."], inspectItem = True)
                                    repositionInventoryItems()
                                    inventory_SM.redraw(0)
                                    environment_SM.redraw(0)
                                    renpy.restart_interaction()
                                    break
                                 elif item1.type == "secateur" and item3.type == "door-vines":
                                    ie_combine = True
                                    removeInventoryItem(item1)
                                    removeEnvironmentItem(item3)
                                    characterSay(who ="You", what = ["Door open"])
                                    inventory_SM.redraw(0)
                                    environment_SM.redraw(0)
                                    renpy.restart_interaction()
                                    break
                                 else:
                                    item1.x = item1.original_x
                                    item1.y = item1.original_y
                                    item1.zorder = 0
                                    characterSay(who ="You", what = ["Didn't work."])
                                    break
                        if i_combine == False and ie_combine == False:
                           item1.x = item1.original_x
                           item1.y = item1.original_y
                           item1.zorder = 0
      if str(event.type) == str(32768): #renpy.pygame_sdl2.MOUSEMOTION:
         mousepos = (x, y)
         if inventory_drag == False:
            for item in inventory_sprites:
               if item.visible == True:
                  if item.x<= x <= item.x + item.width and item.y <= y <= item.y + item.height:
                     renpy.show_screen("inventoryItemMenu", item = item)
                     renpy.restart_interaction()
                     break
      else:
         renpy.hide_screen("inventoryItemMenu")
         renpy.restart_interaction()

   def startDrag(item):
      global inventory_drag
      global item_dragged
      inventory_drag = True
      item_dragged = item.type
      inventory_SM.redraw(0)



   def environmentEvents(event,x,y,at):
      #characterSay(who = "You", what = ["event: "+ str(event.type)+ " x:" +str(x)+ " y: " + str(y)+" at:"+str(at)])
      if event.type == renpy.pygame_sdl2.MOUSEMOTION:
         for item in environment_sprites:
            if item.x<= x <= item.x + item.width and item.y <= y <= item.y + item.height:
               t = Transform(child = item.hover_image, zoom = 0.5)
               item.set_child(t)
               environment_SM.redraw(0)
            else:
               t = Transform(child = item.idle_image, zoom = 0.5)
               item.set_child(t)
               environment_SM.redraw(0)
      elif event.type == renpy.pygame_sdl2.MOUSEBUTTONUP:
         if event.button == 1:
            for item in environment_sprites:
               if i_overlap == False and ie_overlap == False:
                  if item.x<= x <= item.x + item.width and item.y <= y <= item.y + item.height:
                        if item.type == "key":
                              addToInventory(["key", "lantern", "key"])
                        elif item.type == "lantern":
                              addToInventory(["lantern"])
                        elif item.type == "box":
                              characterSay(who = "You", what = ["This box is locked."])
                        elif item.type == "door-vines":
                              characterSay(who = "You", what = ["I can't open the door."])
                        elif item.type == "chest-vines":
                              characterSay(who = "You", what = ["I can't open the chest."])
   def inventoryArrows(button):
      global inventory_lb_enabled
      global inventory_rb_enabled

      if len(inventory_sprites) > 7:
         citem = ""
         for i,item in enumerate(inventory_sprites):
            if button == "right" and inventory_rb_enabled == True:
               if inventory_sprites[-1].visible == False:
                  item.x -= item.width + inventory_slot_padding
                  citem = item
            elif button == "left" and inventory_lb_enabled == True:
               if inventory_sprites[0].visible == False:
                     reversed_index = (len(inventory_sprites) - 1 ) - i
                     inventory_sprites[reversed_index].x += item.width + inventory_slot_padding
                     citem = inventory_sprites[reversed_index]
            if citem != "" and (citem.x<inventory_first_slot_x or citem.x > (inventory_first_slot_x + (citem.width * 7)) + (inventory_slot_padding * 5)):
               setItemVisibility(item = citem, visible = False)
            elif citem != "":
               setItemVisibility(item = citem, visible = True)
         if inventory_sprites[-1].visible == True:
            inventory_rb_enabled = False
         else: 
            inventory_rb_enabled = True
         if inventory_sprites[0].visible == True:
            inventory_lb_enabled = False
         else: 
            inventory_lb_enabled = True
         
         if citem != "":
            inventory_SM.redraw(0)
            renpy.restart_interaction()



   def setItemVisibility(item, visible):
      if visible == False:
         item.visible = False
         t = Transform(child = item.item_image, zoom = 0.5, alpha = 0)
         item.set_child(t)
      else:
         item.visible = True
         t = Transform(child = item.item_image, zoom = 0.5, alpha = 100)
         item.set_child(t)
      inventory_SM.redraw(0)


   def characterSay(who,what, inspectItem = False):
      if isinstance(what, str):
         renpy.call_screen("characterSay", who=who, what = what)
      elif isinstance(what, list):
         global dialogue
         dialogue = {"who": who, "what": what}
         if inspectItem == False:
            renpy.show_screen("characterSay")
            renpy.restart_interaction()


   def addToInventory(items):
      
      for item in items:
         inventory_items.append(item)
         if item == "lantern":
            item_image = Image("items/inventory-lantern-unlit.png")
         else:
            item_image = Image("items/inventory-{}.png".format(item))

         t = Transform(child= item_image, zoom = 0.5)
         inventory_sprites.append(inventory_SM.create(t))
         inventory_sprites[-1].width = inventory_slot_size[0]
         inventory_sprites[-1].height = inventory_slot_size[1]
         inventory_sprites[-1].type = item
         inventory_sprites[-1].item_image = item_image
         inventory_sprites[-1].y = 608
         inventory_sprites[-1].original_y = 608
         inventory_sprites[-1].original_x = 0
         inventory_sprites[-1].visible = True

         if item == "lantern":
               inventory_sprites[-1].state = "unlit"
         else:
               inventory_sprites[-1].state = "default"

         for envitem in environment_sprites:
            if envitem.type == item:
               removeEnvironmentItem(item = envitem)
               break

         repositionInventoryItems()
         inventory_SM.redraw(0)
         environment_SM.redraw(0)
         renpy.restart_interaction()

   def removeEnvironmentItem(item):
      item.destroy()
      environment_sprites.pop(environment_sprites.index(item))
      environment_items.pop(environment_items.index(item.type))

   def removeInventoryItem(item):
      item.destroy()
      inventory_sprites.pop(inventory_sprites.index(item))
      inventory_items.pop(inventory_items.index(item.type))
      
      repositionInventoryItems()

   def repositionInventoryItems():
      global inventory_lb_enabled
      global inventory_rb_enabled
      #global inventory_lv_enabled
      for i,item in enumerate(inventory_sprites):
         if i == 0:
            item.x = inventory_first_slot_x
            inventory_sprites[-1].original_x = item.x
         else: 
            item.x = (inventory_first_slot_x + inventory_slot_size[0] * i) + (inventory_slot_padding * i)
            inventory_sprites[-1].original_x = item.x
         if item.x<inventory_first_slot_x or item.x > (inventory_first_slot_x + (item.width * 7)) + (inventory_slot_padding * 5):
            setItemVisibility(item = item, visible = False)
         elif item != "":
            setItemVisibility(item = item, visible = True)

      if len(inventory_sprites) > 0:
         if inventory_sprites[-1].visible == True:
            inventory_rb_enabled = False
         else: 
            inventory_rb_enabled = True
         if inventory_sprites[0].visible == True:
            inventory_lb_enabled = False
         else: 
            inventory_lb_enabled = True
         

   def checkItemsOverlap(item1, item2):
      if abs((item1.x + item1.width/2)- (item2.x + item2.width/2)) * 2 < item1.width + item2.width and abs((item1.y + item1.height/2)-(item2.y+ item2.height/2))*2 < item1.height + item2.height and item1.type != item2.type:
         return True
      else:
         return False
