import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import time

# Tour data (in this case, an example of scheduled tours)
tours = [
    {
        'tour_name': 'Campus Tour A',
        'date': '2024-11-22',
        'time': '10:00 AM',
        'location': 'Main Campus',
        'participants': ['Alice', 'Bob'],
    },
    {
        'tour_name': 'Library Tour',
        'date': '2024-11-22',
        'time': '2:00 PM',
        'location': 'Library',
        'participants': ['Charlie', 'David'],
    },
]

# SMTP email settings (for sending email reminders)
sender_email = "your_email@example.com"
sender_password = "your_email_password"  # Use app password if 2FA is enabled
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Function to send an email reminder
def send_email(subject, body, recipient_email):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print(f"Reminder sent to {recipient_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

# Function to send SMS reminder using Twilio
def send_sms(message, to_phone):
    from twilio.rest import Client
    
    # Twilio credentials (sign up at https://www.twilio.com/)
    account_sid = 'your_twilio_account_sid'
    auth_token = 'your_twilio_auth_token'
    twilio_number = 'your_twilio_phone_number'
    
    client = Client(account_sid, auth_token)
    
    try:
        message = client.messages.create(
            body=message,
            from_=twilio_number,
            to=to_phone
        )
        print(f"SMS sent to {to_phone}")
    except Exception as e:
        print(f"Error sending SMS: {e}")

# Function to check if the reminder needs to be sent
def check_and_send_reminders(tours):
    current_time = datetime.now()
    
    for tour in tours:
        # Parse the tour date and time
        tour_datetime_str = f"{tour['date']} {tour['time']}"
        tour_datetime = datetime.strptime(tour_datetime_str, "%Y-%m-%d %I:%M %p")

        # Calculate the time difference between now and the tour
        time_difference = tour_datetime - current_time

        # If the tour is in 24 hours or less, send a reminder
        if time_difference <= timedelta(hours=24) and time_difference > timedelta(hours=0):
            subject = f"Reminder: {tour['tour_name']} at {tour['time']}"
            body = f"Dear student ambassador,\n\nThis is a reminder that your tour '{tour['tour_name']}' is scheduled for {tour['date']} at {tour['time']} at {tour['location']}.\n\nPlease be prepared and arrive on time."
            
            # Send reminders to all participants via email and/or SMS
            for participant in tour['participants']:
                # Replace this with the participant's actual email or phone number
                participant_email = f"{participant.lower()}@example.com"
                participant_phone = f"+1234567890"  # Replace with actual phone number
                
                # Send email and SMS reminders
                send_email(subject, body, participant_email)
                send_sms(body, participant_phone)

# Main function to run the reminder check periodically
def main():
    while True:
        print("Checking for tours with upcoming reminders...")
        check_and_send_reminders(tours)
        
        # Sleep for an hour before checking again
        time.sleep(3600)  # Sleep for 1 hour

if __name__ == "__main__":
    main()
