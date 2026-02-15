# Testing Guide

This guide helps you test the digital badge automation system before going live.

## Pre-Deployment Testing Checklist

### ✅ Phase 1: Local Testing

#### Test Badge Generation
```bash
cd /home/runner/work/Learn-Badges/Learn-Badges
python3 scripts/generate_badge.py \
  --name "Test User" \
  --email "test@example.com"
```

**Expected Output:**
- Badge file created in `badges/Test_User_badge.png`
- File size: ~40KB
- Verification code displayed
- No errors

#### Test Hall of Fame Update
```bash
python3 scripts/update_hall_of_fame.py \
  --name "Test User" \
  --profile "https://learn.microsoft.com/users/test/"
```

**Expected Output:**
- Entry added to `HALL_OF_FAME.md`
- No duplicate entry warning on second run
- Proper markdown table formatting

#### Test Email Script (Without Sending)
```bash
python3 scripts/send_email.py \
  --to "test@example.com" \
  --name "Test User" \
  --badge "badges/Test_User_badge.png"
```

**Expected Output:**
- Warning about EMAIL_PROVIDER not set
- Script exits gracefully
- No errors

### ✅ Phase 2: Email Provider Testing

#### Configure Test Email Provider

Choose one provider for testing:

**Option 1: SendGrid**
```bash
export EMAIL_PROVIDER=sendgrid
export SENDGRID_API_KEY=SG.your_test_key
export FROM_EMAIL=test@yourdomain.com
export FROM_NAME="Test Badges"
```

**Option 2: Resend**
```bash
export EMAIL_PROVIDER=resend
export RESEND_API_KEY=re_your_test_key
export FROM_EMAIL=test@yourdomain.com
export FROM_NAME="Test Badges"
```

**Option 3: Gmail**
```bash
export EMAIL_PROVIDER=gmail
export GMAIL_USER=your.email@gmail.com
export GMAIL_APP_PASSWORD=your_16_char_password
export FROM_NAME="Test Badges"
```

#### Send Test Email
```bash
python3 scripts/send_email.py \
  --to "YOUR_ACTUAL_EMAIL@example.com" \
  --name "Test User" \
  --badge "badges/Test_User_badge.png"
```

**Verify:**
- [ ] Email received within 2 minutes
- [ ] Badge attached correctly
- [ ] Email HTML renders properly
- [ ] Links work correctly
- [ ] Not marked as spam

### ✅ Phase 3: GitHub Actions Testing

#### Add Secrets to Repository
1. Go to Settings → Secrets and variables → Actions
2. Add required secrets based on your email provider
3. Verify all secrets are added correctly

#### Enable Workflow Permissions
1. Go to Settings → Actions → General
2. Set "Workflow permissions" to "Read and write permissions"
3. Save changes

#### Test Workflow Run
1. Go to Actions tab
2. Select "Issue Digital Badge" workflow
3. Click "Run workflow"
4. Fill in test data:
   ```
   Name: Test User
   Email: YOUR_ACTUAL_EMAIL@example.com
   Profile: (leave empty)
   Proof: (leave empty)
   ```
5. Click "Run workflow"

**Monitor the run:**
- [ ] Workflow starts successfully
- [ ] All steps complete (green checkmarks)
- [ ] Badge file committed to repository
- [ ] Hall of Fame updated
- [ ] Email received

**Check logs for each step:**
```
✓ Checkout repository
✓ Set up Python
✓ Install dependencies
✓ Generate badge
✓ Update Hall of Fame
✓ Commit and push changes
✓ Send email with badge
✓ Create success comment
```

### ✅ Phase 4: Edge Case Testing

#### Test 1: Long Name
```
Name: "Supercalifragilisticexpialidocious VeryLongLastName"
Email: your@email.com
```

**Expected:** Badge generates with text sized appropriately

#### Test 2: Special Characters in Name
```
Name: "François O'Brien-Smith"
Email: your@email.com
```

**Expected:** Characters handled correctly in filename

#### Test 3: Missing Optional Fields
```
Name: "Test User"
Email: your@email.com
Profile: (empty)
Proof: (empty)
```

**Expected:** Works fine with just required fields

#### Test 4: Invalid Email Format
```
Name: "Test User"
Email: "not-an-email"
```

**Expected:** Email fails gracefully with error message

#### Test 5: Duplicate Request
```
# Run workflow twice with same name
Name: "Duplicate Test"
Email: your@email.com
```

**Expected:** 
- Both badges generated
- Hall of Fame shows warning about duplicate
- New badge file created (or overwrites old one)

### ✅ Phase 5: Load Testing

#### Test Multiple Concurrent Requests
1. Queue 3-5 workflow runs simultaneously
2. Use different names/emails for each
3. Monitor Actions tab

**Expected:**
- All workflows complete successfully
- No merge conflicts
- All emails sent
- Hall of Fame updated correctly

### ✅ Phase 6: Recovery Testing

#### Test 1: Email Provider Down
```bash
# Set invalid API key
export SENDGRID_API_KEY=invalid_key

# Run workflow
```

**Expected:**
- Badge still generated
- Hall of Fame still updated
- Email step fails with clear error message
- Workflow marked as failed

#### Test 2: Git Conflicts
```bash
# Manually edit HALL_OF_FAME.md in another branch
# Run workflow
```

**Expected:**
- Workflow handles conflict gracefully
- Clear error message in logs

#### Test 3: Missing Dependencies
```bash
# Comment out Pillow in workflow
# Run workflow
```

**Expected:**
- Clear error about missing module
- Workflow fails at badge generation step

## Post-Deployment Monitoring

### Daily Checks (First Week)

1. **Check Actions Tab**
   - Any failed workflows?
   - Review error logs

2. **Check Email Deliverability**
   - Check email provider dashboard
   - Any bounces or spam reports?

3. **Review Hall of Fame**
   - Formatting correct?
   - All entries present?

4. **Check Badge Directory**
   - File sizes reasonable?
   - Images rendering correctly?

### Weekly Checks (After First Week)

1. **Monitor email quota**
   - SendGrid: Check daily usage
   - Gmail: Monitor send limits

2. **Review user feedback**
   - Any issues reported?
   - Common questions?

3. **Check repository size**
   - Badge directory growing too large?
   - Consider archiving old badges

## Troubleshooting Common Issues

### Issue: Workflow Times Out

**Symptoms:**
- Workflow runs for 6+ hours
- Eventually cancelled

**Solutions:**
- Check for infinite loops in scripts
- Review Python dependencies installation
- Check email provider response times

### Issue: Badge Not Generated

**Symptoms:**
- Email sent but no badge attached
- Badge file missing from repository

**Solutions:**
- Check Pillow installation
- Verify fonts available
- Check file permissions

### Issue: Email Not Received

**Symptoms:**
- Workflow shows success
- No email in inbox or spam

**Solutions:**
- Verify email provider credentials
- Check from_email is verified
- Review email provider dashboard
- Check spam folder
- Try different email address

### Issue: Hall of Fame Conflicts

**Symptoms:**
- Merge conflicts in HALL_OF_FAME.md
- Workflow fails at commit step

**Solutions:**
- Pull latest changes
- Manually resolve conflicts
- Re-run workflow

### Issue: Rate Limits Exceeded

**Symptoms:**
- Email provider returns 429 error
- Some emails not sent

**Solutions:**
- Reduce concurrent workflow runs
- Upgrade email provider plan
- Implement queuing mechanism

## Success Criteria

Before going live, ensure:

- [x] All test workflows complete successfully
- [x] Test emails received correctly
- [x] Badges generate with correct information
- [x] Hall of Fame updates properly
- [x] No errors in Action logs
- [x] Email provider verified and working
- [x] Documentation reviewed and complete
- [x] Issue template works correctly
- [x] Repository secrets configured
- [x] Workflow permissions enabled

## Ready to Launch! 🚀

Once all tests pass:

1. Announce to your community
2. Share the Actions workflow URL
3. Monitor first few requests closely
4. Gather feedback
5. Iterate and improve

## Testing Log Template

Use this template to track your testing:

```
Date: ___________
Tester: ___________

Phase 1: Local Testing
- [ ] Badge generation: ______
- [ ] Hall of Fame update: ______
- [ ] Email script: ______

Phase 2: Email Testing
- [ ] Provider configured: ______
- [ ] Test email sent: ______
- [ ] Email received: ______

Phase 3: GitHub Actions
- [ ] Secrets configured: ______
- [ ] Permissions enabled: ______
- [ ] Workflow successful: ______

Phase 4: Edge Cases
- [ ] Long name: ______
- [ ] Special characters: ______
- [ ] Missing fields: ______
- [ ] Duplicate request: ______

Phase 5: Load Testing
- [ ] Multiple concurrent: ______

Phase 6: Recovery Testing
- [ ] Email provider down: ______
- [ ] Git conflicts: ______

Notes:
_________________________________
_________________________________
_________________________________

Overall Status: PASS / FAIL / NEEDS WORK
```
