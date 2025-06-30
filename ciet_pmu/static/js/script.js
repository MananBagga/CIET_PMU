AOS.init();
// -------------------------------------------- top bar date time ------------------------------------------------------

function updateClock() {
  const now = new Date();
  document.getElementById("time").textContent = now.toLocaleTimeString();
  document.getElementById("date").textContent = now.toLocaleDateString();
}
setInterval(updateClock, 1000);
updateClock();
