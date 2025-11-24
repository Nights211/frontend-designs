// Navigation scroll effect
const nav = document.querySelector('.nav');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
});

// Progress line
const progressLine = document.querySelector('.progress-line');
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

// Hide scroll indicator
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

// Modal functionality
const modal = document.getElementById('modal');
const modalTitle = document.getElementById('modal-title');
const modalText = document.getElementById('modal-text');
const modalClose = document.querySelector('.modal-close');

const featureData = {
    0: {
        title: 'Lightning Fast Performance',
        text: 'Our platform is optimized for speed at every level. With sub-second response times and a global edge network, your users experience instant results. Built on modern infrastructure with intelligent caching and load balancing.'
    },
    1: {
        title: 'Enterprise Security',
        text: 'Security is not an afterthought. Every request is encrypted end-to-end, data is stored with military-grade encryption, and we maintain SOC 2 Type II compliance. Your data is protected by the same security standards used by Fortune 500 companies.'
    },
    2: {
        title: 'Effortless Scaling',
        text: 'Start small, grow big. Our infrastructure automatically scales to meet your needs, whether you have 10 users or 10 million. No configuration required, no downtime, no surprises. Pay only for what you use.'
    },
    3: {
        title: 'Developer-First Integration',
        text: 'Clean, well-documented APIs that developers love. RESTful endpoints, comprehensive SDKs for all major languages, and detailed guides to get you started in minutes. Our API is designed to be intuitive and powerful.'
    }
};

// Feature items click
document.querySelectorAll('.feature-item').forEach((item, index) => {
    item.addEventListener('click', (e) => {
        e.preventDefault();
        const data = featureData[index];
        modalTitle.textContent = data.title;
        modalText.textContent = data.text;
        modal.classList.add('active');
    });
});

// Stats click
document.querySelectorAll('.stat-item').forEach(item => {
    item.addEventListener('click', (e) => {
        e.preventDefault();
        const label = item.querySelector('.stat-label').textContent;
        const value = item.querySelector('.stat-value').textContent;
        modalTitle.textContent = label;
        modalText.textContent = `We're proud to serve ${value} ${label.toLowerCase()}. This milestone represents our commitment to reliability, quality, and customer satisfaction. Join thousands of satisfied users who trust our platform every day.`;
        modal.classList.add('active');
    });
});

// Close modal
modalClose.addEventListener('click', () => {
    modal.classList.remove('active');
});

modal.addEventListener('click', (e) => {
    if (e.target === modal) {
        modal.classList.remove('active');
    }
});

// Contact form
document.querySelector('.contact-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const input = e.target.querySelector('input');
    const email = input.value;
    modalTitle.textContent = 'Thank You!';
    modalText.textContent = `We've received your email (${email}). Our team will reach out to you within 24 hours. In the meantime, feel free to explore our documentation or reach out to our support team.`;
    modal.classList.add('active');
    input.value = '';
});

// Contact info links
document.querySelectorAll('.contact-info a').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const page = link.textContent;
        modalTitle.textContent = page;
        modalText.textContent = `This is a demo template. The ${page} page would contain relevant information and resources. In a production environment, this would link to actual ${page.toLowerCase()} content.`;
        modal.classList.add('active');
    });
});

// Animate stats on scroll
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
        stat.style.opacity = '0';
        setTimeout(() => {
            stat.style.transition = 'opacity 0.5s';
            stat.style.opacity = '1';
        }, 300);
    });
}

// Smooth scroll for navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && document.querySelector(href)) {
            e.preventDefault();
            document.querySelector(href).scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
