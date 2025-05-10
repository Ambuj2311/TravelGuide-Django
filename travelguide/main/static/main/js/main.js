$(document).ready(function() {

    // Booking form date picker
    $('#checkIn, #checkOut').datepicker({
        format: 'yyyy-mm-dd',
        autoclose: true,
        todayHighlight: true
    });
    
});