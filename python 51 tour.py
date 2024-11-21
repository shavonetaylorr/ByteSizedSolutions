import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Example user data (name, role, email)
users = {
    "manager": [
        {"name": "John Doe", "email": "johndoe@example.com"},
        {"name": "Jane Smith", "email": "janesmith@example.com"}
    ],
    "Ambassador": [
        {"name": "Alice Brown", "email": "alice.brown@example.com"},
        {"name": "Bob White", "email": "bob.white@example.com"}
    ],
    "support": [
        {"name": "Charlie Green", "email": "charlie.green@example.com"}
    ] 
}

# Function to send email alerts
def send_alert(subject, body, recipients):
    # Setup email details
    sender_email = "your_email@example.com"  # Replace with your email
    sender_password = "your_email_password"  # Replace with your email password

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Setup the SMTP server
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            for recipient in recipients:
                msg['To'] = recipient['email']
                server.sendmail(sender_email, recipient['email'], msg.as_string())
            print(f"Alert sent to {len(recipients)} recipients.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Function to manually send alerts to roles
def notify_roles(role, subject, body):
    if role in users:
        send_alert(subject, body, users[role])
    else:
        print("Invalid role. Please choose from 'manager', 'tour_guide', or 'support'.")

# Example usage
if __name__ == "__main__":
    role = input("Enter the role to notify (manager, ambassador, support): ").lower()
    subject = "Important Update on Upcoming Tours"
    body = "Dear team, there has been an important update regarding the upcoming tours. Please review the schedule and act accordingly."
    notify_roles(role, subject, body)

