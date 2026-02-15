# Example Usage Scenarios

This document provides example scenarios for using the Learn-Badges system.

## Scenario 1: User Claims Badge via GitHub Actions

**Steps:**
1. User completes the Microsoft Learn AI Skills Challenge
2. User navigates to the repository's Actions tab
3. User clicks on "Issue Digital Badge" workflow
4. User clicks "Run workflow" button
5. User fills in the form:
   - Name: "Jane Doe"
   - Email: "jane.doe@example.com"
   - Profile: "https://learn.microsoft.com/en-us/users/janedoe/"
   - Proof: (optional screenshot link)
6. User clicks "Run workflow"

**Expected Results:**
- Workflow runs successfully (takes ~30 seconds)
- Badge is generated at `badges/Jane_Doe_badge.png`
- Hall of Fame is updated with Jane's entry
- Jane receives an email with her badge attached
- Jane can share her badge on social media

## Scenario 2: User Requests Badge via Issue

**Steps:**
1. User completes the Microsoft Learn AI Skills Challenge
2. User navigates to repository Issues tab
3. User clicks "New issue" → "Request Digital Badge"
4. User fills out the form with their details
5. User submits the issue

**Expected Results:**
- Issue is created with all user information
- A maintainer reviews the request
- Maintainer triggers the workflow manually using the provided information
- User receives badge via email
- Issue is closed with a success message

## Scenario 3: Bulk Badge Issuance

**For maintainers processing multiple requests:**

1. Collect all badge requests (from issues or a spreadsheet)
2. For each user, run the workflow via Actions tab:
   ```
   Run 1: Name: "User A", Email: "usera@example.com"
   Run 2: Name: "User B", Email: "userb@example.com"
   Run 3: Name: "User C", Email: "userc@example.com"
   ```
3. Workflows can be triggered in quick succession
4. All users receive their badges within minutes

## Scenario 4: Custom Badge for Special Event

**If you want to create a variant for a special event:**

1. Duplicate `scripts/generate_badge.py` to `scripts/generate_special_badge.py`
2. Modify the badge text and colors in the new file
3. Create a new workflow file `.github/workflows/issue-special-badge.yml`
4. Update the workflow to call the new script
5. Users can now claim special event badges

## Scenario 5: Verification of Badge Authenticity

**Someone wants to verify a badge is legitimate:**

1. Recipient shares their badge image
2. Verifier checks the verification code on the badge
3. Verifier contacts the repository maintainer
4. Maintainer checks Hall of Fame for the recipient's name and date
5. Verification code can be regenerated to confirm authenticity:
   ```bash
   python3 scripts/generate_badge.py --name "Recipient Name" --email "email@example.com"
   ```
6. Compare verification codes to confirm authenticity

## Scenario 6: Troubleshooting Email Issues

**User didn't receive their badge email:**

**Step 1: Check Actions logs**
```
1. Go to Actions tab
2. Click on the workflow run
3. Check "Send email with badge" step
4. Look for error messages
```

**Step 2: Common issues and solutions**

Issue: "EMAIL_PROVIDER not set"
```
Solution: Configure email provider secrets in repository settings
See SETUP.md for detailed instructions
```

Issue: "401 Unauthorized"
```
Solution: 
- For SendGrid: Check API key permissions
- For Gmail: Regenerate App Password
- For Resend: Verify API key is correct
```

Issue: "Email sent successfully" but not received
```
Solution:
- Check spam/junk folder
- Verify recipient email address is correct
- Check email provider dashboard for delivery status
```

**Step 3: Resend badge**
- Maintainer can re-run the workflow with the same details
- Badge will be regenerated and resent

## Scenario 7: Migrating to a Different Email Provider

**Currently using SendGrid, want to switch to Resend:**

1. Sign up for Resend account
2. Get your Resend API key
3. Update repository secrets:
   ```
   EMAIL_PROVIDER = resend (update)
   RESEND_API_KEY = re_xxxxx (add new)
   FROM_EMAIL = verify@yourdomain.com (update if needed)
   ```
4. Test with a sample badge request
5. Once confirmed working, can remove old SendGrid secrets

## Scenario 8: Repository Fork for Another Learning Program

**Want to adapt this system for a different program:**

1. Fork the repository
2. Update `README.md` with your program name and details
3. Modify `scripts/generate_badge.py`:
   - Change `title_text` to your program name
   - Update colors to match your branding
   - Add your logo if desired
4. Update `.github/ISSUE_TEMPLATE/badge-request.yml` with your program details
5. Update `scripts/send_email.py` email template
6. Configure your email provider secrets
7. Test the system
8. Share with your community!

## Scenario 9: Adding Multiple Badge Tiers

**Want to offer Bronze, Silver, and Gold badges:**

1. Create three workflow files:
   - `.github/workflows/issue-badge-bronze.yml`
   - `.github/workflows/issue-badge-silver.yml`
   - `.github/workflows/issue-badge-gold.yml`

2. Create three badge generator variants:
   - `scripts/generate_badge_bronze.py` (bronze colors)
   - `scripts/generate_badge_silver.py` (silver colors)
   - `scripts/generate_badge_gold.py` (gold colors)

3. Create separate Hall of Fame files or sections:
   - `HALL_OF_FAME_BRONZE.md`
   - `HALL_OF_FAME_SILVER.md`
   - `HALL_OF_FAME_GOLD.md`

4. Users select which badge tier to claim based on their achievement level

## Scenario 10: Analytics and Reporting

**Want to track badge issuance metrics:**

1. Check Hall of Fame file for total count:
   ```bash
   wc -l < HALL_OF_FAME.md  # Shows total lines
   ```

2. Count badges by month:
   ```bash
   grep "2026-02" HALL_OF_FAME.md | wc -l
   ```

3. Export to CSV for analysis:
   ```bash
   # Extract table data excluding header
   tail -n +5 HALL_OF_FAME.md > badges_export.csv
   ```

4. View all badges issued:
   ```bash
   ls -lh badges/ | wc -l
   ```

5. Check email provider dashboard for delivery rates

## Tips for Success

1. **Test thoroughly** before promoting to your community
2. **Monitor Actions logs** regularly for any issues
3. **Keep documentation updated** as you make changes
4. **Respond to badge requests promptly** to maintain engagement
5. **Celebrate milestones** (100th badge, 500th badge, etc.)
6. **Share success stories** from your Hall of Fame
7. **Gather feedback** from badge recipients to improve the system

## Support Resources

- [Main README](README.md) - Overview and getting started
- [Setup Guide](SETUP.md) - Detailed configuration instructions
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- Repository Issues - Ask questions and report problems
