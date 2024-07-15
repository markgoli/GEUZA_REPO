// Custom Django Admin Menu JavaScript

document.addEventListener('DOMContentLoaded', function () {
    var menuItems = document.querySelectorAll('#header .menu-item');

    menuItems.forEach(function (menuItem) {
        menuItem.addEventListener('mouseenter', function () {
            // Add a class on hover to initiate the sliding effect
            this.classList.add('hovered');
        });

        menuItem.addEventListener('mouseleave', function () {
            // Remove the class when the cursor leaves, resetting the position
            this.classList.remove('hovered');
        });
    });
});

// custom.js
document.addEventListener('DOMContentLoaded', function () {
    const themeToggle = document.querySelector('#theme-toggle-btn');

    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            // Make an AJAX request to the server to toggle the theme
            fetch('/admin/toggle-theme/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),  // Include CSRF token
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({}),
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response as needed
                console.log(data);

                // Toggle dark mode class on the body
                document.body.classList.toggle('dark-mode');
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }

    // Function to get CSRF token from cookies
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
