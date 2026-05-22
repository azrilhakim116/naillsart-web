import os
import re

# Folder root project
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Daftar file HTML di root yang perlu diperbaiki
root_html_files = [
    'index.html',
    'booking.html',
    'collaboration.html',
    'contact.html',
    'our-service.html',
    'press-on.html',
    'terms.html',
    'tutorial.html',
    'tutorial-apply.html',
    'tutorial-care.html',
    'tutorial-measure.html',
    'wishlist.html'
]

def fix_product_links(file_path):
    """Perbaiki link ../product menjadi ./product untuk file HTML di root"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Ganti semua ../product dengan ./product
        original_content = content
        content = content.replace('href="../product/', 'href="./product/')
        content = content.replace('href="../product/', 'href="./product/')  # double check
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed product links: {os.path.basename(file_path)}")
            return True
        else:
            print(f"⏭️  No product links to fix: {os.path.basename(file_path)}")
            return False
    except Exception as e:
        print(f"❌ Error fixing {file_path}: {e}")
        return False

def main():
    print("🔧 Fixing product links in HTML files...\n")
    
    fixed_count = 0
    
    # Perbaiki semua file HTML di root
    for html_file in root_html_files:
        file_path = os.path.join(root_dir, html_file)
        if os.path.exists(file_path):
            if fix_product_links(file_path):
                fixed_count += 1
        else:
            print(f"⚠️  File not found: {html_file}")
    
    print(f"\n✨ Done! Fixed product links in {fixed_count} files.")

if __name__ == "__main__":
    main()
