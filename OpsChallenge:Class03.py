import os
import platform
import subprocess
import time
from datetime import datetime

def ping_host(ip):
    """
    Function to send an ICMP packet (ping) to the specified IP address.
    """
    try:
        # Done choose the appropriate ping command based on the operating system
        if platform.system().lower() == "windows":
            result = subprocess.run(['ping', '-n', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=2)
        else:
            result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=2)

        # Done check if the ping was successful (response code 0)
        if result.returncode == 0:
            return True
        else:
            return False

    except subprocess.TimeoutExpired:
        return False

if __name__ == "__main__":
    # Done specify the IP address to test (replace with your target IP)
    target_ip = "8.8.8.8"

    while True:
        # Done get the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

        # Done perform the ping test and get the result
        is_host_up = ping_host(target_ip)

        # Done determine the status based on the ping result
        status = "Network Active" if is_host_up else "Network Inactive"

        # Done print the result along with the timestamp and destination IP
        print(f"{timestamp} {status} to {target_ip}")

        # Done wait for 2 seconds before the next iteration
        time.sleep(2)
      
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def exit(message='Thank You For Using My Script'):
    print(message)
    sys.exit()

if __name__ == "__main__":
    try:
        # Get user email and password for notifications
        sender_email = input("Enter your email address: ")
        if not sender_email:
            sender_email = 'youremail.com'
        sender_password = input("Enter your email password (App Password for Gmail): ")
        if not sender_password:
            sender_password = "yourpassword from the app in gmail (not login passowrd))"
        receiver_email = input("Enter the administrator's email address: ")

        # Compose the email
        subject = "Test Notification"
        body = "This is a test email notification from your Python script."

        # Send the email notification
        send_email(sender_email, sender_password, receiver_email, subject, body)

        print("Email sent successfully.")
    except KeyboardInterrupt:
        exit("\nExiting the script")
