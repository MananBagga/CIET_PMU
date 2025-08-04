document.addEventListener("DOMContentLoaded", () => {
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

    const menuBtn = document.getElementById("menu-toggle");
    const mobileMenu = document.getElementById("mobile-menu");

    if (menuBtn && mobileMenu) {
        menuBtn.addEventListener("click", (e) => {
            e.stopPropagation(); 
            mobileMenu.classList.toggle("hidden");
        });

        document.addEventListener("click", (e) => {
            const isClickInside = mobileMenu.contains(e.target) || menuBtn.contains(e.target);
            if (!isClickInside && !mobileMenu.classList.contains("hidden")) {
                mobileMenu.classList.add("hidden");
            }
        });
    }
});




document.addEventListener("DOMContentLoaded", function () {
    const rows = document.querySelectorAll(".table-row-item");
    const loadMoreBtn = document.getElementById("loadMoreBtn");
    const showAllBtn = document.getElementById("showAllBtn");

    let visibleCount = 5; 
    function showRows(count) {
        rows.forEach((row, index) => {
            row.style.display = index < count ? "" : "none";
        });
    }

    showRows(visibleCount);

    loadMoreBtn.addEventListener("click", function () {
        visibleCount += 5;
        showRows(visibleCount);

        if (visibleCount >= rows.length) {
            loadMoreBtn.style.display = "none";
        }
    });

    showAllBtn.addEventListener("click", function () {
        visibleCount = rows.length;
        showRows(visibleCount);
        loadMoreBtn.style.display = "none"; 
    });
});
