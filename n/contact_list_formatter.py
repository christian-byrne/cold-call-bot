
import persistent_objects as persistent


def parse_contacts(input_file="backups/contact-list.txt"):
    """
    Parses raw email list assuming it is formatted by having an artist name and
    email address on newlines such that each artist/email combo is alotted 2 lines.
    """
    illegal_characters = ["\n", ":", "'", '"', "*", " ", "-"]
    contacts = {}
    raw = open(input_file, "r").readlines()
    
    i = 0
    while i < len(raw) -2 : 
        if raw[i].strip():
            artist, email = raw[i], raw[i+1]
            for _ in illegal_characters:
                artist = artist.replace(_,"")
                email = email.replace(_,"") 
            contacts[artist] = email
            i += 2
        else:
            i += 1
    
    persistent.save_obj(contacts, "contact_list")
    return contacts


def write_sorted_txt(contacts, filename="backups/contact-list.txt"):
    """
    Write a backup text file of contact list sorted by artist name.

    Args:
        contacts: (dict) dictionary with artist name, email pairs
        filename: (str) name of output file to write to
    """
    x = open(filename, "w")
    for name, email in sorted(contacts.items()):
        x.write(name + "\n")
        x.write(email + "\n")
    x.close()


if __name__ == "__main__":
    contacts = parse_contacts()
