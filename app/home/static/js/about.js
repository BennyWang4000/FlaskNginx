$( document ).ready(function() {
    
    const dep_table = document.getElementById('dep_table');
    fetch('/select_dep', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },  
    })
        .then(response => response.json())
        .then(function (response_json) {
            let table = '';
            response_json['ents'].forEach(element => {
                table += `
                        <option value="${element}">
                    `
            });
            ind_datalist.innerHTML = table
            ind_datalist.DataBind();
        });
});  