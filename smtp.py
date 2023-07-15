# EMAILS TEXT SENDER USING PYTHON  BY RCHAMEXE

import smtplib
import ssl

# Setup port number and servr name

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

email_from = "sender@gmail.com"   # Here you need to put the email sender 
email_to = "receiver@gmail.com"   # Here you need to put the email receiver

password = "" # Here you need to put your app password from your gmail ( don't forget to active 2nd verification on )
# NOTE : if you don't know how to get the app password from your gmail go search about it on youtube or just go on my facebook profil I'will explain it www.facebook.com/3LIIX1
# Or just watch the video : https://video.xx.fbcdn.net/v/t42.1790-2/359570867_827805811784701_6859331017310432078_n.mp4?_nc_cat=109&ccb=1-7&_nc_sid=985c63&efg=eyJ2ZW5jb2RlX3RhZyI6InN2ZV9zZCJ9&_nc_ohc=xINTQeVGb48AX9nMObk&_nc_rml=0&_nc_ht=scontent.frba2-2.fna&oh=00_AfA1JyLsftcy0HqPyyt2E2FZeGqers2vOoeMJ72VVYEXfw&oe=64B71F64




# content of message

message = "follow me on twitter @RCHAMEXE"

# Create context
simple_email_context = ssl.create_default_context()


try:
    # Connect to the server
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from, password)
    print("Connected to server :-)")
    
    # Send the actual email
    print()
    print(f"Sending email to - {email_to}")
    TIE_server.sendmail(email_from, email_to, message)
    print(f"Email successfully sent to - {email_to}")

# If there's an error, print it out
except Exception as e:
    print(e)

# Close the port
finally:
    TIE_server.quit()
