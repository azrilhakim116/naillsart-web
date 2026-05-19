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

  if (!bookingForm || !bookingMessage) {
    return;
  }

  bookingForm.addEventListener('submit', function (event) {
    event.preventDefault();

    if (!bookingForm.checkValidity()) {
      bookingMessage.textContent = 'Please complete all required fields before submitting.';
      bookingMessage.className = 'form-message error';
      bookingForm.reportValidity();
      return;
    }

    var name = bookingForm.elements.name.value.trim();
    bookingMessage.textContent = 'Thank you, ' + name + '! Your booking request has been received.';
    bookingMessage.className = 'form-message success';
    bookingForm.reset();
  });
})();
