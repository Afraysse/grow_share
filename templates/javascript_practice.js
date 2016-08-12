$('#login-button').click(function() {
    console.log('login has been clicked');
    $.post('/api/login', {
        'email': $('#formEmail').val(),
        'password': $('#formPassword').val()
    }, function(currentUser){
        if (currentUser.name == "not recognized") {
            $('not-registered').html('<p>Email or password <br> not recognized.</p>');
        } else {
            $('#login-tog').html('<li><p class="navbar-text">Welcome,' + currentUser.name + '</p></li>');
        }

        console.log(currentUser)}
)})