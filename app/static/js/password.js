document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        const lengthInput = document.getElementById('length');
        const length = lengthInput.value;

        if (length === '' ) {
            event.preventDefault(); 

            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'The length must be filled in.',
            });
        }else if(parseInt(length) > 200){
            event.preventDefault();

            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'The length must not exceed 200 characters.',
            });
        }else if(parseInt(length) <5){
            event.preventDefault();

            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'The length must be greater than 5 characters.',
            }); 
        }
    });
});
