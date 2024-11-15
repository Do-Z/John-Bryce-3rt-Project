// displaying an alert before deleting vacation
function confirmDelete(){
    const ok = confirm ("Are you sure?")
    if (!ok){
        event.preventDefault()
    }
}

// displaying the error for 5 seconds
const errorSpan = document.querySelector(".error");
if(errorSpan){
    setTimeout(() => {
        errorSpan.parentNode.removeChild(errorSpan);
    }, 5000);
}

// displaying the selected country as the selected option in the dropdown
document.addEventListener('DOMContentLoaded', function(){
    const dropdownItems = document.querySelectorAll('.dropdown-item')
    const dropdownButton = document.getElementById('countryDropdown')
    const countryInput = document.getElementById('country-input')
    dropdownItems.forEach(item => {
        item.addEventListener('click', function(event){
            event.preventDefault();
            const selectedCountry = this.getAttribute('data-value');
            const selectedFlag = this.querySelector('.flag-icon').className;
            dropdownButton.innerHTML = `<span class="${selectedFlag}"></span>&nbsp${selectedCountry}`;
            countryInput.value = selectedCountry
        })
    })
})