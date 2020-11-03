$(document).ready(function () {
    setInterval(function () {
        $.post("/complate_count", {},
            function (data) {
                if (data === 'not start') {
                    console.log(data);
                } else {
                    var data_split = data.split(',');
                    $("#processing_time").text(data_split[0]);
                    $("#complete_time").text(data_split[1]);
                    $("#success_rate").text(data_split[2]);
                }
            });
    }, 5000);



    setInterval(function () {
        $.post("/get_logger", {},
            function (data) {
                $("#span_get_logger").text(data);
            });
    }, 4000);
    //
    //
    // setInterval(function () {
    //     $.post("/car_info", {},
    //         function (data) {
    //             if (data === 'not start') {
    //                 $("#car_info").text("暂未获取！");
    //             } else {
    //                 $("#car_info").text(data);
    //             }
    //         });
    // }, 8000);
    //
    // setInterval(function () {
    //     $.post("/code_apply_time", {},
    //         function (data) {
    //             if (data === 'not start') {
    //                 $("#code_apply_time").text("0.00");
    //             } else {
    //                 $("#code_apply_time").text(data);
    //             }
    //         });
    // }, 8000);

    setInterval(function () {
        $.post("/email_can_use", {},
            function (data) {
                let json_data = JSON.parse(data);
                let email_can_use_126 =  $("#email_can_use_126");
                email_can_use_126.text(json_data.can_use);
                email_can_use_126.css('color','green');
                let email_not_can_use_126 = $("#email_not_can_use_126");
                email_not_can_use_126.text(json_data.already_use);
                email_not_can_use_126.css('color','red');
            });
    }, 3000);

    setInterval(function () {
        $.post("/ip_can_use", {},
            function (data) {
                let json_data = JSON.parse(data);
                let ip_can_use =  $("#ip_can_use");
                ip_can_use.text(json_data.can_use);
                ip_can_use.css('color','green');
                let ip_not_can_use = $("#ip_not_can_use");
                ip_not_can_use.text(json_data.already_use);
                ip_not_can_use.css('color','red');
            });
    }, 8000);
});
