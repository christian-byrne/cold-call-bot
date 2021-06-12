# CHANGE THESE VALUES AS NECESSARY
mygmailaccesstoapps="ijecqbdtvchnozek"
myactualgmail="niqvenus@gmail.com"
testing_mode_emails = {
    "me" : "niqvenus@gmail.com"
}


# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import persistent_objects as persistent
from term_gui import make_header 
import history


def send_emails(contacts, test_mode=True, interval_check=False):
    """ Sends emails

        Args:
            contacts : (dict) contact list object (artist, email pairs)
            test_mode : (bool) if True, only sends emails to test emails 
            interval_check : [optional] (int) if specified, only sends emails to 
            addresses that haven't been contacted in that many days or more.
    """

    if test_mode:
        contacts = testing_mode_emails

    # initialize server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(myactualgmail, mygmailaccesstoapps)

    for artist, email in contacts.items():

        if interval_check:
            if not history.scheduled_update(artist, check_interval=int(interval_check)):
                print (f"[-] email send to {artist} too recently. skipping for now")
                continue

        # duplicate names that are just the same name but with '2' at the end
        if artist[-1] == "2":
            artist = artist[:-1]

        # email headers
        message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = myactualgmail
        message["To"] = email

        # Create the plain-text and HTML version of your message
        backup_text = "backup if recipient cant render HTML"
        html = open("emailtemplateforfullsend.html", "r").read()

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(backup_text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # send email
        errors = {}
        try:
            server.sendmail(myactualgmail, [email], message.as_string())
            print (f"[+] email successfully sent to {artist}")
            history.update_history(artist)

        except:
            print (f"[-] error sending message to {artist}")
            errors[artist] = email

    # terminate server
    server.quit()
    log_errors(errors)


def log_errors(errors):
    print(
        make_header(
            60,
            "Errors Sending Message to the Following Contacts:",
            centered=True,
            character="-",
            boxed=True
        )
    )
    for artist, email in errors.items():
        print(
            "Artist:   ",
            artist,
            "\nEmail:    ",
            email,
            "\n"
        )


def main():
    contact_list = persistent.load_obj("contact_list")


