import datetime as dt
import random
import smtplib
import datetime as dt  # Corrected datetime import


weeks = dt.datetime.now()
print(weeks.day)

# Read the quotes file and select a random line
with open("quotes.txt", mode="r", encoding="utf-8") as file:
    lines = file.readlines()

random_index = random.randint(0, len(lines) - 1)
second_line = lines[random_index].strip()

# Email Credentials
Your_email = "berneshshagi123@gmail.com"
Your_pass = "rvox pujg hpiq wxcc"

# Format the message properly
subject = "Your Daily Quote!"
body = f"Subject: {subject}\n\n{second_line}"

# Send Email
try:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()  # Secure connection
    connection.login(user=Your_email, password=Your_pass)
    connection.sendmail(from_addr=Your_email, to_addrs=Your_email, msg=body.encode('utf-8'))
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    connection.close()





