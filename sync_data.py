import os
import glob

# Global Replacements
html_files = glob.glob('d:/software/anti/*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Update Footer Brand
    content = content.replace(
        '<p>Precision Engineering & Complete Manufacturing Solutions. ISO 9001:2015 Certified.</p>',
        '<p>Precision Engineering · ISO 9001:2015</p>'
    )
    # Update Footer Phone
    content = content.replace(
        '+91-9845756343<br>',
        '+91-98457-56343 / +91-080-29908280<br>'
    )
    # Update Footer Links (adding LinkedIn to Connect section if not present)
    old_connect = """<h4>Connect</h4>
                    <ul>
                        <li><a href="contact.html">Contact Us</a></li>
                        <li><a href="products.html">Products</a></li>"""
    new_connect = """<h4>Connect</h4>
                    <ul>
                        <li><a href="contact.html">Contact Us</a></li>
                        <li><a href="products.html">Products</a></li>
                        <li><a href="https://www.linkedin.com/company/finetechblr/" target="_blank">LinkedIn</a></li>"""
    content = content.replace(old_connect, new_connect)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

# Specific File Updates

# index.html
with open('d:/software/anti/index.html', 'r', encoding='utf-8') as file:
    content = file.read()
content = content.replace(
    '<h1>Precision Engineering & High-Performance Tooling.</h1>',
    '<h1>Precision Engineering · CNC Machining · Special Purpose Machines · Global Exports</h1>'
)
content = content.replace(
    '<p>Manufacturers of Precision-Machined Components, SPM Parts, Special Fixtures & Robotic Assemblies.\n                    </p>',
    '<p>Precision manufacturing company specializing in high-tolerance machined components, sub-assemblies, SPM machine parts, and more.</p>'
)
# Make sure to catch single line if formatter changed it
content = content.replace(
    '<p>Manufacturers of Precision-Machined Components, SPM Parts, Special Fixtures & Robotic Assemblies.</p>',
    '<p>Precision manufacturing company specializing in high-tolerance machined components, sub-assemblies, SPM machine parts, and more.</p>'
)
with open('d:/software/anti/index.html', 'w', encoding='utf-8') as file:
    file.write(content)

# about.html
with open('d:/software/anti/about.html', 'r', encoding='utf-8') as file:
    content = file.read()
content = content.replace(
    'strong>Proto Samples</strong>, <strong>Sub-Assemblies</strong>, <strong>SPM Machine parts</strong>,\n                    <strong>Special Fixtures</strong>, and <strong>Robotic components and assemblies</strong>.',
    'strong>Proto Samples</strong>, <strong>Sub-Assemblies</strong>, <strong>SPM Machine parts</strong>, <strong>Press Components</strong>, <strong>Special Fixtures</strong>, and <strong>Robotic Assemblies</strong>.'
)
content = content.replace(
    'Renowned for high-quality production and advanced machining technology, our experienced team\n                    delivers critical components and robotic prototypes with unmatched precision. We operate from a\n                    sprawling 4400 sq. ft. facility strategically designed to handle high-precision, complex jobs while\n                    supporting scalability and growth.',
    'We serve clients across automotive, aerospace, industrial automation and robotics — providing rapid prototyping, production-ready tooling, and end-of-line (EOL) testing machines for export markets such as USA, France and China. We operate from a 4400 sq. ft. facility strategically designed to handle high-precision jobs while supporting scalability and growth.'
)
content = content.replace(
    'Our founders bring over 25 years of experience from global firms\n                    like TVS, FORD, and GM. With a strong background in automation and precision engineering, our\n                    leadership has shaped our global and robotic capabilities, allowing us to export direct to the USA,\n                    Canada, France, and China.',
    'Our founders bring over 20 years of experience from TVS, FORD and GM (PSMI). With deep domain knowledge across automation and global manufacturing, our leadership has shaped our competitive edge.'
)
with open('d:/software/anti/about.html', 'w', encoding='utf-8') as file:
    file.write(content)

# services.html
with open('d:/software/anti/services.html', 'r', encoding='utf-8') as file:
    content = file.read()
content = content.replace(
    '<p>3 high-performance CNC turning centers, including GALAXY and LMW.</p>',
    '<p>CNC Turning Centers including Galaxy Midas 6, Galaxy Midas 0, and LMW LX20T L5.</p>'
)
with open('d:/software/anti/services.html', 'w', encoding='utf-8') as file:
    file.write(content)

# products.html
with open('d:/software/anti/products.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Products replacement requires rewriting the grid completely
products_grid_old = """<div class="grid-3">
            <div class="card">
                <i data-lucide="settings-2" class="card-icon"></i>
                <h3>SPM Machines</h3>
                <p>IR Products & EOL Testing SPM Machines exported to USA, France, and China.</p>
            </div>
            <div class="card">
                <i data-lucide="test-tube" class="card-icon"></i>
                <h3>Testing Equipment</h3>
                <p>Specialized Angle Head Testing SPM Machine developed for precision verification.</p>
            </div>
            <div class="card">
                <i data-lucide="layers" class="card-icon"></i>
                <h3>Precision Shafts</h3>
                <p>Shafts crafted from 17-4Ph and P20 Grade materials for critical applications.</p>
            </div>
            <div class="card">
                <i data-lucide="package" class="card-icon"></i>
                <h3>Machined Components</h3>
                <p>High-quality parts with Case Hard, Aluminium 6061-T6, EN series, and SS304 materials.</p>
            </div>
            <div class="card">
                <i data-lucide="hexagon" class="card-icon"></i>
                <h3>Specialized Parts</h3>
                <p>Custom sub-assemblies and components incorporating Delrin and Teflon.</p>
            </div>
        </div>"""

products_grid_new = """<div class="grid-3">
            <div class="card">
                <i data-lucide="settings-2" class="card-icon"></i>
                <h3>Angle Head Testing SPMs</h3>
                <p>Specialized rigs for assembly verification and high-precision testing.</p>
            </div>
            <div class="card">
                <i data-lucide="test-tube" class="card-icon"></i>
                <h3>EOL Testing SPMs</h3>
                <p>Turnkey end-of-line testers regularly exported, including units sent to France.</p>
            </div>
            <div class="card">
                <i data-lucide="cpu" class="card-icon"></i>
                <h3>Robotic Components</h3>
                <p>Sub-assemblies and precision parts manufactured with micron-level repeatability.</p>
            </div>
            <div class="card">
                <i data-lucide="layers" class="card-icon"></i>
                <h3>Custom Fixtures & Press Parts</h3>
                <p>Engineered for longevity, stability, and high performance in production environments.</p>
            </div>
        </div>"""

content = content.replace(products_grid_old, products_grid_new)
with open('d:/software/anti/products.html', 'w', encoding='utf-8') as file:
    file.write(content)

print("Update script completed successfully.")
