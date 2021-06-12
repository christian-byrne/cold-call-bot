#
# ───────────────────────────────────────────────── USING PERSISTENT OBJECTS ─────
#
import pickle
from term_gui import make_header


def save_obj(obj, name):
    """
    Saves an object to a file for persistent use between
    program instances. 
    
    Params:
        obj     : the object to save
        name    : the name of the file to write to/create
    """

    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    """
    Returns an object that was previously saved with the
    save_obj() function. 
    
    This Program's Stored Objects:
        order       : the dictionary of orders and floor/ceiling prices
        cashed_out  : the IDs of cashed out orders

    Params:
        name    : the name of the object/file that was stored previously
    """

    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


def print_obj(name):
    """
    Prints an object that was previously saved with the
    save_obj() function to stdout.
    
    Params:
        name    : the name of the object/file that was stored previously
    """

    obj = load_obj(name)
    
    print(
        make_header(
            60,
            "Contacts List",
            boxed=True,
            character="-",
            centered=True
        )
    )
    for k, v in obj.items():
        print(
            "Artist:   ",
            k,
            "\nEmail:    ",
            v,
            "\n"
        )

    total = len(list(obj.keys()))
    print(
        make_header(
            60,
            "Total: " + str(total),
            boxed=True,
            character="-",
            centered=True
        )
    )