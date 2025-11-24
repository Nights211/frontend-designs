// Scroll progress
window.addEventListener('scroll', () => {
    const scrollProgress = document.querySelector('.scroll-progress');
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrolled = (window.scrollY / scrollHeight) * 100;
    scrollProgress.style.width = scrolled + '%';
});

// Sticky nav
const nav = document.getElementById('nav');
window.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
});

// Hamburger menu
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');
hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Counter animation
const animateCounter = (element) => {
    const target = parseFloat(element.dataset.target);
    const isDecimal = target % 1 !== 0;
    const duration = 2000;
    const increment = target / (duration / 16);
    let current = 0;
    
    const updateCounter = () => {
        current += increment;
        if (current < target) {
            if (isDecimal) {
                element.textContent = current.toFixed(1);
            } else if (target > 1000000) {
                element.textContent = (current / 1000000).toFixed(1) + 'M+';
            } else if (target > 1000) {
                element.textContent = (current / 1000).toFixed(0) + 'K+';
            } else {
                element.textContent = Math.floor(current);
            }
            requestAnimationFrame(updateCounter);
        } else {
            if (isDecimal) {
                element.textContent = target + '%';
            } else if (target > 1000000) {
                element.textContent = (target / 1000000).toFixed(0) + 'M+';
            } else if (target > 1000) {
                element.textContent = (target / 1000).toFixed(0) + 'K+';
            } else {
                element.textContent = target;
            }
        }
    };
    
    updateCounter();
};

const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const counters = entry.target.querySelectorAll('[data-target]');
            counters.forEach(counter => animateCounter(counter));
            statsObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

const statsSection = document.querySelector('.stats');
if (statsSection) statsObserver.observe(statsSection);

// Tabs
const tabs = document.querySelectorAll('.tab');
const tabPanels = document.querySelectorAll('.tab-panel');

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const targetTab = tab.dataset.tab;
        
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        
        tabPanels.forEach(panel => {
            if (panel.dataset.panel === targetTab) {
                panel.classList.add('active');
            } else {
                panel.classList.remove('active');
            }
        });
    });
});

// Copy code
document.querySelectorAll('.copy-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const codeId = btn.dataset.copy;
        const code = document.getElementById(codeId).textContent;
        navigator.clipboard.writeText(code).then(() => {
            showToast('Code copied to clipboard!');
        });
    });
});

// Typing animation for demo
const typingText = document.querySelector('.typing-text');
const demoText = "Quantum computing is a revolutionary approach to computation that leverages quantum mechanical phenomena...";
let charIndex = 0;

const typeWriter = () => {
    if (charIndex < demoText.length) {
        typingText.textContent += demoText.charAt(charIndex);
        charIndex++;
        setTimeout(typeWriter, 30);
    }
};

const demoObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            setTimeout(typeWriter, 500);
            demoObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

const demoSection = document.querySelector('.demo');
if (demoSection) demoObserver.observe(demoSection);

// Carousel
let currentSlide = 0;
const testimonials = document.querySelectorAll('.testimonial');
const prevBtn = document.querySelector('.carousel-btn.prev');
const nextBtn = document.querySelector('.carousel-btn.next');

const showSlide = (index) => {
    testimonials.forEach((testimonial, i) => {
        if (i === index) {
            testimonial.classList.add('active');
        } else {
            testimonial.classList.remove('active');
        }
    });
};

if (testimonials.length > 0) {
    showSlide(0);
    
    prevBtn.addEventListener('click', () => {
        currentSlide = (currentSlide - 1 + testimonials.length) % testimonials.length;
        showSlide(currentSlide);
    });
    
    nextBtn.addEventListener('click', () => {
        currentSlide = (currentSlide + 1) % testimonials.length;
        showSlide(currentSlide);
    });
    
    setInterval(() => {
        currentSlide = (currentSlide + 1) % testimonials.length;
        showSlide(currentSlide);
    }, 5000);
}

// FAQ accordion
document.querySelectorAll('.faq-question').forEach(question => {
    question.addEventListener('click', () => {
        const faqItem = question.parentElement;
        const isActive = faqItem.classList.contains('active');
        
        document.querySelectorAll('.faq-item').forEach(item => {
            item.classList.remove('active');
        });
        
        if (!isActive) {
            faqItem.classList.add('active');
        }
    });
});

// Scroll to top button
const scrollTopBtn = document.querySelector('.scroll-top');
window.addEventListener('scroll', () => {
    if (window.scrollY > 500) {
        scrollTopBtn.classList.add('visible');
    } else {
        scrollTopBtn.classList.remove('visible');
    }
});

scrollTopBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Toast notification
const showToast = (message) => {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.classList.add('show');
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
};

// Form submissions
document.getElementById('hero-form').addEventListener('submit', (e) => {
    e.preventDefault();
    showToast('Thanks! We\'ll be in touch soon.');
    e.target.reset();
});

document.getElementById('newsletter-form').addEventListener('submit', (e) => {
    e.preventDefault();
    showToast('Successfully subscribed to newsletter!');
    e.target.reset();
});

// Pricing buttons
document.querySelectorAll('.pricing-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const plan = btn.dataset.plan;
        if (plan === 'enterprise') {
            openModal('contact-modal');
        } else {
            openModal('signup-modal');
        }
    });
});

// Nav CTA button
document.querySelector('.nav-cta').addEventListener('click', () => {
    openModal('signup-modal');
});

// Modal functions
const openModal = (modalId) => {
    const modal = document.getElementById(modalId);
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
};

const closeModal = (modal) => {
    modal.classList.remove('active');
    document.body.style.overflow = '';
};

// Close modal buttons
document.querySelectorAll('.modal-close').forEach(btn => {
    btn.addEventListener('click', () => {
        closeModal(btn.closest('.modal'));
    });
});

// Close modal on backdrop click
document.querySelectorAll('.modal').forEach(modal => {
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal(modal);
        }
    });
});

// Switch between login and signup
document.getElementById('switch-to-login').addEventListener('click', (e) => {
    e.preventDefault();
    closeModal(document.getElementById('signup-modal'));
    openModal('login-modal');
});

document.getElementById('switch-to-signup').addEventListener('click', (e) => {
    e.preventDefault();
    closeModal(document.getElementById('login-modal'));
    openModal('signup-modal');
});

// Forgot password
document.getElementById('forgot-password').addEventListener('click', (e) => {
    e.preventDefault();
    showToast('Password reset link sent to your email!');
});

// Signup form
document.getElementById('signup-form').addEventListener('submit', (e) => {
    e.preventDefault();
    showToast('Account created successfully! Welcome to Neural.');
    closeModal(document.getElementById('signup-modal'));
    e.target.reset();
});

// Login form
document.getElementById('login-form').addEventListener('submit', (e) => {
    e.preventDefault();
    showToast('Welcome back! Redirecting to dashboard...');
    closeModal(document.getElementById('login-modal'));
    e.target.reset();
});

// Contact form
document.getElementById('contact-form').addEventListener('submit', (e) => {
    e.preventDefault();
    showToast('Thanks for reaching out! Our team will contact you within 24 hours.');
    closeModal(document.getElementById('contact-modal'));
    e.target.reset();
});

// Footer links
document.querySelectorAll('.footer-link').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const action = link.dataset.action;
        
        switch(action) {
            case 'docs':
                openModal('docs-modal');
                break;
            case 'api':
                openModal('api-modal');
                break;
            case 'support':
                showToast('Opening support chat...');
                setTimeout(() => {
                    showToast('Support: How can we help you today?');
                }, 1500);
                break;
            case 'about':
                showToast('Neural was founded in 2024 to democratize AI access.');
                break;
            case 'blog':
                showToast('Redirecting to blog...');
                break;
            case 'careers':
                showToast('We\'re hiring! Check out our open positions.');
                break;
        }
    });
});

// Documentation navigation
document.querySelectorAll('.docs-link').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetDoc = link.dataset.doc;
        
        // Update active link
        document.querySelectorAll('.docs-link').forEach(l => l.classList.remove('active'));
        link.classList.add('active');
        
        // Show target section
        document.querySelectorAll('.doc-section').forEach(section => {
            if (section.dataset.section === targetDoc) {
                section.classList.add('active');
            } else {
                section.classList.remove('active');
            }
        });
    });
});

// Keyboard shortcuts
document.addEventListener('keydown', (e) => {
    // ESC to close modals
    if (e.key === 'Escape') {
        document.querySelectorAll('.modal.active').forEach(modal => {
            closeModal(modal);
        });
    }
    
    // Ctrl/Cmd + K to open docs
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        openModal('docs-modal');
    }
});

// Intersection Observer for animations
const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll('.feature-card, .timeline-item, .pricing-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s, transform 0.6s';
    fadeObserver.observe(el);
});
