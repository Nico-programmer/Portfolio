// ! MENÚ DESPLEGABLE (NAVBAR MOBILE)

// ? Selecciona el ícono del menú
let menuIcon = document.querySelector('#menu-icon');

// ? Selecciona la barra de navegación
let navbar = document.querySelector('.navbar');

// ? Evento click para abrir/cerrar el menú
menuIcon.onclick = () => {
    // Cambia el ícono de hamburguesa a cerrar
    menuIcon.classList.toggle('fa-bars');
    menuIcon.classList.toggle('fa-xmark');

    // Muestra u oculta el menú
    navbar.classList.toggle('active');
};

// ! ENLACE ACTIVO SEGÚN SECCIÓN

// Selecciona todas las secciones
let sections = document.querySelectorAll('section');

// Selecciona todos los enlaces del navbar
let navLinks = document.querySelectorAll('header nav a');

// Evento al hacer scroll
window.onscroll = () => {

    // Recorre cada sección
    sections.forEach(sec => {
        let top = window.scrollY; // Posición actual del scroll
        let offset = sec.offsetTop - 150; // Inicio de la sección
        let height = sec.offsetHeight; // Altura de la sección
        let id = sec.getAttribute('id'); // ID de la sección

        // Verifica si el scroll está dentro de la sección
        if (top >= offset && top < offset + height) {

            // Elimina la clase active de todos los enlaces
            navLinks.forEach(link => link.classList.remove('active'));

            // Activa el enlace correspondiente a la sección visible
            document
                .querySelector(`header nav a[href*="${id}"]`)
                ?.classList.add('active');
        }
    });

    /* ================================ NAVBAR STICKY ================================ */

    // Selecciona el header
    let header = document.querySelector('header');

    // Agrega la clase sticky al hacer scroll
    header.classList.toggle('sticky', window.scrollY > 100);

    /* ================================ CERRAR MENÚ AL HACER SCROLL ================================ */

    // Restaura el ícono del menú
    menuIcon.classList.remove('fa-xmark');
    menuIcon.classList.add('fa-bars');

    // Oculta el menú
    navbar.classList.remove('active');
};

/* ================================ ANIMACIONES SCROLL REVEAL ================================ */

// Configuración global de ScrollReveal
ScrollReveal({
    // reset: true, /* Reinicia animaciones (opcional) */
    distance: '80px', // Distancia del desplazamiento
    duration: 2000, // Duración de la animación
    display: 200 // Retardo antes de mostrarse
});

// Animaciones desde arriba
ScrollReveal().reveal('.home-content, .heading', { origin: 'top' });

// Animaciones desde abajo
ScrollReveal().reveal(
    '.home-img, .services-container, .portfolio-box, .contact form',
    { origin: 'bottom' }
);

// Animaciones desde la izquierda
ScrollReveal().reveal('.home-content h1, .about-img', { origin: 'left' });

// Animaciones desde la derecha
ScrollReveal().reveal('.home-content p, .about-content', { origin: 'right' });

/* ================================ EFECTO DE TEXTO (TYPED.JS) ================================ */

// Inicializa Typed.js
const typed = new Typed('.multiple-text', {
    strings: ['Desarrollador de software', 'Analista de software'], // Textos animados
    typeSpeed: 100, // Velocidad de escritura
    backSpeed: 100, // Velocidad de borrado
    backDelay: 1000, // Tiempo antes de borrar
    loop: true // Repite la animación
});