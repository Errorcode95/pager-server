import win32com.client as win32
import time
import subprocess

def receive_emails():
    outlook = win32.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # 6 represents the Inbox folder
    messages = inbox.Items
    messages.Sort("[ReceivedTime]", True)  # Sort by received time in descending order
    subject = ""
    for msg in messages:
        subject = msg.Subject
        print("Received email with subject:", subject)
        break  # Only process the latest email
    return subject

def transmit_pocsag(subject):
    if subject:
        # Remove any non-ASCII characters from the subject
        subject = ''.join(filter(lambda x: x in string.printable, subject))
        subprocess.run(sudo echo -e "1016269:AWOOOOO" | sudo ./rpitx/pocsag -f "152175000" -r 512 -t 1)

# Main program
while True:
    email_subject = receive_emails()
    transmit_pocsag(email_subject)
    time.sleep(60)  # Wait for 1 minute before checking emails again
