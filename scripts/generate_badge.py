#!/usr/bin/env python3
"""
Distribute digital badge for Microsoft Learn completion.
"""

import argparse
import os
import shutil
from datetime import datetime
import hashlib


def sanitize_filename(name):
    """Sanitize the name for use in filename."""
    return "".join(c if c.isalnum() or c in (' ', '_') else '_' for c in name).strip().replace(' ', '_')


def generate_badge(name, email, profile_url=None, proof_url=None, badge_image_path="assets/step-into-ai-with-copilot-badge.png"):
    """Distribute a digital badge by copying the pre-designed image.
    
    Args:
        name: Recipient name
        email: Recipient email
        profile_url: Optional Microsoft Learn profile URL (not used)
        proof_url: Optional completion proof URL (not used)
        badge_image_path: Path to pre-designed badge image (default: assets/step-into-ai-with-copilot-badge.png)
    
    Returns:
        tuple: (output_path, verification_code)
    """
    
    # Generate verification code (hash of name + email + date)
    verification_string = f"{name}{email}{datetime.now().strftime('%Y%m%d')}"
    verification_code = hashlib.sha256(verification_string.encode()).hexdigest()[:12].upper()
    
    # Setup output path
    output_dir = "badges"
    os.makedirs(output_dir, exist_ok=True)
    sanitized_name = sanitize_filename(name)
    output_path = os.path.join(output_dir, f"{sanitized_name}_badge.png")
    
    # Verify badge image exists
    if not os.path.exists(badge_image_path):
        raise FileNotFoundError(f"Badge image not found: {badge_image_path}")
    
    # Copy the custom badge image to the output location
    shutil.copy2(badge_image_path, output_path)
    print(f"Badge distributed: {badge_image_path} -> {output_path}")
    print(f"Verification Code: {verification_code}")
    
    # Write outputs to file for GitHub Actions
    output_file = "badge_info.txt"
    with open(output_file, 'w') as f:
        f.write(f"badge_path={output_path}\n")
        f.write(f"verification_code={verification_code}\n")
    
    return output_path, verification_code


def main():
    parser = argparse.ArgumentParser(description='Distribute a digital badge')
    parser.add_argument('--name', required=True, help='Recipient name')
    parser.add_argument('--email', required=True, help='Recipient email')
    parser.add_argument('--profile', help='Microsoft Learn profile URL (not used)')
    parser.add_argument('--proof', help='Completion proof URL (not used)')
    parser.add_argument('--badge-image', dest='badge_image', 
                        default='assets/step-into-ai-with-copilot-badge.png',
                        help='Path to pre-designed badge image file (default: assets/step-into-ai-with-copilot-badge.png)')
    
    args = parser.parse_args()
    
    badge_path, verification_code = generate_badge(
        args.name,
        args.email,
        args.profile,
        args.proof,
        args.badge_image
    )


if __name__ == "__main__":
    main()
