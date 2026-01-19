/* ================================ ENVÍO DEL FORMULARIO DE CONTACTO ================================ */

// Escucha el evento submit del formulario
document.getElementById("contactForm").addEventListener("submit", function (e) {

    // Evita que el formulario recargue la página
    e.preventDefault();

    // Referencia al formulario actual
    const form = this;

    // Crea un objeto FormData con todos los campos del formulario
    const formData = new FormData(form);

    /* ================================ CONFIGURACIÓN DEL TOAST ================================ */
    const Toast = Swal.mixin({
        toast: true, // Activa el modo toast
        position: "top-end", // Posición en la esquina superior derecha
        showConfirmButton: false, // Oculta el botón de confirmación
        timer: 3000, // Duración del toast (3 segundos)
        timerProgressBar: true, // Muestra barra de progreso
        didOpen: (toast) => {
            // Pausa el temporizador al pasar el mouse
            toast.onmouseenter = Swal.stopTimer;
            // Reanuda el temporizador al quitar el mouse
            toast.onmouseleave = Swal.resumeTimer;
        }
    });

    /* ================================ ENVÍO AJAX CON FETCH ================================ */
    fetch("/", {
        method: "POST", // Método HTTP
        headers: {
            // Indica que es una petición AJAX
            "X-Requested-With": "XMLHttpRequest",
        },
        body: formData // Datos del formulario
    })

    // Convierte la respuesta a JSON
    .then(response => response.json())

    // Procesa la respuesta del servidor
    .then(data => {

        // Muestra el mensaje recibido del backend
        Toast.fire({
            icon: data.status, // success | error | warning
            title: data.message // Mensaje del servidor
        });

        // Si el envío fue exitoso
        if (data.status === "success") {
            form.reset(); // Limpia el formulario
        }
    })

    /* ================================ MANEJO DE ERRORES ================================ */
    .catch(() => {
        // Muestra un mensaje genérico de error
        Toast.fire({
            icon: "error",
            title: "Error inesperado ❌"
        });
    });
});