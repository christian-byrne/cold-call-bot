import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# initialize server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()


# Gmail Sign In
gmail_sender = "chrbyrne96@gmail.com"
gmail_passwd = "panhzgtiapjqlpmx" # app password
server.login(gmail_sender, gmail_passwd)

# recipient
recipient = "chrbyrne96@gmail.com"

# email headers
message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = gmail_sender
message["To"] = recipient

# Create the plain-text and HTML version of your message
backup_text = "backup if recipient cant render HTML"
html = open("letterhead-template.html", "r").read()


# recipient params
inline_url = "https://trevor-reznik.github.io/guides/email-template/1.mp3"
external_url = "https://bymyself.life/niq-venus.html"
recipient_name = "{test name}"
artist_name = "{artist test name}"

replace_dict = {
    "$ARTISTNAME" : recipient,
    "$MUSICLINK" : inline_url,
    "$EXTERNALLINKL" : external_url,
    "$RECIPIENTNAME" : recipient_name,
    "$ARTISTNAME" : artist_name
}

for key, new in replace_dict.items():
    html = html.replace(key, new)

# Turn these into plain/html MIMEText objects
part1 = MIMEText(backup_text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# send email
try:
    server.sendmail(gmail_sender, [recipient], message.as_string())
    print ("[+] email successful sent to " + recipient)
except:
    print ("[-] error sending message to " + recipient)

# terminate server
server.quit()