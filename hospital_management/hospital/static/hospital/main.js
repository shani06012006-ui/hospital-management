console.log("MedPlus Management System Active");

// Add a simple fade-in effect to the container
document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.main-container');
    container.style.opacity = 0;
    container.style.transition = 'opacity 0.8s ease-in';
    setTimeout(() => container.style.opacity = 1, 100);
});