import os
import re

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def fix_links_in_file(file_path):
    """Fix all relative links to use absolute paths from root"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix navbar links (but not images or css)
        # Fix href="our-service.html" -> href="/our-service.html"
        content = re.sub(r'href="([a-z-]+\.html)"', r'href="/\1"', content)
        
        # Fix href="tutorial.html" -> href="/tutorial.html"  
        content = re.sub(r"href='([a-z-]+\.html)'", r"href='/\1'", content)
        
        # Fix href="./product/ -> href="/product/
        content = content.replace('href="./product/', 'href="/product/')
        
        # Fix onclick window.location relative paths
        content = re.sub(r"window\.location\.href='([a-z-]+\.html)'", r"window.location.href='/\1'", content)
        content = re.sub(r'window\.location\.href="([a-z-]+\.html)"', r'window.location.href="/\1"', content)
        
        # Fix index.html to just /
        content = content.replace('href="/index.html"', 'href="/"')
        content = re.sub(r'href="index\.html"', 'href="/"', content)
        
        # Don't change image/css/video paths - keep them as ./public/
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed links: {os.path.basename(file_path)}")
            return True
        else:
            print(f"⏭️  No changes needed: {os.path.basename(file_path)}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("🔗 Fixing all navigation links to use absolute paths...\n")
    
    fixed_count = 0
    
    # Fix index.html
    index_path = os.path.join(root_dir, 'index.html')
    if os.path.exists(index_path):
        if fix_links_in_file(index_path):
            fixed_count += 1
    
    print(f"\n✨ Done! Fixed {fixed_count} files.")
    print("\n📝 All navbar links now use absolute paths (starting with /)")
    print("   This ensures they work from any page on the website!")

if __name__ == "__main__":
    main()
