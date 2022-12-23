const app_id = document.getElementById('app_id')
const app_date = document.getElementById('app_date')
const app_submit = document.getElementById('app_submit')

const mon_morning = document.getElementById('mon_morning')
const tue_morning = document.getElementById('tue_morning')
const wed_morning = document.getElementById('wed_morning')
const thr_morning = document.getElementById('thr_morning')
const fri_morning = document.getElementById('fri_morning')
const sat_morning = document.getElementById('sat_morning')
const sun_morning = document.getElementById('sun_morning')
const mon_afternoon = document.getElementById('mon_afternoon')
const tue_afternoon = document.getElementById('tue_afternoon')
const wed_afternoon = document.getElementById('wed_afternoon')
const thr_afternoon = document.getElementById('thr_afternoon')
const fri_afternoon = document.getElementById('fri_afternoon')
const sat_afternoon = document.getElementById('sat_afternoon')
const sun_afternoon = document.getElementById('sun_afternoon')
const mon_night = document.getElementById('mon_night')
const tue_night = document.getElementById('tue_night')
const wed_night = document.getElementById('wed_night')
const thr_night = document.getElementById('thr_night')
const fri_night = document.getElementById('fri_night')
const sat_night = document.getElementById('sat_night')
const sun_night = document.getElementById('sun_night')
const td_array = [mon_morning, tue_morning, wed_morning, thr_morning, fri_morning, sat_morning, sun_morning, mon_afternoon, tue_afternoon, wed_afternoon, thr_afternoon, fri_afternoon, sat_afternoon, sun_afternoon, mon_night, tue_night, wed_night, thr_night, fri_night, sat_night, sun_night]

fetch('/select_cli', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        'doc_id': document.currentScript.getAttribute('doc_id'),
    }),
})
    .then((response) => {
        return response.json()
    })
    .then(function (response_json) {
        console.log(response_json)
        response_json['content'].forEach(element => {
            // 0~6 morning 7~13 afternoon
            // 0 7 14 monday, 1 8 15 tuesday
            let idx = 0;
            switch (element.cli_time) {
                case '08:30:00':
                    idx += 0
                    break;
                case '13:30:00':
                    idx += 7
                    break;
                case '18:00:00':
                    idx += 14
                    break;
            }
            switch (element.cli_day) {
                case 1:
                    idx += 0;
                    break;
                case 2:
                    idx += 1;
                    break;
                case 3:
                    idx += 2;
                    break;
                case 4:
                    idx += 3;
                    break;
                case 5:
                    idx += 4;
                    break;
                case 6:
                    idx += 5;
                    break;
                case 7:
                    idx += 6;
                    break;
            }

            td_array[idx].innerHTML += `<h6 style="font-size: small;"><input type="radio" name="cli" value="${element.cli_id}"/>${element.cli_date}</h6></br>`
        });
    });

function insert_app() {
    fetch('/insert_app', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'med_id': app_id.value,
            'cli_id': document.querySelector('input[name="cli"]:checked').value,
        }),
    })
        .then((response) => {
            return response.json()
        })
        .then(function (response_json) {
            console.log(response_json)

            alert('預約成功');
            window.location.href = "http://140.83.85.111";
        })
};
app_submit.onclick = function () { insert_app() };