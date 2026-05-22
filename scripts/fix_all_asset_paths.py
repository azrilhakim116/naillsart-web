import os
import re

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def fix_asset_paths(file_path, is_in_subfolder=False):
    """Fix all asset paths to use absolute paths from root"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        if is_in_subfolder:
            # For files in product/ folder: ../public/ -> /public/
            content = content.replace('src="../public/', 'src="/public/')
            content = content.replace('href="../public/', 'href="/public/')
        else:
            # For files in root: ./public/ -> /public/
            content = content.replace('src="./public/', 'src="/public/')
            content = content.replace('href="./public/', 'href="/public/')
            # Also fix if someone used public/ without ./
            content = re.sub(r'src="public/', r'src="/public/', content)
            content = re.sub(r'href="public/', r'href="/public/', content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed asset paths: {os.path.basename(file_path)}")
            return True
        else:
            print(f"⏭️  No changes: {os.path.basename(file_path)}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("🖼️  Fixing ALL asset paths to use absolute paths...\n")
    
    fixed_count = 0
    
    # Fix index.html and other root files
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
            if fix_asset_paths(file_path, is_in_subfolder=False):
                fixed_count += 1
    
    # Fix product pages
    product_dir = os.path.join(root_dir, 'product')
    product_files = ['almond.html', 'square.html', 'coffin.html', 'stilettos.html']
    
    print("\n📦 Fixing product pages:")
    for product_file in product_files:
        file_path = os.path.join(product_dir, product_file)
        if os.path.exists(file_path):
            if fix_asset_paths(file_path, is_in_subfolder=True):
                fixed_count += 1
    
    print(f"\n✨ Done! Fixed {fixed_count} files.")
    print("\n✅ All asset paths now use absolute paths: /public/images/... /public/css/... /public/video/...")
    print("   This ensures assets load from ANY page on the website!")

if __name__ == "__main__":
    main()
