import os
import glob

html_files = glob.glob('d:/software/anti/*.html')

# CSS Updates via file replace to avoid multireplace syntax issues
# Update style.css directly by rewriting it
with open('d:/software/anti/style.css', 'r', encoding='utf-8') as file:
    css = file.read()

# 1. Update primary gradient to be richer
css = css.replace(
    '--gradient-main: linear-gradient(135deg, var(--text-main) 0%, var(--text-muted) 100%);',
    '--gradient-main: linear-gradient(135deg, #0f172a 0%, #059669 50%, #10b981 100%);'
)
css = css.replace(
    '--gradient-main: linear-gradient(135deg, #ffffff 0%, #94a3b8 100%);',
    '--gradient-main: linear-gradient(135deg, #ffffff 0%, #34d399 50%, #10b981 100%);'
)

# 2. Update background image for a moving mesh-like feel rather than static dots
css = css.replace(
    '''background-image: radial-gradient(circle at top right, rgba(16, 185, 129, 0.05), transparent 40%),
    radial-gradient(circle at bottom left, rgba(16, 185, 129, 0.05), transparent 40%);''',
    '''background-image: 
        radial-gradient(circle at 15% 50%, rgba(16, 185, 129, 0.08), transparent 40%),
        radial-gradient(circle at 85% 30%, rgba(5, 150, 105, 0.08), transparent 40%),
        radial-gradient(circle at 50% 80%, rgba(52, 211, 153, 0.08), transparent 40%);
  background-size: 200% 200%;
  animation: bgPulse 20s ease infinite;'''
)

# 3. Add background pulse keyframes if not exist, and update hero grid for index.html dynamic element
keyframe_append = '''

@keyframes bgPulse {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.hero-visuals {
  position: relative;
  width: 100%;
  height: 400px;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2;
  perspective: 1000px;
}

.geometric-shape {
  width: 300px;
  height: 300px;
  background: linear-gradient(135deg, rgba(16,185,129,0.2) 0%, rgba(5,150,105,0.4) 100%);
  border: 1px solid rgba(16,185,129,0.5);
  border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
  box-shadow: 0 0 40px rgba(16,185,129,0.2), inset 0 0 40px rgba(16,185,129,0.2);
  animation: morph 8s ease-in-out infinite alternate;
  backdrop-filter: blur(10px);
}

.geometric-shape::after {
  content: '';
  position: absolute;
  top: 10%;
  left: 10%;
  right: 10%;
  bottom: 10%;
  border: 1px dotted rgba(255,255,255,0.3);
  border-radius: inherit;
  animation: spin 20s linear infinite;
}

@keyframes morph {
  0% { border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%; transform: rotate(0deg) scale(1); box-shadow: 0 0 40px rgba(16,185,129,0.2); }
  33% { border-radius: 50% 50% 20% 80% / 25% 80% 20% 75%; transform: rotate(10deg) scale(1.05); box-shadow: 0 0 60px rgba(16,185,129,0.4); }
  66% { border-radius: 80% 20% 50% 50% / 80% 25% 75% 20%; transform: rotate(-10deg) scale(0.95); box-shadow: 0 0 40px rgba(5,150,105,0.3); }
  100% { border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%; transform: rotate(0deg) scale(1); box-shadow: 0 0 40px rgba(16,185,129,0.2); }
}

@keyframes spin {
  100% { transform: rotate(360deg); }
}
'''
if '@keyframes bgPulse' not in css:
    css += keyframe_append

# 4. Enhance navbar glass blur
css = css.replace('backdrop-filter: blur(20px);', 'backdrop-filter: blur(30px);')

# 5. Fix hero grid columns for the animated shape
css = css.replace(
    '''.hero-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 60px;
  align-items: center;
  text-align: center;
  max-width: 900px;
  margin: 0 auto;
}

/* Center hero content when visuals are missing */
@media (min-width: 901px) {
  .hero-grid {
    grid-template-columns: 1fr;
  }
}''',
    '''.hero-grid {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 60px;
  align-items: center;
  text-align: left;
  max-width: 1280px;
  margin: 0 auto;
}

@media (min-width: 901px) {
  .hero-grid {
    grid-template-columns: 1.1fr 0.9fr;
  }
}'''
)

# 6. Apply card hover dynamic border
card_hover = '''
.card::after {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  border-radius: 20px;
  box-shadow: 0 0 0 2px var(--primary-color);
  opacity: 0;
  transform: scale(0.95);
  transition: all 0.4s ease;
  pointer-events: none;
}

.card:hover::after {
  opacity: 1;
  transform: scale(1);
}
'''
if '.card::after' not in css:
    css += card_hover

with open('d:/software/anti/style.css', 'w', encoding='utf-8') as file:
    file.write(css)

# Update index.html
with open('d:/software/anti/index.html', 'r', encoding='utf-8') as file:
    index_html = file.read()

index_html = index_html.replace(
    '<!-- Hero visuals removed -->',
    '<div class="hero-visuals"><div class="geometric-shape"></div></div>'
)

with open('d:/software/anti/index.html', 'w', encoding='utf-8') as file:
    file.write(index_html)

print("Aesthetics updated.")
