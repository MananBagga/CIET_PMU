// // AOS.init();
// // -------------------------------------------- top bar date time ------------------------------------------------------

// function updateClock() {
//   const now = new Date();
//   document.getElementById("time").textContent = now.toLocaleTimeString();
//   document.getElementById("date").textContent = now.toLocaleDateString();
// }
// setInterval(updateClock, 1000);
// updateClock();



// --------------------------------------------------------------------


document.addEventListener("DOMContentLoaded", () => {
    const sidebar = document.getElementById('sidebar');
    const toggle = document.getElementById('sidebarToggle');
    const mainContent = document.getElementById('mainContent');

    if (toggle && sidebar && mainContent) {
        toggle.addEventListener('click', () => {
            // Only toggle when screen is < md breakpoint
            if (window.innerWidth < 768) {
                sidebar.classList.toggle('-translate-x-full');
                mainContent.classList.toggle('translate-x-64');
            }
        });
    }
});


document.addEventListener("DOMContentLoaded", function () {
    const menuBtn = document.getElementById('menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');

    if (!menuBtn || !mobileMenu) {
        console.error("Navbar elements not found!");
        return;
    }

    menuBtn.addEventListener('click', () => {
        const isHidden = mobileMenu.classList.contains('hidden');

        if (isHidden) {
            mobileMenu.classList.remove('hidden');
            setTimeout(() => {
                mobileMenu.classList.remove('scale-95', 'opacity-0');
                mobileMenu.classList.add('scale-100', 'opacity-100');
            }, 10);
        } else {
            mobileMenu.classList.add('scale-95', 'opacity-0');
            setTimeout(() => mobileMenu.classList.add('hidden'), 150);
        }
    });

    // Auto close when clicking a link
    document.querySelectorAll('#mobile-menu a').forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.add('scale-95', 'opacity-0');
            setTimeout(() => mobileMenu.classList.add('hidden'), 150);
        });
    });

    // Auto close when clicking outside
    document.addEventListener('click', (e) => {
        if (!mobileMenu.contains(e.target) && !menuBtn.contains(e.target) && !mobileMenu.classList.contains('hidden')) {
            mobileMenu.classList.add('scale-95', 'opacity-0');
            setTimeout(() => mobileMenu.classList.add('hidden'), 150);
        }
    });
});

