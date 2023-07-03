screen characterSay(who = None, what = None):
    modal True
    zorder 60
    style_prefix "say"

    window:
        id "window"
        window:
            padding (20,20)
            id "namebox"
            style "namebox"
            if who is not None:
                text who id "who"   
            else:
                text dialogue["who"]
        
        
        if what is not None:
            text what id "what" xpos 0.25 ypos 0.4 xanchor 0.0
        else:
            text dialogue["what"][0] xpos 0.25 ypos 0.4 xanchor 0.0
        
    button:
        xfill True
        yfill True
        if what is None:
            action If(len(dialogue["what"])>1, true = RemoveFromSet(dialogue["what"],dialogue["what"][0]),false = [Hide("characterSay"), SetVariable("dialogue",{})])
        else:
            action Return(True)

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
