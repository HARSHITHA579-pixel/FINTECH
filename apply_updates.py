import os
import glob

html_files = glob.glob('d:/software/anti/*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('images/logo.jpg', 'images/logo.png')
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

# Update index.html
with open('d:/software/anti/index.html', 'r', encoding='utf-8') as file:
    index_html = file.read()
index_html = index_html.replace('<!-- Hero visuals removed -->', '<div class="hero-visuals">\n                    <img src="images/cnc_lathe_lmw.png" alt="High Performance CNC Lathe" class="hero-image">\n                </div>')
with open('d:/software/anti/index.html', 'w', encoding='utf-8') as file:
    file.write(index_html)

# Update services.html
with open('d:/software/anti/services.html', 'r', encoding='utf-8') as file:
    services = file.read()
services = services.replace('<p>3 high-performance CNC turning centers, including GALAXY and LMW.</p>', '<p>3 high-performance CNC turning centers, including GALAXY and LMW.</p>\n                <img src="images/cnc_lathe_lmw.png" alt="CNC Turning" class="card-image">')
services = services.replace('<p>3 VMCs from COSMOS and BFW with 4th-axis capability for high-speed milling and complex contouring.\n                </p>', '<p>3 VMCs from COSMOS and BFW with 4th-axis capability for high-speed milling and complex contouring.\n                </p>\n                <img src="images/vmc_cosmos.png" alt="Vertical Machining Center" class="card-image">')
services = services.replace('<p>Dedicated Quality Room with 10+ Mitutoyo tools, Digital Height Gauge, and Profile Projector for\n                    zero-defect output.</p>', '<p>Dedicated Quality Room with 10+ Mitutoyo tools, Digital Height Gauge, and Profile Projector for\n                    zero-defect output.</p>\n                <img src="images/inspection_height_gauge.png" alt="Quality Assurance" class="card-image">')
with open('d:/software/anti/services.html', 'w', encoding='utf-8') as file:
    file.write(services)

# Update products.html
with open('d:/software/anti/products.html', 'r', encoding='utf-8') as file:
    products = file.read()
products = products.replace('<p>Specialized Angle Head Testing SPM Machine developed for precision verification.</p>', '<p>Specialized Angle Head Testing SPM Machine developed for precision verification.</p>\n                <img src="images/profile_projector.png" alt="Profile Projector" class="card-image">')
with open('d:/software/anti/products.html', 'w', encoding='utf-8') as file:
    file.write(products)

print("HTML pages updated successfully.")
