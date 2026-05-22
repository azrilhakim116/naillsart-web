# ONNAILS - Static Website

## Overview
This is a fully static HTML/CSS/JavaScript version of the ONNAILS press-on nails website. It has been converted from an Express.js + EJS templating architecture to pure static files for simpler deployment and hosting.

## Project Structure

```
nailart-app/
├── index.html                    # Homepage
├── press-on.html                 # Browse all nail collections
├── our-service.html              # Services & portfolio
├── tutorial.html                 # Tutorials hub
├── tutorial-measure.html         # How to measure nails
├── tutorial-apply.html           # How to apply nails
├── tutorial-care.html            # How to care for nails
├── wishlist.html                 # Loyalty card program
├── collaboration.html            # Brand collaboration
├── booking.html                  # Booking info
├── contact.html                  # Contact information
├── terms.html                    # Terms & conditions
├── product/                      # Product detail pages
│   ├── almond.html
│   ├── square.html
│   ├── coffin.html
│   └── stilettos.html
├── public/                       # Static assets
│   ├── css/
│   │   └── style.css            # Custom styles
│   └── images/                  # Product images
└── package.json                  # Project metadata
```

## Key Features

- **100% Static HTML** - No server-side processing required
- **Alpine.js** - Client-side interactivity (navbar dropdowns, overlays)
- **Tailwind CSS** - Responsive utility-first styling (via CDN)
- **Font Awesome** - Icon library for social media and UI elements
- **Relative Linking** - All links use relative paths for easy deployment
- **Mobile Responsive** - Optimized for all screen sizes

## Deployment

This website can be deployed to any static hosting service:

### Deploy to Vercel (Recommended)

1. **Install Vercel CLI (Optional)**
   ```bash
   npm install -g vercel
   ```

2. **Deploy via CLI**
   ```bash
   vercel
   ```
   Follow the prompts to link your project.

3. **Deploy via Vercel Website**
   - Go to [vercel.com](https://vercel.com)
   - Click "Add New Project"
   - Import your Git repository (GitHub/GitLab/Bitbucket)
   - Vercel will auto-detect settings
   - Click "Deploy"

4. **Manual Settings (if needed)**
   - Framework Preset: `Other`
   - Build Command: (leave empty)
   - Output Directory: `./`
   - Install Command: (leave empty)

### Other Hosting Options

- **GitHub Pages** - Push to `gh-pages` branch
- **Netlify** - Connect repository and auto-deploy
- **Traditional Web Host** - FTP upload to public_html folder
- **Local Testing** - `npx http-server` or any local server

## Local Testing

To test locally:

```bash
# Using Python (built-in)
python -m http.server 8000

# Or using Node.js
npx http-server

# Or using PHP
php -S localhost:8000
```

Then open `http://localhost:8000` in your browser.

## Site Map

**Main Pages:**
- index.html - Homepage with product showcase
- press-on.html - All press-on collections with galleries

**Product Categories:**
- product/almond.html
- product/square.html
- product/coffin.html
- product/stilettos.html

**Information Pages:**
- our-service.html - Services and portfolio
- tutorial.html - Tutorials overview
- tutorial-measure.html - Measurement guide
- tutorial-apply.html - Application guide
- tutorial-care.html - Care guide

**Additional Pages:**
- wishlist.html - Loyalty card
- collaboration.html - Brand collaborations
- booking.html - Booking information
- contact.html - Contact details
- terms.html - Terms & conditions

## Technologies Used

- **HTML5** - Markup structure
- **CSS3** - Styling (via Tailwind CDN)
- **JavaScript** - Alpine.js framework
- **Icons** - Font Awesome 6.5.1
- **Fonts** - Google Fonts (Playfair Display, Montserrat, Kalnia, Allura)

## Browser Support

Works on all modern browsers:
- Chrome/Chromium 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Notes

- All Express.js and EJS dependencies have been removed
- `server.js` and `/routes/` and `/views/` directories have been deleted
- Images are served from the `public/images/` directory
- No build process required - serve as-is

## Maintenance

To update content:
1. Edit HTML files directly
2. Update links if adding/removing pages
3. Modify styles in `public/css/style.css`
4. Add new images to `public/images/`

All pages use consistent navbar and footer markup for easy updates across the entire site.

---

**Version:** 2.0.0 (Static HTML)  
**Last Updated:** 2024  
**Owner:** ONNAILS
