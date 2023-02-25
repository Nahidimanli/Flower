
    ContactUsLogic = {
        emailManager(email,) {
            fetch('/core/api/contactus/', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token }}'
                },
                body: JSON.stringify({
                    'email': email,
                })
            })
                .then(response => response.json())
                .then(data => {
                    contactusModalLongTitle = document.getElementById('contactusModalLongTitle');
                    emailinput.value = '';
                })
            }
    }

    sendbutton = document.getElementById('sendbutton')
    emailinput = document.getElementById('emailinput')

    sendbutton.onclick = function (e) {
        e.preventDefault();
        email = emailinput.value,
        ContactUsLogic.emailManager(email);
    }

