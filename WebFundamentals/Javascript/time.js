var hour = 8;
var minute = 50;
var period = 'AM';
var message = '';

if (minute < 30){
    message = "It's just after" + ' ' + hour;
} else {
    message = "It's almost" + ' ' + (hour + 1);
}
if (period === 'AM') {
    console.log(message, 'in the morning');
} else {
    console.log(message, 'in the evening');
}


hour = 7;
minute = 15;
period = "PM";

if (minute < 30){
    message = "It's just after" + ' ' + hour;
} else {
    message = "It's almost" + ' ' + (hour + 1);
}
if (period === 'AM') {
    console.log(message, 'in the morning');
} else {
    console.log(message, 'in the evening');
}