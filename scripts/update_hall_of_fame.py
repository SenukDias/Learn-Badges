#!/usr/bin/env python3
"""
Update the Hall of Fame with a new badge recipient.
"""

import argparse
import os
from datetime import datetime


def update_hall_of_fame(name, profile_url=None):
    """Add a new entry to the Hall of Fame."""
    
    hall_of_fame_file = "HALL_OF_FAME.md"
    
    # Create Hall of Fame if it doesn't exist
    if not os.path.exists(hall_of_fame_file):
        with open(hall_of_fame_file, 'w') as f:
            f.write("# 🏆 Hall of Fame\n\n")
            f.write("Congratulations to all who have completed the Microsoft Learn AI Skills Challenge!\n\n")
            f.write("| Name | Date Completed | Profile |\n")
            f.write("|------|----------------|----------|\n")
    
    # Read existing content
    with open(hall_of_fame_file, 'r') as f:
        content = f.read()
    
    # Prepare new entry
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    if profile_url and profile_url.strip():
        profile_link = f"[Profile]({profile_url})"
    else:
        profile_link = "N/A"
    
    new_entry = f"| {name} | {date_str} | {profile_link} |\n"
    
    # Check if user already exists in the Hall of Fame table
    # Look for exact match in table rows (format: "| Name | Date | Profile |")
    lines = content.split('\n')
    for line in lines:
        if line.startswith('|') and not line.startswith('|---'):
            # Extract the name column (first column after initial |)
            columns = [col.strip() for col in line.split('|')]
            if len(columns) >= 2 and columns[1] == name:
                print(f"⚠️  {name} is already in the Hall of Fame")
                return
    
    # Append new entry
    with open(hall_of_fame_file, 'a') as f:
        f.write(new_entry)
    
    print(f"✅ Added {name} to the Hall of Fame!")


def main():
    parser = argparse.ArgumentParser(description='Update Hall of Fame')
    parser.add_argument('--name', required=True, help='Recipient name')
    parser.add_argument('--profile', help='Microsoft Learn profile URL')
    
    args = parser.parse_args()
    
    update_hall_of_fame(args.name, args.profile)


if __name__ == "__main__":
    main()
