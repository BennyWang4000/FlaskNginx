const search_id = document.getElementById('search_id');
const search_date = document.getElementById('search_date');
const search_submit = document.getElementById('search_submit');
const app_tbody = document.getElementById('app_tbody');

function select_app() {
    fetch('/select_app', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'med_id': search_id.value,
            'pat_date': search_date.value,
        }),
    })
        .then((response) => {
            return response.json()
        })
        .then(function (response_json) {
            console.log(response_json)
            let table = '';
            response_json['content'].forEach(element => {
                // let check = '';
                table += `<tr>`;
                table += `<td align="center"><h6>${element.cli_date}</h6></td>`;
                table += `<td align="center"><h6>${element.cli_day}</h6></td>`;
                table += `<td align="center"><h6>${element.cli_time}</h6></td>`;
                table += `<td align="center"><h6>${element.dep_name}</h6></td>`;
                table += `<td align="center"><h6>${element.doc_name}</h6></td>`;
                switch (element.app_check) {
                    case 0:
                        table += `<td align="center"><button id="${element.cli_id}">取消</button></td>`;
                        break;
                    case 1:
                        table += `<td align="center"><h6>完成</h6></td>`;
                        break;
                    case 2:
                        table += `<td align="center"><h6>已取消</h6></td>`;
                        break;
                }
                table += `</tr>`;
            });
            app_tbody.innerHTML = table;
        })
};
search_submit.onclick = function () { select_app() };

function cancel_app() {
    fetch('/cancel_app', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'med_id': search_id.value,
            'pat_date': search_date.value,
        }),
    })
        .then((response) => {
            return response.json()
        })
        .then(function (response_json) {
            console.log(response_json)

            alert('取消成功');
            window.location.href = "http://140.83.85.111/search";
        })
};