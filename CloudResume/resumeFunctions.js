<script>
    document.querySelectorAll('.navigation-bar a').forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default navigation behavior

            var pageId = this.getAttribute('href').substring(1); // Get the target page ID
            var currentPage = document.querySelector('.page:not(.hidden)'); // Get the currently visible page

            if (currentPage) {
                currentPage.classList.add('hidden'); // Hide the currently visible page
            }

            document.getElementById(pageId).classList.remove('hidden'); // Show the target page
        });
    });
</script>