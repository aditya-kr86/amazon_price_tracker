import requests
import smtplib
from bs4 import BeautifulSoup
PRODUCT_SITE = "PRODUCT_SITE"
TARGET_PRICE = TARGET_PRICE
MY_EMAIL = "EMAIL"
MY_PASSWORD = "PASSWORD"
recipient_email = "recipient_email"

response = requests.get(PRODUCT_SITE)
product_web = response.text
# print(product_web)

soup = BeautifulSoup(product_web, "html.parser")
# print(soup.prettify())

price = soup.find(name="span", class_="a-price-fraction").getText()
# print(price)
if int(price) <= TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=recipient_email,
            msg=f"Subject:Low Price Alert!\n\nThe Product You are Wishing To be Buy is\n Available at Just {price}"
        )
    if connection:
        try:
            connection.quit()  # Close the connection
        except smtplib.SMTPServerDisconnected:
            print("The connection was already closed.")
