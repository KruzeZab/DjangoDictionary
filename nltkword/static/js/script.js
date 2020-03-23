$(document).ready(function() {
    $('#search-field').on('focus blur', changebg); 
    $('.play').click(speaker);
}); 

function changebg() {
    $('.main-section').toggleClass('add-bg remove-bg');
}

function speaker() {
    let word = $(this).prev().text();
    const msg = new SpeechSynthesisUtterance(word);
    speechSynthesis.speak(msg);
}
