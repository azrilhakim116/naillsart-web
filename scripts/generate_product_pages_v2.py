# Script untuk generate 3 halaman product lainnya berdasarkan template almond.html
import os
import re

# Path files
base_path = r"c:\data azril\nailart-app"
template_path = os.path.join(base_path, "product", "almond.html")

# Product configurations
products = [
    {
        "name": "SQUARE",
        "filename": "square.html",
        "description": "THE SQUARE SHAPE FEATURES STRAIGHT SIDES AND A FLAT TIP, CREATING A BOLD AND<br class=\"hidden md:block\"/> MODERN SILHOUETTE. THIS CONTEMPORARY STYLE IS PERFECT FOR MAKING A STATEMENT<br class=\"hidden md:block\"/> AND WORKS BEAUTIFULLY WITH GEOMETRIC AND MINIMALIST DESIGNS",
        "image_main": "square.png.png",
        "image_prefix": "square",
        "whatsapp_name": "SQUARE NAILS"
    },
    {
        "name": "COFFIN",
        "filename": "coffin.html",
        "description": "THE COFFIN SHAPE (ALSO KNOWN AS BALLERINA) COMBINES ELEGANCE WITH EDGE, FEATURING<br class=\"hidden md:block\"/> LONG TAPERED SIDES AND A SQUARED-OFF TIP. THIS TRENDY SHAPE IS PERFECT<br class=\"hidden md:block\"/> FOR THOSE WHO WANT A MODERN, SOPHISTICATED LOOK WITH MAXIMUM STYLE IMPACT",
        "image_main": "coffin.png.png",
        "image_prefix": "coffin",
        "whatsapp_name": "COFFIN NAILS"
    },
    {
        "name": "STILETTO",
        "filename": "stilettos.html",
        "description": "THE STILETTO SHAPE FEATURES A LONG, DRAMATIC POINT THAT CREATES A FIERCE AND<br class=\"hidden md:block\"/> BOLD STATEMENT. THIS EDGY STYLE IS PERFECT FOR SPECIAL OCCASIONS AND<br class=\"hidden md:block\"/> FOR THOSE WHO WANT TO COMMAND ATTENTION WITH THEIR NAILS",
        "image_main": "stilettos.png.png",
        "image_prefix": "stiletto",
        "whatsapp_name": "STILETTO NAILS"
    }
]

# Read template
print("📖 Reading template from almond.html...")
with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

# Generate each product page
for product in products:
    print(f"\n🔨 Generating {product['filename']}...")
    
    # Replace content
    content = template_content
    
    # Title and headings
    content = content.replace("Almond Nails - ONNAILS", f"{product['name'].title()} Nails - ONNAILS")
    content = content.replace("ALMOND", product['name'])
    content = content.replace("Almond", product['name'].title())
    
    # Description
    content = re.sub(
        r'THE ALMOND SHAPE IS A CLASSIC SILHOUETTE.*?ELEGANT, VERSATILE BASE FOR ANY MANICURE',
        product['description'],
        content,
        flags=re.DOTALL
    )
    
    # Main image
    content = content.replace("almond.png.png", product['image_main'])
    
    # Gallery images (almond1.jpg -> square1.jpg, etc.)
    for i in range(1, 24):
        content = content.replace(f"almond{i}.jpg", f"{product['image_prefix']}{i}.jpg")
    
    # Special case for card 9 (uses almond10.jpg)
    content = content.replace("almond10.jpg", f"{product['image_prefix']}9.jpg")
    content = content.replace("almond11.jpg", f"{product['image_prefix']}10.jpg")
    content = content.replace("almond12.jpg", f"{product['image_prefix']}11.jpg")
    content = content.replace("almond13.jpg", f"{product['image_prefix']}12.jpg")
    content = content.replace("almond14.jpg", f"{product['image_prefix']}13.jpg")
    content = content.replace("almond15.jpg", f"{product['image_prefix']}14.jpg")
    content = content.replace("almond16.jpg", f"{product['image_prefix']}15.jpg")
    content = content.replace("almond17.jpg", f"{product['image_prefix']}16.jpg")
    content = content.replace("almond18.jpg", f"{product['image_prefix']}17.jpg")
    content = content.replace("almond19.jpg", f"{product['image_prefix']}18.jpg")
    content = content.replace("almond20.jpg", f"{product['image_prefix']}19.jpg")
    content = content.replace("almond21.jpg", f"{product['image_prefix']}20.jpg")
    content = content.replace("almond22.jpg", f"{product['image_prefix']}21.jpg")
    content = content.replace("almond23.jpg", f"{product['image_prefix']}22.jpg")
    
    # Last card uses first image (card 23 = card 1)
    # Already fixed by replacing almond1.jpg above
    
    # CSS class names
    content = content.replace(".almond-card:hover", f".{product['image_prefix']}-card:hover")
    content = content.replace("class=\"almond-card", f"class=\"{product['image_prefix']}-card")
    content = content.replace(".almond-card", f".{product['image_prefix']}-card")
    content = content.replace("querySelector('.almond-card')", f"querySelector('.{product['image_prefix']}-card')")
    content = content.replace("querySelectorAll('.almond-card')", f"querySelectorAll('.{product['image_prefix']}-card')")
    
    # Console logs
    content = content.replace("ONNAILS Almond Page Loaded", f"ONNAILS {product['name'].title()} Page Loaded")
    
    # WhatsApp message
    content = content.replace("ALMOND NAILS", product['whatsapp_name'])
    content = content.replace("*ALMOND NAILS", f"*{product['whatsapp_name']}")
    
    # Alt texts
    content = content.replace("Almond Design", f"{product['name'].title()} Design")
    content = content.replace("alt=\"Almond Nails\"", f"alt=\"{product['name'].title()} Nails\"")
    
    # Save file
    output_path = os.path.join(base_path, "product", product['filename'])
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {product['filename']} created successfully!")
    print(f"   - 23 cards: {product['image_prefix']}1.jpg - {product['image_prefix']}23.jpg")
    print(f"   - Main image: {product['image_main']}")
    print(f"   - Class name: .{product['image_prefix']}-card")

print("\n🎉 All product pages generated successfully!\n")
print("📁 Generated files:")
for product in products:
    print(f"   - product/{product['filename']}")
