$(document).ready(function() { 
    $.ajax({
        url: "/api/outputs"
    }).then(function(data) {
        for (var i = 0; i < data.length; i++) {
            htmlCode = '<option value="' + data[i].value + '">' + data[i].name + '</option>';
            $('#outputs').append(htmlCode);
        }
    });

    $.ajax({
        url: "/api/classes"
    }).then(function(data) {
        for (var i = 0; i < data.length; i++) {
            htmlCode = '<option value="' + data[i] + '">' + data[i] + '</option>';
            $('#yoga_classes').append(htmlCode);
        }
    });
});

function edit_files() {
    $.ajax({
        url: "/api/edit_files"
    }).then(function(data) {
        return;
    });
}

function generate() {
    var gen_url = "/api/generate?"
    gen_url += "class=" + $( "#yoga_classes option:selected" ).text();
    gen_url += "&output=" + $( "#outputs option:selected" ).text();

    $.ajax({
        url: gen_url
    }).then(function(data) {
        return;
    });
}