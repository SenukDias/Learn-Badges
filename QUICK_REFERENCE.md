# Quick Reference Guide

## How to Claim Your Badge (Quick Steps)

### Method 1: GitHub Actions (Fastest)
1. Go to [Actions Tab](../../actions/workflows/issue-badge.yml)
2. Click **"Run workflow"**
3. Fill in your details
4. Click **"Run workflow"** again
5. Check your email in 2-3 minutes! 📧

### Method 2: Create an Issue
1. Go to [Issues](../../issues/new/choose)
2. Select **"Request Digital Badge"**
3. Fill out the form
4. Submit and wait for approval

---

## What Information Do You Need?

| Field | Required? | Example |
|-------|-----------|---------|
| Full Name | ✅ Yes | Jane Doe |
| Email Address | ✅ Yes | jane.doe@example.com |
| Microsoft Learn Profile | ❌ Optional | https://learn.microsoft.com/users/janedoe |
| Completion Proof | ❌ Optional | Link to screenshot or certificate |

---

## What You'll Receive

✅ Personalized digital badge (800x600 PNG)  
✅ Unique verification code  
✅ Email with badge attached  
✅ Your name in the [Hall of Fame](HALL_OF_FAME.md)  

---

## Troubleshooting

### ❓ Didn't receive email?
- Check spam/junk folder
- Verify email address was correct
- Check [Actions tab](../../actions) for errors
- Contact maintainer via issue

### ❓ Can I get multiple badges?
- Each person gets one badge per completion
- Requesting duplicate will show warning

### ❓ Can I customize my badge?
- Badge design is standardized for all recipients
- Your name and date make it unique

### ❓ How do I verify badge authenticity?
- Each badge has a unique verification code
- Cross-reference with [Hall of Fame](HALL_OF_FAME.md)
- Contact repository maintainer to verify

---

## Sharing Your Badge

Here are some ideas for sharing your achievement:

### LinkedIn
1. Upload badge to a new post
2. Add text: "Completed the Microsoft Learn AI Skills Challenge! 🎓"
3. Tag relevant people/companies
4. Include hashtags: #MicrosoftLearn #AISkills #DigitalBadge

### Twitter/X
```
Just earned my digital badge for completing the Microsoft Learn AI Skills Challenge! 🎉 
#MicrosoftLearn #AISkills #Achievement
```

### GitHub Profile README
```markdown
## 🏆 Achievements
- Microsoft Learn AI Skills Challenge Badge (2026)
```

### Portfolio Website
Add the badge image with a link to the Hall of Fame

### Email Signature
Resize badge to 150x112px and add to your signature

---

## Email Providers for Maintainers

Quick comparison to help choose:

| Provider | Free Tier | Setup Difficulty | Best For |
|----------|-----------|------------------|----------|
| **SendGrid** | 100/day | Easy | Most users |
| **Resend** | 100/day | Very Easy | Developers |
| **Gmail** | 500/day | Medium | Small scale |

See [SETUP.md](SETUP.md) for detailed configuration.

---

## Badge Specifications

- **Format:** PNG
- **Dimensions:** 800x600 pixels
- **Size:** ~40KB
- **Colors:** Blue-purple gradient with gold accents
- **Fonts:** DejaVu Sans

---

## Repository Structure (For Developers)

```
Learn-Badges/
├── .github/
│   ├── workflows/
│   │   └── issue-badge.yml       # Main automation workflow
│   └── ISSUE_TEMPLATE/
│       └── badge-request.yml     # Issue form template
├── scripts/
│   ├── generate_badge.py         # Creates badge images
│   ├── send_email.py             # Handles email delivery
│   └── update_hall_of_fame.py    # Updates recipient list
├── badges/                        # Generated badge files
├── HALL_OF_FAME.md               # Public recipient list
├── README.md                     # Main documentation
├── SETUP.md                      # Configuration guide
├── EXAMPLES.md                   # Usage scenarios
└── QUICK_REFERENCE.md            # This file
```

---

## Maintainer Quick Actions

### Manually Trigger Badge for Someone
```bash
# Go to Actions → Issue Digital Badge → Run workflow
# Fill in their details and run
```

### Check Recent Badges
```bash
ls -lt badges/ | head -10
```

### View Hall of Fame Stats
```bash
wc -l HALL_OF_FAME.md
```

### Test Email Configuration
```bash
python3 scripts/send_email.py \
  --to "your-email@example.com" \
  --name "Test User" \
  --badge "badges/test_badge.png"
```

### Generate Badge Locally
```bash
python3 scripts/generate_badge.py \
  --name "Test User" \
  --email "test@example.com"
```

---

## Support

Need help?
- 📖 Read the [full README](README.md)
- 🔧 Check the [setup guide](SETUP.md)
- 💡 Browse [examples](EXAMPLES.md)
- 🐛 [Report an issue](../../issues/new)

---

**Happy badge claiming! 🎉**
