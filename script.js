(function () {
  var links = document.querySelectorAll('nav a');
  var current = window.location.pathname.split('/').pop() || 'index.html';

  links.forEach(function (link) {
    if (link.getAttribute('href') === current) {
      link.classList.add('active');
    }
  });

  var bookingForm = document.getElementById('booking-form');
  var bookingMessage = document.getElementById('booking-message');

  if (bookingForm && bookingMessage) {
    bookingForm.addEventListener('submit', function (event) {
      event.preventDefault();

      if (!bookingForm.checkValidity()) {
        bookingMessage.textContent = 'Please complete all required fields before submitting.';
        bookingMessage.className = 'form-message error';
        bookingForm.reportValidity();
        return;
      }

      var bookingName = bookingForm.elements.name.value.trim();
      bookingMessage.textContent = 'Thank you, ' + bookingName + '! Your booking request has been received.';
      bookingMessage.className = 'form-message success';
      bookingForm.reset();
    });
  }

  var contactForm = document.getElementById('contact-form');
  var contactStatus = document.getElementById('contact-message-status');

  if (contactForm && contactStatus) {
    contactForm.addEventListener('submit', function (event) {
      event.preventDefault();

      if (!contactForm.checkValidity()) {
        contactStatus.textContent = 'Please complete all required fields before sending your message.';
        contactStatus.className = 'form-message error';
        contactForm.reportValidity();
        return;
      }

      var contactName = contactForm.elements.name.value.trim();
      contactStatus.textContent = 'Thanks, ' + contactName + '! Your message has been sent.';
      contactStatus.className = 'form-message success';
      contactForm.reset();
    });
  }
})();
