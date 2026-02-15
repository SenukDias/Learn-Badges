#!/usr/bin/env python3
"""
Send email with the digital badge attached.
Supports multiple email providers: SendGrid, Resend, Gmail SMTP.
"""

import argparse
import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def send_email_sendgrid(to_email, name, badge_path, api_key, from_email, from_name):
    """Send email using SendGrid API."""
    try:
        import requests
        import base64
        
        # Read badge file
        with open(badge_path, 'rb') as f:
            badge_data = base64.b64encode(f.read()).decode()
        
        badge_filename = os.path.basename(badge_path)
        
        # Prepare email
        email_data = {
            "personalizations": [{
                "to": [{"email": to_email, "name": name}],
                "subject": "🎉 Your Microsoft Learn AI Skills Challenge Badge!"
            }],
            "from": {"email": from_email, "name": from_name},
            "content": [{
                "type": "text/html",
                "value": f"""
                <html>
                <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                    <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                        <h1 style="color: #2962FF;">🎉 Congratulations, {name}!</h1>
                        
                        <p>You've successfully completed the <strong>Microsoft Learn AI Skills Challenge</strong>!</p>
                        
                        <p>Your personalized digital badge is attached to this email. You can:</p>
                        <ul>
                            <li>Share it on social media</li>
                            <li>Add it to your LinkedIn profile</li>
                            <li>Include it in your portfolio</li>
                            <li>Display it on your personal website</li>
                        </ul>
                        
                        <p>You've also been added to our <a href="https://github.com/SenukDias/Learn-Badges/blob/main/HALL_OF_FAME.md">Hall of Fame</a>!</p>
                        
                        <p style="margin-top: 30px;">
                            <strong>Keep learning and growing! 🚀</strong>
                        </p>
                        
                        <hr style="margin: 30px 0; border: none; border-top: 1px solid #eee;">
                        
                        <p style="font-size: 12px; color: #666;">
                            This badge was issued by the Learn-Badges automation system.<br>
                            If you have any questions, please visit our <a href="https://github.com/SenukDias/Learn-Badges">GitHub repository</a>.
                        </p>
                    </div>
                </body>
                </html>
                """
            }],
            "attachments": [{
                "content": badge_data,
                "filename": badge_filename,
                "type": "image/png",
                "disposition": "attachment"
            }]
        }
        
        # Send email
        response = requests.post(
            "https://api.sendgrid.com/v3/mail/send",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json=email_data
        )
        
        if response.status_code == 202:
            print(f"✅ Email sent successfully via SendGrid to {to_email}")
            return True
        else:
            print(f"❌ SendGrid error: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error sending email via SendGrid: {e}")
        return False


def send_email_resend(to_email, name, badge_path, api_key, from_email, from_name):
    """Send email using Resend API."""
    try:
        import requests
        import base64
        
        # Read badge file
        with open(badge_path, 'rb') as f:
            badge_data = base64.b64encode(f.read()).decode()
        
        badge_filename = os.path.basename(badge_path)
        
        # Prepare email
        email_data = {
            "from": f"{from_name} <{from_email}>",
            "to": [to_email],
            "subject": "🎉 Your Microsoft Learn AI Skills Challenge Badge!",
            "html": f"""
            <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                    <h1 style="color: #2962FF;">🎉 Congratulations, {name}!</h1>
                    
                    <p>You've successfully completed the <strong>Microsoft Learn AI Skills Challenge</strong>!</p>
                    
                    <p>Your personalized digital badge is attached to this email. You can:</p>
                    <ul>
                        <li>Share it on social media</li>
                        <li>Add it to your LinkedIn profile</li>
                        <li>Include it in your portfolio</li>
                        <li>Display it on your personal website</li>
                    </ul>
                    
                    <p>You've also been added to our <a href="https://github.com/SenukDias/Learn-Badges/blob/main/HALL_OF_FAME.md">Hall of Fame</a>!</p>
                    
                    <p style="margin-top: 30px;">
                        <strong>Keep learning and growing! 🚀</strong>
                    </p>
                    
                    <hr style="margin: 30px 0; border: none; border-top: 1px solid #eee;">
                    
                    <p style="font-size: 12px; color: #666;">
                        This badge was issued by the Learn-Badges automation system.<br>
                        If you have any questions, please visit our <a href="https://github.com/SenukDias/Learn-Badges">GitHub repository</a>.
                    </p>
                </div>
            </body>
            </html>
            """,
            "attachments": [{
                "filename": badge_filename,
                "content": badge_data
            }]
        }
        
        # Send email
        response = requests.post(
            "https://api.resend.com/emails",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json=email_data
        )
        
        if response.status_code in [200, 201]:
            print(f"✅ Email sent successfully via Resend to {to_email}")
            return True
        else:
            print(f"❌ Resend error: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error sending email via Resend: {e}")
        return False


def send_email_gmail(to_email, name, badge_path, gmail_user, gmail_password, from_name):
    """Send email using Gmail SMTP."""
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = f"{from_name} <{gmail_user}>"
        msg['To'] = to_email
        msg['Subject'] = "🎉 Your Microsoft Learn AI Skills Challenge Badge!"
        
        # HTML body
        html_body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                <h1 style="color: #2962FF;">🎉 Congratulations, {name}!</h1>
                
                <p>You've successfully completed the <strong>Microsoft Learn AI Skills Challenge</strong>!</p>
                
                <p>Your personalized digital badge is attached to this email. You can:</p>
                <ul>
                    <li>Share it on social media</li>
                    <li>Add it to your LinkedIn profile</li>
                    <li>Include it in your portfolio</li>
                    <li>Display it on your personal website</li>
                </ul>
                
                <p>You've also been added to our <a href="https://github.com/SenukDias/Learn-Badges/blob/main/HALL_OF_FAME.md">Hall of Fame</a>!</p>
                
                <p style="margin-top: 30px;">
                    <strong>Keep learning and growing! 🚀</strong>
                </p>
                
                <hr style="margin: 30px 0; border: none; border-top: 1px solid #eee;">
                
                <p style="font-size: 12px; color: #666;">
                    This badge was issued by the Learn-Badges automation system.<br>
                    If you have any questions, please visit our <a href="https://github.com/SenukDias/Learn-Badges">GitHub repository</a>.
                </p>
            </div>
        </body>
        </html>
        """
        
        msg.attach(MIMEText(html_body, 'html'))
        
        # Attach badge
        with open(badge_path, 'rb') as f:
            img = MIMEImage(f.read())
            img.add_header('Content-Disposition', 'attachment', filename=os.path.basename(badge_path))
            msg.attach(img)
        
        # Send email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.quit()
        
        print(f"✅ Email sent successfully via Gmail to {to_email}")
        return True
        
    except Exception as e:
        print(f"❌ Error sending email via Gmail: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description='Send badge email')
    parser.add_argument('--to', required=True, help='Recipient email')
    parser.add_argument('--name', required=True, help='Recipient name')
    parser.add_argument('--badge', required=True, help='Path to badge image')
    
    args = parser.parse_args()
    
    # Get email provider from environment
    email_provider = os.environ.get('EMAIL_PROVIDER', '').lower()
    
    if not email_provider:
        print("⚠️  EMAIL_PROVIDER not set. Skipping email send.")
        print("ℹ️  To enable email notifications, configure EMAIL_PROVIDER and related secrets.")
        print("ℹ️  Supported providers: sendgrid, resend, gmail")
        return
    
    from_email = os.environ.get('FROM_EMAIL', 'noreply@example.com')
    from_name = os.environ.get('FROM_NAME', 'Learn Badges')
    
    # Send email based on provider
    success = False
    
    if email_provider == 'sendgrid':
        api_key = os.environ.get('SENDGRID_API_KEY')
        if not api_key:
            print("❌ SENDGRID_API_KEY not configured")
            sys.exit(1)
        success = send_email_sendgrid(args.to, args.name, args.badge, api_key, from_email, from_name)
        
    elif email_provider == 'resend':
        api_key = os.environ.get('RESEND_API_KEY')
        if not api_key:
            print("❌ RESEND_API_KEY not configured")
            sys.exit(1)
        success = send_email_resend(args.to, args.name, args.badge, api_key, from_email, from_name)
        
    elif email_provider == 'gmail':
        gmail_user = os.environ.get('GMAIL_USER')
        gmail_password = os.environ.get('GMAIL_APP_PASSWORD')
        if not gmail_user or not gmail_password:
            print("❌ GMAIL_USER and GMAIL_APP_PASSWORD not configured")
            sys.exit(1)
        success = send_email_gmail(args.to, args.name, args.badge, gmail_user, gmail_password, from_name)
        
    else:
        print(f"❌ Unsupported email provider: {email_provider}")
        print("ℹ️  Supported providers: sendgrid, resend, gmail")
        sys.exit(1)
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
