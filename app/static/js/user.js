document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
       
        const inputs = form.querySelectorAll('input:not([type="hidden"])');

        
        const allFilled = Array.from(inputs).every(input => input.value.trim() !== '');

        if (!allFilled) {
            event.preventDefault(); 
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'All fields must be filled out.',
            });
        }
    });
});
