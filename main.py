import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://www.youthall.com/tr/talent-programs/?page=1&order=6"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER_EMAILS = os.getenv("RECEIVER_EMAILS").split(",")

def send_email(subject, body):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = ", ".join(RECEIVER_EMAILS)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, RECEIVER_EMAILS, msg.as_string())
        server.quit()
        print("Mail is sent!")
    except Exception as e:
        print(f"An error occured while sending mail {e}")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    job_listings = soup.find_all("div", class_="y-talent box_hover border-line-light-blue shadow-light")
    
    email_body = "New Internship Programs:\n\n"
    
    for job in job_listings:
        title_tag = job.find("div", class_="y-talent_title")
        title = title_tag.label.text.strip() if title_tag else "Unknown"
        
        company_tag = job.find("div", class_="y-talent_company_name")
        company = company_tag.span.text.strip() if company_tag else "Unknown"
        
        link_tag = job.find("a", href=True)
        link = "https://www.youthall.com" + link_tag["href"] if link_tag else "Unknown"
        
        email_body += f"Job title: {title}\nCompany: {company}\nLink: {link}\n\n"
    
    if job_listings:
        send_email("Youthall New Internship Programs", email_body)
    else:
        print("No new listings found.")
else:
    print("Page could not be loaded!", response.status_code)
