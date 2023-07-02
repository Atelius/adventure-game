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
      chest_unlock_tries = 2
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
      pass
   def inventoryEvents(event,x,y,at):
      pass
   def environmentEvents(event,x,y,at):
      pass
   def inventoryArrows(button):
      pass