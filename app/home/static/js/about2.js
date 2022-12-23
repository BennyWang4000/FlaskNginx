const doc_table = document.getElementById('doc_table');
fetch('/select_doc', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        'dep_id': document.currentScript.getAttribute('dep_id'),
    }),
})
    .then(response => response.json())
    .then(function (response_json) {
        console.log(response_json)
        let table = '';
        let r = 0;
        table += `<tr>`;
        response_json['content'].forEach(element => {
            table += `<td><h6><a href="/about3?doc_id=${element.doc_id}&doc_name=${element.doc_name}">${element.doc_name}</a></h6></td>`
            if (r % 3 === 2) {
                table += `</tr><tr>`;
            }
            r += 1;
        });
        doc_table.innerHTML += table;
    });