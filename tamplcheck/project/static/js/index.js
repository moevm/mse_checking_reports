function handleFiles() {
    /* функция отправки post-запроса */
    var baseFile = window.localStorage.getItem('base');
    var templateFile = window.localStorage.getItem('template');
    console.log(baseFile);
    console.log(templateFile);
    if (baseFile === "{}" || templateFile === "{}") {
        alert("Документы не выбраны");
    }
    else {
        let req = {
            base: baseFile,
            template: templateFile
        };
        console.log("file uploaded");

        fetch('/index/result', {
        // Specify the method
        method: 'POST',
        // A JSON payload
        body: JSON.stringify(req)
    }).then(function (response) {
        return response.text();
    }).then(function (text) {
        //our response from views.py
        console.log('POST response: ');
        console.log(text);
        alert(text);
    });
    }
}

function saveBase() {
    /* сохрание полного пути до исходного файла */
    var mFile = document.getElementById("file_upload_document").files;
    window.localStorage.setItem('base', mFile[0].name);
}

function saveTemplate() {
    /* сохранение полного пути до файла-шаблона */
    var mFile = document.getElementById("file_upload_template").files;
    window.localStorage.setItem('template', mFile[0].name);
}
