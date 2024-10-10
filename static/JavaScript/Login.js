function enviarLogin(event) {
    event.preventDefault(); 

    const email = document.getElementById('email').value;
    const senha = document.getElementById('senha').value;
    const mensagemErr = document.getElementById('mensagemErr')

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `email=${email}&senha=${senha}`
    })
    .then(response => response.json())
    .then(data => {
        if(data.sucess){
            window.location.href = '/teste'
        }
        else {
            mensagemErr.innerText = data.message;
            mensagemErr.style.display = 'block';
        }
    })
}