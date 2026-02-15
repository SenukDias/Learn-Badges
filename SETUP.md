# 🔧 Configuration Guide

This guide will help you set up the digital badge automation system.

## Quick Start

### Step 1: Choose Your Email Provider

Select one of the supported email providers:

#### Option A: SendGrid (Recommended)
- ✅ Free tier: 100 emails/day
- ✅ Easy setup
- ✅ Reliable delivery

**Setup:**
1. Sign up at https://sendgrid.com/
2. Go to Settings → API Keys
3. Create a new API key with "Mail Send" permissions
4. Verify a sender email in Settings → Sender Authentication

#### Option B: Resend
- ✅ Free tier: 100 emails/day  
- ✅ Modern API
- ✅ Great developer experience

**Setup:**
1. Sign up at https://resend.com/
2. Get your API key from the dashboard
3. Verify your domain (or use their test domain for testing)

#### Option C: Gmail
- ✅ Free
- ✅ Use your existing Gmail account
- ⚠️ Requires 2FA and App Password

**Setup:**
1. Enable 2-Factor Authentication on your Google account
2. Go to https://myaccount.google.com/apppasswords
3. Generate an app password for "Mail"
4. Save the 16-character password

### Step 2: Configure GitHub Secrets

Go to your repository's Settings → Secrets and variables → Actions → New repository secret

Add the following secrets based on your email provider:

#### For SendGrid:
```
EMAIL_PROVIDER = sendgrid
SENDGRID_API_KEY = SG.xxxxxxxxxxxxxxxxxxxxxx
FROM_EMAIL = noreply@yourdomain.com
FROM_NAME = Learn Badges Team
```

#### For Resend:
```
EMAIL_PROVIDER = resend
RESEND_API_KEY = re_xxxxxxxxxxxxxxxxxxxxxx
FROM_EMAIL = noreply@yourdomain.com
FROM_NAME = Learn Badges Team
```

#### For Gmail:
```
EMAIL_PROVIDER = gmail
GMAIL_USER = your.email@gmail.com
GMAIL_APP_PASSWORD = xxxxxxxxxxxxxxxx (16-character app password)
FROM_NAME = Learn Badges Team
```

### Step 3: Enable Workflow Permissions

1. Go to Settings → Actions → General
2. Under "Workflow permissions", select:
   - ✅ Read and write permissions
3. Click "Save"

### Step 4: Test the Setup

1. Go to Actions tab
2. Select "Issue Digital Badge" workflow
3. Click "Run workflow"
4. Fill in test data:
   - Name: Test User
   - Email: your-email@example.com
   - Leave other fields empty
5. Click "Run workflow"
6. Wait a few moments and check your email!

## Troubleshooting

### Email not received?

1. **Check spam folder** - Badge emails might be filtered
2. **Check Actions logs** - Go to Actions tab → Latest workflow run → View logs
3. **Verify secrets** - Ensure all required secrets are set correctly
4. **Test email provider** - Make sure your API key/credentials are valid

### Badge not generated?

1. Check the Actions logs for Python errors
2. Ensure Pillow installed correctly (should happen automatically)
3. Check for file permission issues

### Hall of Fame not updated?

1. Verify workflow has write permissions
2. Check for git conflicts
3. Review Actions logs for git errors

### Common Error Messages

**"EMAIL_PROVIDER not set"**
- Add the `EMAIL_PROVIDER` secret with value: `sendgrid`, `resend`, or `gmail`

**"SENDGRID_API_KEY not configured"**
- Add your SendGrid API key as a repository secret

**"401 Unauthorized"**
- Check that your API key is valid and has the correct permissions

**"Permission denied"**
- Enable workflow write permissions in repository settings

## Advanced Configuration

### Custom Badge Design

Edit `scripts/generate_badge.py`:

```python
# Change colors
border_color = (255, 215, 0)  # Gold
background_start = (41, 98, 255)  # Blue
background_end = (138, 43, 226)  # Purple

# Change dimensions
width, height = 800, 600

# Change text
title_text = "YOUR CUSTOM TITLE"
```

### Custom Email Template

Edit `scripts/send_email.py` - find the HTML sections and customize:

```python
html_body = f"""
<html>
<body>
    <h1>Your Custom Heading</h1>
    <!-- Add your custom HTML here -->
</body>
</html>
"""
```

### Add Your Logo

1. Add your logo to the repository (e.g., `assets/logo.png`)
2. Modify `scripts/generate_badge.py`:

```python
# Load and paste logo
logo = Image.open('assets/logo.png')
logo = logo.resize((100, 100))  # Resize as needed
img.paste(logo, (350, 50))  # Position on badge
```

### Multiple Badge Types

To support multiple badge types (different challenges):

1. Duplicate the workflow file with a new name
2. Modify the badge text in the new `generate_badge.py` call
3. Update the issue template accordingly

## Security Best Practices

1. **Never commit secrets** - Always use GitHub Secrets
2. **Rotate API keys** - Change keys periodically
3. **Use least privilege** - Give API keys only required permissions
4. **Monitor usage** - Check email provider dashboards regularly
5. **Enable 2FA** - On GitHub and email provider accounts

## Email Provider Limits

### SendGrid Free Tier
- 100 emails/day
- No credit card required
- Single sender verification

### Resend Free Tier
- 100 emails/day
- 1 domain
- No credit card required

### Gmail
- 500 emails/day (free account)
- 2,000 emails/day (Google Workspace)
- Rate limits apply

## Support

Need help? 
1. Check the [main README](README.md)
2. Review [GitHub Actions documentation](https://docs.github.com/en/actions)
3. Open an issue in this repository

## Next Steps

Once configured:
1. Test the workflow with your own email
2. Share the Actions URL with your community
3. Promote the badge program
4. Monitor the Hall of Fame growth!

Happy badge issuing! 🎉
