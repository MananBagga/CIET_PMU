document.addEventListener("DOMContentLoaded", () => {

    const sidebar = document.getElementById('sidebar');
    const toggle = document.getElementById('sidebarToggle');
    const mainContent = document.getElementById('mainContent');

    if (toggle && sidebar && mainContent) {
        toggle.addEventListener('click', () => {
            if (window.innerWidth < 768) {
                sidebar.classList.toggle('-translate-x-full');
                mainContent.classList.toggle('translate-x-64');
            }
        });
    }


    const menuBtn = document.getElementById('menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');

    if (menuBtn && mobileMenu) {
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

        document.querySelectorAll('#mobile-menu a').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('scale-95', 'opacity-0');
                setTimeout(() => mobileMenu.classList.add('hidden'), 150);
            });
        });


        document.addEventListener('click', (e) => {
            if (!mobileMenu.contains(e.target) && !menuBtn.contains(e.target) && !mobileMenu.classList.contains('hidden')) {
                mobileMenu.classList.add('scale-95', 'opacity-0');
                setTimeout(() => mobileMenu.classList.add('hidden'), 150);
            }
        });
    }
});
