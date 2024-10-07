import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

# Gmail SMTP settings
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = input("Enter your Email: ")
To=input("To: ")
password = getpass.getpass(prompt="Emter your App Password: ")  

# Create the MIMEMultipart object
message = MIMEMultipart("alternative")
message["Subject"] = input("Enter Email Subject: ")
message["From"] = sender_email
message["To"] = To     # asingh1@kol.amity.edu
# To2="skumar2@kol.amity.edu"
# HTML content
with open("index.html","r") as f:
    html_content=f.read()

# Attach the HTML content to the email
part = MIMEText(html_content, "html")
message.attach(part)

# Connect to the Gmail SMTP server and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to a secure one
    server.login(sender_email, password)
    server.sendmail(sender_email, [To], message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()
