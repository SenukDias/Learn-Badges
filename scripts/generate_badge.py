#!/usr/bin/env python3
"""
Generate a personalized digital badge for Microsoft Learn completion.
"""

import argparse
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import hashlib


def sanitize_filename(name):
    """Sanitize the name for use in filename."""
    return "".join(c if c.isalnum() or c in (' ', '_') else '_' for c in name).strip().replace(' ', '_')


def generate_badge(name, email, profile_url=None, proof_url=None):
    """Generate a personalized badge image."""
    
    # Badge dimensions
    width, height = 800, 600
    
    # Create image with gradient background
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Create gradient background (blue to purple)
    for y in range(height):
        ratio = y / height
        r = int(41 + (138 - 41) * ratio)
        g = int(98 + (43 - 98) * ratio)
        b = int(255 + (226 - 255) * ratio)
        draw.rectangle([(0, y), (width, y+1)], fill=(r, g, b))
    
    # Draw decorative border
    border_color = (255, 215, 0)  # Gold
    border_width = 10
    draw.rectangle(
        [(border_width, border_width), (width-border_width, height-border_width)],
        outline=border_color,
        width=border_width
    )
    
    # Add inner decorative corners
    corner_size = 40
    for x, y in [(30, 30), (width-30, 30), (30, height-30), (width-30, height-30)]:
        draw.ellipse(
            [(x-corner_size//2, y-corner_size//2), (x+corner_size//2, y+corner_size//2)],
            fill=border_color
        )
    
    # Text positioning
    center_x = width // 2
    
    # Try to load fonts, fallback to default if not available
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        name_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
        info_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except (OSError, IOError):
        title_font = ImageFont.load_default()
        name_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        info_font = ImageFont.load_default()
    
    # Draw title
    title_text = "CERTIFICATE OF COMPLETION"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text((center_x - title_width//2, 80), title_text, fill='white', font=title_font)
    
    # Draw subtitle
    subtitle_text = "Microsoft Learn AI Skills Challenge"
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    draw.text((center_x - subtitle_width//2, 150), subtitle_text, fill='white', font=subtitle_font)
    
    # Draw decorative line
    line_y = 200
    draw.line([(center_x - 200, line_y), (center_x + 200, line_y)], fill=border_color, width=3)
    
    # Draw "This is to certify that"
    certify_text = "This is to certify that"
    certify_bbox = draw.textbbox((0, 0), certify_text, font=info_font)
    certify_width = certify_bbox[2] - certify_bbox[0]
    draw.text((center_x - certify_width//2, 240), certify_text, fill='white', font=info_font)
    
    # Draw recipient name
    name_bbox = draw.textbbox((0, 0), name, font=name_font)
    name_width = name_bbox[2] - name_bbox[0]
    draw.text((center_x - name_width//2, 280), name, fill=border_color, font=name_font)
    
    # Draw achievement text
    achievement_text = "has successfully completed the"
    achievement_bbox = draw.textbbox((0, 0), achievement_text, font=info_font)
    achievement_width = achievement_bbox[2] - achievement_bbox[0]
    draw.text((center_x - achievement_width//2, 350), achievement_text, fill='white', font=info_font)
    
    # Draw plan name
    plan_text = "Microsoft Learn AI Skills Challenge"
    plan_bbox = draw.textbbox((0, 0), plan_text, font=subtitle_font)
    plan_width = plan_bbox[2] - plan_bbox[0]
    draw.text((center_x - plan_width//2, 385), plan_text, fill='white', font=subtitle_font)
    
    # Draw date
    date_text = f"Issued on: {datetime.now().strftime('%B %d, %Y')}"
    date_bbox = draw.textbbox((0, 0), date_text, font=info_font)
    date_width = date_bbox[2] - date_bbox[0]
    draw.text((center_x - date_width//2, 460), date_text, fill='white', font=info_font)
    
    # Generate verification code (hash of name + email + date)
    verification_string = f"{name}{email}{datetime.now().strftime('%Y%m%d')}"
    verification_code = hashlib.sha256(verification_string.encode()).hexdigest()[:12].upper()
    
    # Draw verification code
    verify_text = f"Verification Code: {verification_code}"
    verify_bbox = draw.textbbox((0, 0), verify_text, font=info_font)
    verify_width = verify_bbox[2] - verify_bbox[0]
    draw.text((center_x - verify_width//2, 510), verify_text, fill='white', font=info_font)
    
    # Save badge
    output_dir = "badges"
    os.makedirs(output_dir, exist_ok=True)
    
    sanitized_name = sanitize_filename(name)
    output_path = os.path.join(output_dir, f"{sanitized_name}_badge.png")
    img.save(output_path, 'PNG', quality=95)
    
    print(f"Badge generated successfully: {output_path}")
    print(f"Verification Code: {verification_code}")
    
    # Write outputs to file for GitHub Actions
    output_file = "badge_info.txt"
    with open(output_file, 'w') as f:
        f.write(f"badge_path={output_path}\n")
        f.write(f"verification_code={verification_code}\n")
    
    return output_path, verification_code


def main():
    parser = argparse.ArgumentParser(description='Generate a digital badge')
    parser.add_argument('--name', required=True, help='Recipient name')
    parser.add_argument('--email', required=True, help='Recipient email')
    parser.add_argument('--profile', help='Microsoft Learn profile URL')
    parser.add_argument('--proof', help='Completion proof URL')
    
    args = parser.parse_args()
    
    badge_path, verification_code = generate_badge(
        args.name,
        args.email,
        args.profile,
        args.proof
    )


if __name__ == "__main__":
    main()
