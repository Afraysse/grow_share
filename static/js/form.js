/* FUNCTIONS FOR FORM ON DASHBOARD.HTML */


/* EGGS FORM */

$(document).ready(function() {
    var $aerialTr = $('#id_A').closest('tr').hide();
    var $groundSprayTr = $('#id_B').closest('tr').hide();

    $('#id_application_method').change(function() {
        var selectedValue = $(this).val();

        if(selectedValue  === 'A') {
            $aerialTr.show();
            $groundSprayTr.hide();
        } else if (selectedValue === 'B') {
            $aerialTr.hide();
            $groundSprayTr.show();
        } else {
            $aerialTr.hide();
            $groundSprayTr.hide();
        }
    });
});

// $( "select" ).change(function () {
//     var str = "";
//     $( "select option:eggs" ).each(function () {
//         str += $( this ).text() + " ";
//     });
//     $( "div" ).text( str );
// })
// .change();