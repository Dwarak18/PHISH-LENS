import random
import string

def generate_phishing_subject():
    subjects = [
        "Urgent: Your account has been compromised!",
        "Action Required: Verify your account information",
        "Important: Update your payment details",
        "Alert: Suspicious login detected",
        "Congratulations! You've won a prize",
        "Your package delivery is delayed",
        "Security Alert: Password reset needed",
        "Verify your identity to avoid suspension",
        "Your invoice is attached",
        "Confirm your subscription now"
    ]
    return random.choice(subjects)

def generate_phishing_body():
    templates = [
        "Dear user,\n\nWe detected unusual activity on your account. Please click the link below to verify your information:\n{url}\n\nThank you,\nSupport Team",
        "Hello,\n\nYour payment has failed. Please update your payment details here:\n{url}\n\nBest regards,\nBilling Department",
        "Hi,\n\nYou have won a prize! Claim it now by visiting:\n{url}\n\nCheers,\nRewards Team",
        "Dear customer,\n\nYour package delivery is delayed. Track your package here:\n{url}\n\nThank you for your patience,\nDelivery Service",
        "Attention,\n\nYour account will be suspended unless you verify your identity here:\n{url}\n\nRegards,\nAccount Security"
    ]
    return random.choice(templates)

def generate_url():
    chars = string.ascii_lowercase + string.digits
    domain = ''.join(random.choices(chars, k=random.randint(5, 10)))
    tld = random.choice(['.com', '.net', '.org', '.info', '.biz'])
    return f"http://{domain}{tld}"

def generate_phishing_email():
    subject = generate_phishing_subject()
    body_template = generate_phishing_body()
    url = generate_url()
    body = body_template.format(url=url)
    return subject, body

# Generate 10,000 phishing emails
phishing_emails = [generate_phishing_email() for _ in range(10000)]

# Save to CSV
import csv
filename = "phishing_emails_dataset.csv"
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Body"])
    writer.writerows(phishing_emails)

filename
