# Youthall Staj Botu

Bu proje, Youthall platformundaki yeni staj ilanlarını otomatik olarak kontrol eder ve belirlenen e-posta adreslerine yeni ilanları içeren bir e-posta gönderir.

## Özellikler
- Youthall Talent Programs sayfasındaki ilanları tarar.
- İlan başlıklarını, şirket isimlerini ve ilan bağlantılarını çeker.
- Kullanıcılara belirlenen aralıklarla otomatik e-posta gönderir.
- PythonAnywhere veya Windows Görev Zamanlayıcı ile otomatikleştirilebilir.

## Gereksinimler
Bu projenin çalışması için aşağıdaki Python kütüphanelerinin yüklenmiş olması gerekir:

```sh
pip install requests beautifulsoup4 smtplib
```

Ayrıca, bir Gmail hesabı üzerinden e-posta göndermek için **Gmail Uygulama Şifresi** oluşturulmalıdır.

## Kullanım

1. **Config Ayarları:**
   - `EMAIL_ADDRESS` ve `EMAIL_PASSWORD` değişkenlerini kendi bilgilerinize göre düzenleyin.
   - `RECEIVER_EMAILS` listesine e-posta gönderilecek adresleri ekleyin.
2. **Script'i Çalıştırma:**
   - PythonAnywhere veya Windows Görev Zamanlayıcı kullanarak belirlenen aralıklarla çalıştırabilirsiniz.

---

# Youthall Internship Bot

This project automatically checks new internship postings on the Youthall platform and sends an email containing new listings to predefined recipients.

## Features
- Scrapes internship listings from the Youthall Talent Programs page.
- Extracts job titles, company names, and job links.
- Sends automatic email notifications at specified intervals.
- Can be automated using PythonAnywhere or Windows Task Scheduler.

## Requirements
To run this project, ensure the following Python libraries are installed:

```sh
pip install requests beautifulsoup4 smtplib
```

Additionally, a **Gmail App Password** is required for email sending.

## Usage

1. **Configure Settings:**
   - Update `EMAIL_ADDRESS` and `EMAIL_PASSWORD` with your credentials.
   - Add recipient emails to the `RECEIVER_EMAILS` list.
2. **Run the Script:**
   - Use PythonAnywhere or Windows Task Scheduler to run the script at desired intervals.

