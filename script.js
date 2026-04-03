// script.js

// Set the date we're counting down to
const countDownDate = new Date("Apr 25, 2026 11:00:00").getTime();

// Update the count down every 1 second
const x = setInterval(function() {

  // Get today's date and time
  const now = new Date().getTime();

  // Find the distance between now and the count down date
  const distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  const days = Math.floor(distance / (1000 * 60 * 60 * 24));
  const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the elements safely handling possible missing elements
  const elDays = document.getElementById("days");
  const elHours = document.getElementById("hours");
  const elMins = document.getElementById("minutes");
  const elSecs = document.getElementById("seconds");
  
  if (elDays) elDays.innerHTML = formatNumber(days);
  if (elHours) elHours.innerHTML = formatNumber(hours);
  if (elMins) elMins.innerHTML = formatNumber(minutes);
  if (elSecs) elSecs.innerHTML = formatNumber(seconds);

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("countdown-timer").innerHTML = "<h3 style='color: var(--color-green);'>¡Llegó el gran día!</h3>";
  }
}, 1000);

function formatNumber(number) {
    return number < 10 ? "0" + number : number;
}

// ======== REPRODUCTOR DE MÚSICA Y WELCOME OVERLAY ========
const audioPlayer = document.getElementById('local-audio');
const welcomeOverlay = document.getElementById('welcome-overlay');
const btnOpenInvite = document.getElementById('btn-open-invite');
let hasStarted = false;

const START_TIME = 21;
const END_TIME = 110;

// Evitar scroll lateral y vertical mientras está el overlay
document.body.style.overflow = 'hidden';

audioPlayer.addEventListener('timeupdate', () => {
    if (audioPlayer.currentTime >= END_TIME) {
        audioPlayer.currentTime = START_TIME;
    }
});

btnOpenInvite.addEventListener('click', () => {
    // Al hacer click explícito en este botón, el navegador SÍ permite audio
    if (audioPlayer.currentTime < START_TIME || audioPlayer.currentTime >= END_TIME) {
        audioPlayer.currentTime = START_TIME;
    }
    
    audioPlayer.play().then(() => {
        hasStarted = true;
    }).catch(e => {
        console.log('Autoplay prevenido:', e);
    });

    // Desaparecer el overlay
    welcomeOverlay.classList.add('hidden');
    
    // Reactivar el scroll normal
    document.body.style.overflow = 'auto';
    document.body.style.overflowX = 'hidden'; // Mantener oculto scroll lateral por el diseño
});

// ======== EFECTO DE CHISPAS DORADAS ========
document.addEventListener("DOMContentLoaded", () => {
    const sparksContainer = document.createElement('div');
    sparksContainer.id = 'sparks-container';
    document.getElementById('hero').appendChild(sparksContainer);

    const createSpark = () => {
        const spark = document.createElement('div');
        spark.classList.add('spark');
        
        // Randomizar posición inicial (a lo ancho de la pantalla)
        spark.style.left = Math.random() * 100 + 'vw';
        
        // Randomizar tamaño de la chispa (entre 3px y 8px)
        const size = Math.random() * 5 + 3;
        spark.style.width = size + 'px';
        spark.style.height = size + 'px';
        
        // Randomizar duración de caída para que se vea natural (entre 6s y 15s)
        const duration = Math.random() * 9 + 6;
        spark.style.animationDuration = duration + 's';
        
        sparksContainer.appendChild(spark);
        
        // Eliminar del DOM después de que termine la animación
        setTimeout(() => {
            spark.remove();
        }, duration * 1000); 
    };

    // Crear una chispa cada 400 milisegundos para un efecto estelar elegante
    setInterval(createSpark, 400);
});