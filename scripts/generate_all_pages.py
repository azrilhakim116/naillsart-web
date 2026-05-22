import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Template untuk halaman booking
booking_html = '''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Booking - ONNAILS</title>
	<script src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
	<link rel="stylesheet" href="./public/css/style.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
	<link href="https://fonts.googleapis.com/css2?family=Kalnia:wght@500&display=swap" rel="stylesheet">
	<script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-[#f2d6d3]">

<header x-data="{}" class="w-full onnails-navbar relative">
	<div class="max-w-[1440px] mx-auto px-6 h-[80px] flex items-center justify-between">
		<a href="./index.html" class="absolute left-1/2 -translate-x-1/2">
			<img src="./public/images/onnails.png" class="h-16 md:h-20" />
		</a>
		<a href="./index.html" class="ml-auto text-gray-800 hover:text-[#CE8A97] font-[Kalnia]">← BACK TO HOME</a>
	</div>
</header>

<section class="max-w-[800px] mx-auto px-6 py-16 min-h-[70vh]">
	<div class="text-center mb-12">
		<h1 class="font-[Kalnia] text-5xl text-[#7A2E2E] mb-6">BOOK YOUR NAILS</h1>
		<p class="text-xl text-gray-600">Choose your preferred booking method</p>
	</div>
	
	<div class="grid md:grid-cols-2 gap-8">
		<a href="https://wa.me/62895433711020" 
		   target="_blank"
		   class="group bg-white rounded-2xl shadow-lg p-8 hover:shadow-2xl transition-all hover:-translate-y-1">
			<div class="text-center">
				<i class="fa-brands fa-whatsapp text-6xl text-[#25D366] mb-6 group-hover:scale-110 transition"></i>
				<h2 class="font-[Kalnia] text-2xl text-[#7A2E2E] mb-4">WhatsApp</h2>
				<p class="text-gray-600 mb-6">Chat with us directly for custom orders</p>
				<span class="inline-block px-6 py-3 bg-[#25D366] text-white rounded-full font-[Kalnia] tracking-wider">
					CHAT NOW
				</span>
			</div>
		</a>
		
		<a href="https://s.shopee.co.id/6fd78uVutN?share_channel_code=1" 
		   target="_blank"
		   class="group bg-white rounded-2xl shadow-lg p-8 hover:shadow-2xl transition-all hover:-translate-y-1">
			<div class="text-center">
				<i class="fa-solid fa-shop text-6xl text-[#EE4D2D] mb-6 group-hover:scale-110 transition"></i>
				<h2 class="font-[Kalnia] text-2xl text-[#7A2E2E] mb-4">Shopee</h2>
				<p class="text-gray-600 mb-6">Order from our official Shopee store</p>
				<span class="inline-block px-6 py-3 bg-[#EE4D2D] text-white rounded-full font-[Kalnia] tracking-wider">
					SHOP NOW
				</span>
			</div>
		</a>
	</div>
</section>

<footer class="onnails-footer py-12">
	<div class="max-w-[1440px] mx-auto px-6 text-center">
		<img src="./public/images/onnailss.png" alt="ONNAILS" class="h-32 mx-auto">
	</div>
</footer>

</body>
</html>
'''

# Template untuk halaman contact  
contact_html = '''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Contact - ONNAILS</title>
	<script src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
	<link rel="stylesheet" href="./public/css/style.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
	<link href="https://fonts.googleapis.com/css2?family=Kalnia:wght@500&display=swap" rel="stylesheet">
	<script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-[#f2d6d3]">

<header x-data="{}" class="w-full onnails-navbar relative">
	<div class="max-w-[1440px] mx-auto px-6 h-[80px] flex items-center justify-between">
		<a href="./index.html" class="absolute left-1/2 -translate-x-1/2">
			<img src="./public/images/onnails.png" class="h-16 md:h-20" />
		</a>
		<a href="./index.html" class="ml-auto text-gray-800 hover:text-[#CE8A97] font-[Kalnia]">← BACK TO HOME</a>
	</div>
</header>

<section class="max-w-[800px] mx-auto px-6 py-16 min-h-[70vh]">
	<div class="text-center mb-12">
		<h1 class="font-[Kalnia] text-5xl text-[#7A2E2E] mb-6">CONTACT US</h1>
		<p class="text-xl text-gray-600">Get in touch with ONNAILS</p>
	</div>
	
	<div class="bg-white rounded-2xl shadow-lg p-8 space-y-6">
		<div class="flex items-start gap-4">
			<i class="fa-brands fa-whatsapp text-3xl text-[#25D366] mt-1"></i>
			<div>
				<h3 class="font-[Kalnia] text-xl text-[#7A2E2E] mb-2">WhatsApp</h3>
				<a href="https://wa.me/62895433711020" target="_blank" class="text-gray-600 hover:text-[#CE8A97]">
					+62 895 4337 11020
				</a>
			</div>
		</div>
		
		<div class="flex items-start gap-4">
			<i class="fa-brands fa-instagram text-3xl text-[#E4405F] mt-1"></i>
			<div>
				<h3 class="font-[Kalnia] text-xl text-[#7A2E2E] mb-2">Instagram</h3>
				<a href="https://www.instagram.com/onnailssss" target="_blank" class="text-gray-600 hover:text-[#CE8A97]">
					@onnailssss
				</a>
			</div>
		</div>
		
		<div class="flex items-start gap-4">
			<i class="fa-brands fa-tiktok text-3xl text-black mt-1"></i>
			<div>
				<h3 class="font-[Kalnia] text-xl text-[#7A2E2E] mb-2">TikTok</h3>
				<a href="https://www.tiktok.com/@onnailsss_?_r=1&_t=ZS-95HjEZLRVMg" target="_blank" class="text-gray-600 hover:text-[#CE8A97]">
					@onnailsss_
				</a>
			</div>
		</div>
	</div>
</section>

<footer class="onnails-footer py-12">
	<div class="max-w-[1440px] mx-auto px-6 text-center">
		<img src="./public/images/onnailss.png" alt="ONNAILS" class="h-32 mx-auto">
	</div>
</footer>

</body>
</html>
'''

# Template redirect sederhana
simple_redirect = '''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>{title} - ONNAILS</title>
	<meta http-equiv="refresh" content="0; url=./index.html">
	<link href="https://fonts.googleapis.com/css2?family=Kalnia:wght@500&display=swap" rel="stylesheet">
	<style>
		body {{ font-family: 'Kalnia', serif; display: flex; align-items: center; justify-content: center; min-height: 100vh; background: #f2d6d3; }}
		.message {{ text-align: center; }}
		a {{ color: #7A2E2E; }}
	</style>
</head>
<body>
	<div class="message">
		<h1>{title}</h1>
		<p>Redirecting to homepage...</p>
		<p><a href="./index.html">Click here if not redirected</a></p>
	</div>
</body>
</html>
'''

pages = {
    'booking.html': booking_html,
    'contact.html': contact_html,
    'collaboration.html': simple_redirect.format(title="Collaboration"),
    'our-service.html': simple_redirect.format(title="Our Services"),
    'terms.html': simple_redirect.format(title="Terms & Conditions"),
    'tutorial.html': simple_redirect.format(title="Tutorials"),
    'tutorial-apply.html': simple_redirect.format(title="How to Apply"),
    'tutorial-care.html': simple_redirect.format(title="Nail Care"),
    'tutorial-measure.html': simple_redirect.format(title="How to Measure"),
    'wishlist.html': simple_redirect.format(title="Wishlist/Loyalty"),
}

print("📄 Generating pages...\n")

for filename, content in pages.items():
    file_path = os.path.join(root_dir, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Created: {filename}")

print(f"\n✨ Done! Created {len(pages)} pages.")
