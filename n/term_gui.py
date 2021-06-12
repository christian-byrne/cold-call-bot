"""
Make headers for easier reading of script output at command line
"""


def make_header(gui_length, text, character="─", centered=False, tiers=3, boxed=False, auto_capitalize=True, style="triple bar", middle_leader=3):
    gui_length = int(gui_length)
    middle_leader = int(middle_leader)
    tiers = int(tiers)
    if auto_capitalize:
        text = str(text).upper()
    else:
        text = str(text)
    character = str(character)[0]
    ret = ""

    if style == "triple bar" or style:

        # Top Tier
        if tiers > 1:
            ret+= "\n\n " + character * gui_length + "\n"
            if tiers > 3:
                for _ in range( (tiers - 3) // 2 ):
                    ret+= " " + character * gui_length + "\n"
        else:
            ret += "\n\n"

        # Middle Tier
        if boxed:
            mid_char = " "
        else:
            mid_char = character
        ret = ret + " |" if boxed else ret + " "

        if not centered:
            ret += mid_char * int(middle_leader) + \
                " " + str(text).strip() + " " + \
                    mid_char * ( (gui_length - (2 + int(middle_leader))) - len(text) )
        if centered:
            if boxed:
                fill = ( gui_length - ( len(text) + 4 ) ) // 2
            if not boxed:
                 fill = ( gui_length - ( len(text) + 2 ) ) // 2
            ret += ( mid_char * fill ) + " " + str(text).strip() + " " + ( mid_char * fill )
            if ( gui_length - (len(text) + 2) ) % 2:
                ret += mid_char 
        
        ret = ret[:-2] + "|\n" if boxed and not centered else ret + "|\n" if boxed and centered else ret + "\n"

        # Bottom Tier
        if tiers > 2:
            ret += " " + character * gui_length + "\n"
            if tiers > 3:
                for _ in range( ((tiers - 3) // 2) + (tiers - 3) % 2 ):
                    ret+= " " + character * gui_length + "\n"
            ret += "\n"
        else:
            ret += "\n\n"
    
    return ret