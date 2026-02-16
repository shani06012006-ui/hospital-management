console.log("MedPlus Management System Active");

document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.main-container');
    container.style.opacity = 0;
    container.style.transition = 'opacity 0.8s ease-in';
    setTimeout(() => container.style.opacity = 1, 100);
});