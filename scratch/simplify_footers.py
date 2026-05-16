import os
import re

def simplify_footer(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to find the entire security and verification block
    # It starts with '---' and contains 'Yasal Uyarı' and 'Doğrulama Bilgisi'
    pattern = r'---\s*>\s*\[!(?:CAUTION|NOTE)\]\s*>\s*\*\*Yasal Uyarı:\*\*.*?m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>'
    
    new_footer = """---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>"""

    # We need to use re.DOTALL to match across multiple lines
    new_content = re.sub(pattern, new_footer, content, flags=re.DOTALL)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

docs_dir = r'c:\Users\nolto\Audicodes Çalışma\docs'
root_readme = r'c:\Users\nolto\Audicodes Çalışma\README.md'

files_updated = 0

# Check root files
if os.path.exists(root_readme):
    if simplify_footer(root_readme):
        files_updated += 1

# Check docs directory recursively
for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            if simplify_footer(file_path):
                files_updated += 1

print(f"Updated {files_updated} files.")
