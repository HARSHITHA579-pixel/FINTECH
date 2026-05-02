document.addEventListener('DOMContentLoaded', () => {
    // Navigation Active State Logic
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        const href = link.getAttribute('href');

        // Accurate active state matching
        if (currentPath.endsWith(href) || (currentPath === '/' && href === 'index.html')) {
            link.classList.add('active');
        }
    });

    // Theme Toggle Logic
    const themeToggleBtn = document.getElementById('theme-toggle');

    // Check for saved theme preference or use system preference
    const savedTheme = localStorage.getItem('theme');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    let currentTheme = savedTheme || (systemPrefersDark ? 'dark' : 'light');

    // Apply initial theme
    document.documentElement.setAttribute('data-theme', currentTheme);

    // Initial Icon Setup
    function updateThemeIcon(theme) {
        themeToggleBtn.innerHTML = ''; // Clear existing SVG or i tag
        const icon = document.createElement('i');
        // If theme is dark, show sun (to switch to light)
        // If theme is light, show moon (to switch to dark)
        icon.setAttribute('data-lucide', theme === 'dark' ? 'sun' : 'moon');
        themeToggleBtn.appendChild(icon);
        lucide.createIcons(); // Convert to SVG
    }

    // Set initial icon
    updateThemeIcon(currentTheme);

    themeToggleBtn.addEventListener('click', () => {
        const prevTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = prevTheme === 'dark' ? 'light' : 'dark';

        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);

        updateThemeIcon(newTheme);
    });

    // Refresh icons to apply change
    lucide.createIcons();

    // Scroll Animation Logic
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.hero-content, .page-content p, .page-content > div > div, article, .footer-content');
    animatedElements.forEach(el => {
        el.classList.add('fade-in');
        observer.observe(el);
    });

    console.log('Premium Website Loaded');
});

// Back to Top Button Logic
const backToTopBtn = document.createElement('button');
backToTopBtn.innerHTML = '<i data-lucide="arrow-up"></i>';
backToTopBtn.className = 'back-to-top';
backToTopBtn.ariaLabel = 'Back to Top';
document.body.appendChild(backToTopBtn);

// Re-initialize icons for the new button
if (window.lucide) {
    lucide.createIcons();
}

window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        backToTopBtn.classList.add('visible');
    } else {
        backToTopBtn.classList.remove('visible');
    }
});

backToTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});
