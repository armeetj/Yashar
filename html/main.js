shownUpload = document.getElementById('shownUpload');
response = document.getElementById('response')
hiddenUpload = document.getElementById('hiddenUpload');

shownUpload.addEventListener('click', () => { //shown button clicked
    hiddenUpload.click(); //click hidden button
});
hiddenUpload.addEventListener('change', () => { //file chosen
    response.innerHTML='File uploaded';
});