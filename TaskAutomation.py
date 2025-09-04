#Extract Email Addressesfrom a.txt file and save them to another file.
import re

input_file = "emails.txt"
output_file = "extracted_emails.txt"

# Read file content
with open(input_file, "r") as file:
    content = file.read()

# Extract emails using regex
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", content)

# Save to output file
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print(f"✅ Extracted {len(emails)} email(s) to '{output_file}'.")
