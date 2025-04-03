import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv() #.env dosyasını yükle

# Youthall Talent Programs Sayfası URL'si
url = "https://www.youthall.com/tr/talent-programs/?page=1&order=6"

# HTTP isteği gönder
headers = {"User-Agent": "Mozilla/5.0"}  # Bot olarak algılanmamak için
response = requests.get(url, headers=headers)

# E-posta bilgileri
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER_EMAILS = os.getenv("RECEIVER_EMAILS").split(",") # E-posta listesini diziye çevir

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
        print("E-posta başarıyla gönderildi!")
    except Exception as e:
        print(f"E-posta gönderilirken hata oluştu: {e}")

# Yanıt başarılı mı kontrol et
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    job_listings = soup.find_all("div", class_="y-talent box_hover border-line-light-blue shadow-light")
    
    email_body = "Yeni Staj Programları:\n\n"
    
    for job in job_listings:
        title_tag = job.find("div", class_="y-talent_title")
        title = title_tag.label.text.strip() if title_tag else "Bilinmiyor"
        
        company_tag = job.find("div", class_="y-talent_company_name")
        company = company_tag.span.text.strip() if company_tag else "Bilinmiyor"
        
        link_tag = job.find("a", href=True)
        link = "https://www.youthall.com" + link_tag["href"] if link_tag else "Bilinmiyor"
        
        email_body += f"İlan: {title}\nŞirket: {company}\nBağlantı: {link}\n\n"
    
    if job_listings:
        send_email("Youthall Yeni Staj Programları", email_body)
    else:
        print("Yeni ilan bulunamadı.")
else:
    print("Sayfa yüklenemedi!", response.status_code)
