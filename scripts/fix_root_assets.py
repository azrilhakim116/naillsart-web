import os
import re

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def fix_to_root_assets(file_path, is_in_subfolder=False):
    """Fix paths to use assets directly from root"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        if is_in_subfolder:
            # For files in product/ folder
            content = content.replace('src="../public/images/', 'src="../images/')
            content = content.replace('src="../public/css/', 'src="../css/')
            content = content.replace('src="../public/video/', 'src="../video/')
            content = content.replace('href="../public/images/', 'href="../images/')
            content = content.replace('href="../public/css/', 'href="../css/')
        else:
            # For files in root
            content = content.replace('src="public/images/', 'src="images/')
            content = content.replace('src="public/css/', 'src="css/')
            content = content.replace('src="public/video/', 'src="video/')
            content = content.replace('href="public/images/', 'href="images/')
            content = content.replace('href="public/css/', 'href="css/')
            content = content.replace('href="public/video/', 'href="video/')
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed: {os.path.basename(file_path)}")
            return True
        else:
            print(f"⏭️  No changes: {os.path.basename(file_path)}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("📁 Restructuring to root-level assets...\n")
    
    fixed_count = 0
    
    # Fix root HTML files
    root_html_files = [
        'index.html', 'booking.html', 'contact.html', 
        'collaboration.html', 'our-service.html', 'press-on.html',
        'terms.html', 'tutorial.html', 'tutorial-apply.html',
        'tutorial-care.html', 'tutorial-measure.html', 'wishlist.html'
    ]
    
    print("📄 Fixing root HTML files:")
    for html_file in root_html_files:
        file_path = os.path.join(root_dir, html_file)
        if os.path.exists(file_path):
            if fix_to_root_assets(file_path, is_in_subfolder=False):
                fixed_count += 1
    
    # Fix product pages
    product_dir = os.path.join(root_dir, 'product')
    product_files = ['almond.html', 'square.html', 'coffin.html', 'stilettos.html']
    
    print("\n📦 Fixing product pages:")
    for product_file in product_files:
        file_path = os.path.join(product_dir, product_file)
        if os.path.exists(file_path):
            if fix_to_root_assets(file_path, is_in_subfolder=True):
                fixed_count += 1
    
    print(f"\n✨ Done! Fixed {fixed_count} files.")
    print("\n✅ New structure:")
    print("   /images/onnails.png")
    print("   /css/style.css")
    print("   /video/...")
    print("\n   This is the standard Vercel static structure!")

if __name__ == "__main__":
    main()
