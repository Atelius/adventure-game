transform chest_transform:
   zoom 0.5
   anchor (0.5, 0.5)
   align (0.5, 0.7)
   subpixel True
   on hover:
      easein 1.0 zoom 0.51
   on idle:
      easein 1.0 zoom 0.5

transform chest_unlocked_anim:
   zoom 0.5
   alpha 0.0
   parallel:
      easein 3.0 zoom 0.7
   parallel:
      easein 2.0 alpha 1.0