document.addEventListener("DOMContentLoaded", () => {
    // Sidebar Toggle
    const sidebar = document.getElementById("sidebar");
    const toggle = document.getElementById("sidebarToggle");
    const mainContent = document.getElementById("mainContent");

    if (sidebar && toggle) {
        toggle.addEventListener("click", () => {
            if (window.innerWidth < 1024) {
                sidebar.classList.toggle("-translate-x-full");
                if (mainContent) mainContent.classList.toggle("ml-64");
            }
        });
    }

    // Mobile Navbar Toggle
    const menuBtn = document.getElementById("menu-toggle");
    const mobileMenu = document.getElementById("mobile-menu");

    if (menuBtn && mobileMenu) {
        menuBtn.addEventListener("click", (e) => {
            e.stopPropagation(); // ✅ prevents outside click from firing
            mobileMenu.classList.toggle("hidden");
        });

        // Close menu when clicking outside of it
        document.addEventListener("click", (e) => {
            const isClickInside = mobileMenu.contains(e.target) || menuBtn.contains(e.target);
            if (!isClickInside && !mobileMenu.classList.contains("hidden")) {
                mobileMenu.classList.add("hidden");
            }
        });
    }
});
