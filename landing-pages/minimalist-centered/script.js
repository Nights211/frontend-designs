// Scroll snap navigation
const sections = document.querySelectorAll('.section');
const progressLine = document.querySelector('.progress-line');

// Update progress line on scroll
let ticking = false;
window.addEventListener('scroll', () => {
    if (!ticking) {
        window.requestAnimationFrame(() => {
            updateProgressLine();
            ticking = false;
        });
        ticking = true;
    }
});

function updateProgressLine() {
    const scrolled = window.scrollY;
    const height = document.documentElement.scrollHeight - window.innerHeight;
    const progress = (scrolled / height) * 100;
    if (progressLine) {
        progressLine.style.background = `linear-gradient(to bottom, var(--accent) ${progress}%, var(--light-gray) ${progress}%)`;
    }
}

// Hide scroll indicator after first scroll
let hasScrolled = false;
window.addEventListener('scroll', () => {
    if (!hasScrolled && window.scrollY > 50) {
        hasScrolled = true;
        const scrollIndicator = document.querySelector('.scroll-indicator');
        if (scrollIndicator) {
            scrollIndicator.style.opacity = '0';
            scrollIndicator.style.transition = 'opacity 0.5s';
        }
    }
});

// Form submission
document.querySelector('.contact-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const input = e.target.querySelector('input');
    alert('This is a demo. Form submission not implemented.');
    input.value = '';
});

// CTA button
document.querySelector('.cta-btn').addEventListener('click', () => {
    alert('This is a demo template. Button action not implemented.');
});

// Animate stats on scroll into view
const numberSection = document.querySelector('.number-section');
let statsAnimated = false;

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting && !statsAnimated) {
            animateStats();
            statsAnimated = true;
        }
    });
}, { threshold: 0.5 });

if (numberSection) {
    observer.observe(numberSection);
}

function animateStats() {
    const statValues = document.querySelectorAll('.stat-value');
    statValues.forEach(stat => {
        const text = stat.textContent;
        stat.style.opacity = '0';
        setTimeout(() => {
            stat.style.transition = 'opacity 0.5s';
            stat.style.opacity = '1';
        }, 300);
    });
}
