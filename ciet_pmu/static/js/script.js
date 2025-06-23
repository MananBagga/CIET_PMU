// -------------------------------------------- top bar date time ------------------------------------------------------

function updateClock() {
  const now = new Date();
  document.getElementById("time").textContent = now.toLocaleTimeString();
  document.getElementById("date").textContent = now.toLocaleDateString();
}
setInterval(updateClock, 1000);
updateClock();


// -------------------------------------------- search icon ---------------------------------------------------------------

function toggleSearch() {
  const form = document.getElementById("searchForm");
  form.classList.toggle("hidden");
  if (!form.classList.contains("hidden")) {
    form.querySelector("input").focus();
  }
}

// ------------------------------------------------- hero section ----------------------------------------------------------

// Modal Control
function openModal() {
  document.getElementById("authModal").classList.remove("hidden");
}
function closeModal() {
  document.getElementById("authModal").classList.add("hidden");
}
