# 🎓 Learn-Badges

Automated digital badge system for recognizing completion of the **Microsoft Learn AI Skills Challenge**.

[![Issue Badge](https://github.com/SenukDias/Learn-Badges/actions/workflows/issue-badge.yml/badge.svg)](https://github.com/SenukDias/Learn-Badges/actions/workflows/issue-badge.yml)

## 🎯 Overview

This repository provides an automated system to:
- ✅ Generate personalized digital badges for learners
- 📧 Email badges directly to recipients
- 🏆 Maintain a public Hall of Fame
- 🔐 Provide verification codes for authenticity

## 🚀 How to Claim Your Badge

### Option 1: Trigger the Workflow (Recommended)

If you have access to the repository:

1. Go to the [Actions tab](../../actions/workflows/issue-badge.yml)
2. Click "Run workflow"
3. Fill in your details:
   - Your full name
   - Your email address
   - Your Microsoft Learn profile URL (optional)
   - Link to completion proof (optional)
4. Click "Run workflow"
5. Your badge will be generated and emailed to you within minutes!

### Option 2: Create a Badge Request Issue

1. Go to [Issues](../../issues/new/choose)
2. Select "Request Digital Badge"
3. Fill out the form with your information
4. Submit the issue
5. A maintainer will review and process your request

## 📋 What You'll Receive

- 🎨 A personalized digital badge (PNG format, 800x600px)
- 🔢 A unique verification code for authenticity
- 🏆 Recognition in our [Hall of Fame](HALL_OF_FAME.md)
- 📧 Email with your badge and instructions for sharing

## 🎨 Badge Features

Your personalized badge includes:
- Your name prominently displayed
- Microsoft Learn AI Skills Challenge title
- Issue date
- Unique verification code
- Professional design with gradient background and gold accents

## 🏆 Hall of Fame

Check out our [Hall of Fame](HALL_OF_FAME.md) to see all the amazing learners who have completed the challenge!

## 🔧 Setup (For Repository Maintainers)

### Prerequisites

- GitHub repository with Actions enabled
- Email service provider account (choose one):
  - **SendGrid** (recommended, 100 emails/day free)
  - **Resend** (100 emails/day free)
  - **Gmail** (with App Password)

### Configuration Steps

1. **Choose your email provider** and obtain credentials:

   **For SendGrid:**
   - Sign up at [SendGrid](https://sendgrid.com/)
   - Create an API key
   - Verify a sender email address

   **For Resend:**
   - Sign up at [Resend](https://resend.com/)
   - Get your API key
   - Verify your domain

   **For Gmail:**
   - Enable 2-Factor Authentication
   - Generate an [App Password](https://myaccount.google.com/apppasswords)

2. **Add secrets to your GitHub repository:**

   Go to Settings → Secrets and variables → Actions → New repository secret

   **Required for all providers:**
   - `EMAIL_PROVIDER`: Set to `sendgrid`, `resend`, or `gmail`
   - `FROM_EMAIL`: Your sender email address
   - `FROM_NAME`: Your sender name (e.g., "Learn Badges Team")

   **For SendGrid:**
   - `SENDGRID_API_KEY`: Your SendGrid API key

   **For Resend:**
   - `RESEND_API_KEY`: Your Resend API key

   **For Gmail:**
   - `GMAIL_USER`: Your Gmail address
   - `GMAIL_APP_PASSWORD`: Your Gmail App Password

3. **Enable GitHub Actions:**
   - Ensure Actions are enabled in repository settings
   - Grant workflow write permissions (Settings → Actions → General → Workflow permissions → Read and write permissions)

### Testing the Setup

1. Run the workflow manually with test data
2. Check the Actions tab for any errors
3. Verify the email is received
4. Confirm the Hall of Fame is updated

## 🛠️ Technical Details

### Architecture

```
User Triggers Workflow
        ↓
GitHub Actions starts
        ↓
Generate personalized badge (Python + Pillow)
        ↓
Update Hall of Fame (Markdown)
        ↓
Send email with badge (SendGrid/Resend/Gmail)
        ↓
Commit changes to repository
        ↓
User receives badge via email
```

### File Structure

```
.
├── .github/
│   ├── workflows/
│   │   └── issue-badge.yml          # Main workflow
│   └── ISSUE_TEMPLATE/
│       └── badge-request.yml        # Issue template
├── scripts/
│   ├── generate_badge.py            # Badge generator
│   ├── update_hall_of_fame.py       # Hall of Fame updater
│   └── send_email.py                # Email sender
├── badges/                           # Generated badges (created automatically)
├── HALL_OF_FAME.md                  # Public Hall of Fame
└── README.md                        # This file
```

### Dependencies

- Python 3.11+
- Pillow (image generation)
- requests (API calls)

## 🔒 Security

- Email credentials are stored as GitHub Secrets (encrypted)
- Verification codes ensure badge authenticity
- No sensitive data is committed to the repository
- Badge files are stored in the repository but contain no personal data beyond names

## 📝 Customization

### Customize Badge Design

Edit `scripts/generate_badge.py` to modify:
- Colors and gradients
- Font styles and sizes
- Layout and spacing
- Logo or additional graphics

### Customize Email Template

Edit `scripts/send_email.py` to modify the email HTML template.

### Customize Plan Details

Update the plan URL and title in:
- `README.md`
- `scripts/generate_badge.py`
- `.github/ISSUE_TEMPLATE/badge-request.yml`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Microsoft Learn for providing excellent learning resources
- The open-source community for the tools that make this possible

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](../../issues) page
2. Create a new issue if your problem isn't already reported
3. Provide as much detail as possible

---

**Happy Learning! 🚀**