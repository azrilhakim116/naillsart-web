import os
import re

laravel_views = r"c:\data azril\nailart-laravel\resources\views"

def fix_laravel_paths(file_path, is_in_subfolder=False):
    """Convert HTML paths to Laravel Blade syntax"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix asset paths
        if is_in_subfolder:
            # Product pages: ../images/ -> {{ asset('images/...') }}
            content = re.sub(r'src="../images/([^"]+)"', r'src="{{ asset(\'images/\1\') }}"', content)
            content = re.sub(r'src="../css/([^"]+)"', r'src="{{ asset(\'css/\1\') }}"', content)
            content = re.sub(r'src="../video/([^"]+)"', r'src="{{ asset(\'video/\1\') }}"', content)
            content = re.sub(r'href="../css/([^"]+)"', r'href="{{ asset(\'css/\1\') }}"', content)
        else:
            # Root pages: images/ -> {{ asset('images/...') }}
            content = re.sub(r'src="images/([^"]+)"', r'src="{{ asset(\'images/\1\') }}"', content)
            content = re.sub(r'src="css/([^"]+)"', r'src="{{ asset(\'css/\1\') }}"', content)
            content = re.sub(r'src="video/([^"]+)"', r'src="{{ asset(\'video/\1\') }}"', content)
            content = re.sub(r'href="css/([^"]+)"', r'href="{{ asset(\'css/\1\') }}"', content)
        
        # Fix navigation paths menggunakan url()
        content = re.sub(r'href="/product/([^"]+)"', r'href="{{ url(\'/product/\1\') }}"', content)
        content = re.sub(r'href="/([a-z-]+)"', r'href="{{ url(\'/\1\') }}"', content)
        content = re.sub(r'href="/"', r'href="{{ url(\'/\') }}"', content)
        
        # Fix window.location.href
        content = re.sub(r"window\.location\.href='/([^']+)'", r"window.location.href='{{ url(\'/\1\') }}'", content)
        
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
    print("🚀 Converting to Laravel Blade syntax...\n")
    
    fixed_count = 0
    
    # Fix root blade files
    root_blades = [
        'welcome.blade.php', 'booking.blade.php', 'contact.blade.php'
    ]
    
    print("📄 Fixing root Blade files:")
    for blade_file in root_blades:
        file_path = os.path.join(laravel_views, blade_file)
        if os.path.exists(file_path):
            if fix_laravel_paths(file_path, is_in_subfolder=False):
                fixed_count += 1
    
    # Fix product blade files
    product_dir = os.path.join(laravel_views, 'product')
    if os.path.exists(product_dir):
        print("\n📦 Fixing product Blade files:")
        for blade_file in os.listdir(product_dir):
            if blade_file.endswith('.blade.php'):
                file_path = os.path.join(product_dir, blade_file)
                if fix_laravel_paths(file_path, is_in_subfolder=True):
                    fixed_count += 1
    
    print(f"\n✨ Done! Fixed {fixed_count} Blade files.")
    print("\n✅ Laravel syntax applied:")
    print("   Images: {{ asset('images/...') }}")
    print("   CSS: {{ asset('css/...') }}")
    print("   Links: {{ url('/...') }}")

if __name__ == "__main__":
    main()
