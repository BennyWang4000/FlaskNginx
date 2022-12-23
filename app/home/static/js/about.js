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
        let r = 0;
        table += `<tr>`;
        response_json['content'].forEach(element => {
            table += `<td><h6><a href="/about2?dep_id=${element.dep_id}&dep_name=${element.dep_name}">${element.dep_name}</a></h6></td>`
            if (r % 3 === 2) {
                table += `</tr><tr>`;
            }
            r += 1;
        });
        table += `</tr>`;
        dep_table.innerHTML = table;
    });