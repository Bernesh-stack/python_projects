import pandas as pd
import datetime as dt
import random
import smtplib

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
today_date = dt.datetime.now().day
today_month = dt.datetime.now().month

Your_email = "berneshshagi123@gmail.com"
Your_pass = "rvox pujg hpiq wxcc"

data = pd.read_csv("birthdays.csv")

for _, row in data.iterrows():
    if row["month"] == today_month and row["day"] == today_date:
        name_person = row["name"]
        email_person = row["email"]
        re = random.randint(1, 3)

        with open(f"letter_templates/letter_{re}.txt") as datas:
            content = datas.read()
            contents = content.replace("name", name_person)

        try:
            # Corrected SMTP server and port
            connection = smtplib.SMTP("smtp.gmail.com", port=587)
            connection.starttls()
            connection.login(Your_email, Your_pass)
            connection.sendmail(from_addr=Your_email, to_addrs=email_person, msg=contents)
            print(f"Email sent successfully to {email_person}")

        except smtplib.SMTPException as e:
            # Handle connection or sending failure
            print(f"Failed to send email to {email_person}. Error: {e}")

        finally:
            connection.quit()  # Properly closing the connection
