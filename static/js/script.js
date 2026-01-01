// Gallery filter functionality
document.addEventListener('DOMContentLoaded', function() {
    // Gallery filtering
    const filterButtons = document.querySelectorAll('.filter-btn');
    const galleryCards = document.querySelectorAll('.gallery-card');
    
    if (filterButtons.length > 0) {
        filterButtons.forEach(button => {
            button.addEventListener('click', function() {
                // Remove active class from all buttons
                filterButtons.forEach(btn => btn.classList.remove('active'));
                // Add active class to clicked button
                this.classList.add('active');
                
                const filter = this.getAttribute('data-filter');
                
                // Filter cards
                galleryCards.forEach(card => {
                    if (filter === 'all') {
                        card.style.display = 'block';
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transform = 'scale(1)';
                        }, 10);
                    } else {
                        const status = card.getAttribute('data-status');
                        if (status === filter) {
                            card.style.display = 'block';
                            setTimeout(() => {
                                card.style.opacity = '1';
                                card.style.transform = 'scale(1)';
                            }, 10);
                        } else {
                            card.style.opacity = '0';
                            card.style.transform = 'scale(0.8)';
                            setTimeout(() => {
                                card.style.display = 'none';
                            }, 300);
                        }
                    }
                });
            });
        });
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href !== '') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
    
    // Add animation on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animatedElements = document.querySelectorAll('.contestant-card, .package-card, .feature-card, .contact-card, .gallery-card, .faq-card');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
    
    // Mobile menu toggle (if needed in future)
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (navToggle) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
    }
    
    // Copy to clipboard functionality for bank details
    const bankValues = document.querySelectorAll('.detail-value, .bank-value');
    bankValues.forEach(value => {
        value.style.cursor = 'pointer';
        value.title = 'Click to copy';
        
        value.addEventListener('click', function() {
            const text = this.textContent;
            navigator.clipboard.writeText(text).then(() => {
                // Show copied feedback
                const original = this.textContent;
                this.textContent = 'Copied!';
                this.style.color = '#25D366';
                
                setTimeout(() => {
                    this.textContent = original;
                    this.style.color = '';
                }, 1500);
            }).catch(err => {
                console.error('Failed to copy:', err);
            });
        });
    });
    
    // Update vote counts dynamically (if API is available)
    function updateVoteCounts() {
        fetch('/api/contestants')
            .then(response => response.json())
            .then(contestants => {
                contestants.forEach(contestant => {
                    const voteElements = document.querySelectorAll(`[data-contestant-id="${contestant.id}"] .votes-count, [data-contestant-id="${contestant.id}"] .votes-number, [data-contestant-id="${contestant.id}"] .current-votes`);
                    voteElements.forEach(el => {
                        el.textContent = contestant.votes;
                    });
                    
                    // Update progress bars
                    const progressBars = document.querySelectorAll(`[data-contestant-id="${contestant.id}"] .progress-fill, [data-contestant-id="${contestant.id}"] .progress-fill-large`);
                    const percentage = Math.min((contestant.votes / 400) * 100, 100);
                    progressBars.forEach(bar => {
                        bar.style.width = percentage + '%';
                    });
                });
            })
            .catch(err => console.error('Error updating votes:', err));
    }
    
    // Update votes every 30 seconds
    setInterval(updateVoteCounts, 30000);
    
    // Countdown timer (if needed for specific deadline)
    const countdownDate = new Date('April 30, 2026 23:59:59').getTime();
    
    function updateCountdown() {
        const now = new Date().getTime();
        const distance = countdownDate - now;
        
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);
        
        // Update countdown display if element exists
        const countdownElement = document.querySelector('.countdown-number');
        if (countdownElement && countdownElement.textContent.includes('Days')) {
            countdownElement.textContent = days;
        }
        
        // If countdown is finished
        if (distance < 0) {
            clearInterval(countdownInterval);
            if (countdownElement) {
                countdownElement.textContent = 'CLOSED';
            }
        }
    }
    
    const countdownInterval = setInterval(updateCountdown, 1000);
    updateCountdown();
    
    // Add sparkle effect on mouse move
    document.addEventListener('mousemove', function(e) {
        if (Math.random() > 0.95) {
            createSparkle(e.clientX, e.clientY);
        }
    });
    
    function createSparkle(x, y) {
        const sparkle = document.createElement('div');
        sparkle.className = 'sparkle-particle';
        sparkle.style.cssText = `
            position: fixed;
            left: ${x}px;
            top: ${y}px;
            width: 4px;
            height: 4px;
            background: var(--gold);
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            animation: sparkleFloat 1s ease-out forwards;
        `;
        
        document.body.appendChild(sparkle);
        
        setTimeout(() => {
            sparkle.remove();
        }, 1000);
    }
    
    // Add sparkle animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes sparkleFloat {
            0% {
                transform: translateY(0) scale(1);
                opacity: 1;
            }
            100% {
                transform: translateY(-50px) scale(0);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
});

// Add data attributes to contestant cards for vote tracking
window.addEventListener('load', function() {
    const contestantCards = document.querySelectorAll('.contestant-card, .gallery-card');
    contestantCards.forEach(card => {
        const idElement = card.querySelector('.contestant-id, .gallery-reference');
        if (idElement) {
            const id = idElement.textContent.replace('Reference: ', '').trim();
            card.setAttribute('data-contestant-id', id);
        }
    });
});
