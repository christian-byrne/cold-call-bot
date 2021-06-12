"""
Logging activity. 
Functions can be called to check intervals for various mailing schemes/randomization strategies.
"""


from time import time, localtime
import persistent_objects as persistent


def scheduled_update(artist, check_interval=False):
    """ Check history logs to check last time an email was sent to address.
        Returns the days since last email unless check_interval is specified. 

        Params:
            artist: (str) as it appears in the contact_list object
            check_interval: (int) checks if the last email was sent long than interval (in days), 
                            if it was, returns True; otherwise, returns False
    """

    history = persistent.load_obj("history")

    if artist not in history.keys():
        if check_interval: return False
        else: return 100000
 
    last_yrday = history[artist] 
    curr_yrday = curr_time()
    if curr_yrday < last_yrday:
        curr_yrday += 365

    if check_interval:
        if curr_yrday - last_yrday >= check_interval:
            return True
        return False
    else:
        return curr_yrday - last_yrday


def update_history(artist):
    log = persistent.load_obj("history")
    log[artist] = curr_time()
    persistent.save_obj(log, "history")


def curr_time():
    return localtime(time())[7]
