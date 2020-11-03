function sms_select(type) {
    let project_kanong = [
        {"country": "VN", "pid": "越南-1519"},
        {"country": "TH", "pid": "泰国-1147"},
        {"country": "GB", "pid": "英国-1394"},
        {"country": "ZA", "pid": "南非-1122"},
        {"country": "CD", "pid": "刚果金-243"},
        {"country": "PA", "pid": "巴拿马-507"},
        {"country": "MY", "pid": "马来-1385"},
        {"country": "CN", "pid": "国内-1634"},
        {"country": "ID", "pid": "印尼-1832"},
        {"country": "ID", "pid": "印尼-1729"},
        {"country": "MM", "pid": "缅甸-1158"},
        {"country": "MM", "pid": "缅甸-1020"},
        {"country": "CI", "pid": "科特迪瓦-1470"},
        {"country": "KH", "pid": "柬埔寨-1484"},
        {"country": "MG", "pid": "马达-1080"},
        {"country": "KE", "pid": "肯尼亚-1094"},
        {"country": "PH", "pid": "菲律宾-1286"},
        {"country": "LS", "pid": "莱索托-1545"},
        {"country": "LA", "pid": "老挝-1693"},
        {"country": "ZA", "pid": "南非专属-1786"},
        {"country": "HK", "pid": "香港-1584"},
        {"country": "MO", "pid": "澳门-1602"},
        {"country": "US", "pid": "美国-2171"}

    ];

    let project_xiaomifeng = [{"pid": "印度（区号91）", "country": "IN"},
        {"pid": "伊朗", "country": "IR"},
        {"pid": "孟加拉", "country": "BD"},
        {"pid": "巴基斯坦", "country": "PK"},
        {"pid": "埃塞俄比亚", "country": "ET"},
        {"pid": "阿尔及利亚", "country": "DZ"}
    ];

    let project_dingdang = [{"pid": "（马来西亚，区号60）1049 ", "country": "MY"},
        {"pid": "（中国，区号86）1054", "country": "CN"},
        {"pid": "（加纳，区号233）1064", "country": "GH"},
        {"pid": "（缅甸，区号95）1080", "country": "MM"},
        {"pid": "（南非，区号27）1108", "country": "ZA"},
        {"pid": "（俄罗斯，区号7）1121", "country": "RU"},
        {"pid": "（印尼，区号62）1122", "country": "ID"},
        {"pid": "（菲律宾，区号63）1152", "country": "PH"},
        {"pid": "（英国，区号44）", "country": "GB"},
        {"pid": "（乌克兰，区号380）1247", "country": "UA"},
        {"pid": "（罗马尼亚，区号40）1249", "country": "RO"},
        {"pid": "（越南，区号84）1300", "country": "VN"},
        {"pid": "（波兰，区号48）1313", "country": "PL"},
        {"pid": "（柬埔寨，区号855）1354", "country": "KH"},
        {"pid": "（泰国，区号66）1359", "country": "TH"},
        {"pid": "（印度，区号91）1401", "country": "IN"},
        {"pid": "（香港，区号852）1446", "country": "HK"}
    ];

    let project_kele = [{"pid": "（香港，区号852）", "country": "HK1"},
        {"pid": "（香港2，区号852）", "country": "HK2"},
        {"pid": "（越南，区号84）", "country": "VN"},
        {"pid": "（缅甸，区号95）", "country": "MM"},
        {"pid": "（印尼，区号62）", "country": "ID"},
        {"pid": "（南非，区号27）", "country": "ZA"},
        {"pid": "（老挝，区号856）", "country": "LA"},
        {"pid": "（菲律宾，区号63）", "country": "PH"},
        {"pid": "（台湾，区号886）", "country": "TW"}
    ];

    let project_xiangjiao = [{"pid": "项目ID：1013   （柬埔寨，区号855）", "country": "KH"},
        {"pid": "项目ID：1014（老挝，区号856）", "country": "UA"},
        {"pid": "项目ID：1015（南非，区号27）", "country": "ZA"},
        {"pid": "项目ID：1016（印尼，区号62）", "country": "ID"},
        {"pid": "项目ID：1029 香港，区号852）", "country": "HK"},
        {"pid": "项目ID：1051 中国，区号86）", "country": "CN"},
        {"pid": "项目ID：1052（马来西亚，区号60）", "country": "MY"},
        {"pid": "项目ID：1054（南非2，区号27）", "country": "ZA2"},
        {"pid": "项目ID：1055（印度，区号91）", "country": "IN"},
        {"pid": "项目ID：1056（越南，区号84）", "country": "VN"},
        {"pid": "项目ID：1082（法国，区号33）", "country": "FR"},
        {"pid": "项目ID：1091（美国，区号1）", "country": "US"},
        {"pid": "项目ID：1140（香港2，区号852）", "country": "HK2"}
    ];
    let id_country = $("#id_country");
    id_country.empty("");

    if (type === "卡农") {
        id_country.append("<option value=\"0\" selected>卡农项目ID</option>");
        $.each(project_kanong, function (i, n) {
            $("#id_country").append("<option value=" + n.country + ">" + n.pid + "</option>")
        })
    } else if (type === "香蕉") {
        id_country.append("<option value=\"0\" selected>香蕉项目ID</option>");
        $.each(project_xiangjiao, function (i, n) {
            $("#id_country").append("<option value=" + n.country + ">" + n.pid + "</option>")
        })
    } else if (type === "小蜜蜂") {
        id_country.append("<option value=\"0\" selected>小蜜蜂项目ID</option>");
        $.each(project_xiaomifeng, function (i, n) {
            $("#id_country").append("<option value=" + n.country + ">" + n.pid + "</option>")
        })
    } else if (type === "叮当") {
        id_country.append("<option value=\"0\" selected>叮当项目ID</option>");
        $.each(project_dingdang, function (i, n) {
            $("#id_country").append("<option value=" + n.country + ">" + n.pid + "</option>")
        })
    } else if (type === "可乐") {
        id_country.append("<option value=\"0\" selected>可乐项目ID</option>");
        $.each(project_kele, function (i, n) {
            $("#id_country").append("<option value=" + n.country + ">" + n.pid + "</option>")
        })
    }
}

/***
 * 开始任务
 */
function start_task_obj() {
    let proxy_switch = $("input[name='proxy_switch']:checked").val();
    alert(proxy_switch);
    // let count = $('#id_count').val();
    // let sms = $('#id_sms').val();
    // let user = $('#id_user').val();
    // let pid = $('#id_country').val();
    // let pwd = $('#id_pwd').val();
    // let wait = $('#id_wait').val();
    // let data = {
    //     'count': count,
    //     'sms': sms,
    //     'user': user,
    //     'pid': pid,
    //     'pwd': pwd,
    //     'wait': wait,
    //     'use_ip_proxy': use_ip_proxy
    // };
    let data = {
        'use_ip_proxy': proxy_switch
    };
    alert("已开始任务，等待任务结束，或者点击 停止 按钮 结束本次任务");
    $.post("/registry", data,
        function (data) {
            alert(data);
            $.post("/patch_time", {},
                function (data) {
                    if (data === 'not start') {
                        $("#patch_time").text("等待批次任务...");
                        end_task_obj();
                    } else {
                        $("#patch_time").text(data);
                        end_task_obj();
                    }
                });
        });

    $("#start_task").css("color", "red");
}

function fresh_ip() {
    alert("开始筛选代理IP");
}

function stop_ip() {
    alert("停止筛选代理IP");
}

/**
 * 停止任务
 */
function end_task_obj() {
    $.post("/stop_task", {},
        function (data) {
            alert("stop!");
        });
    $("#start_task").css("color", "green");
}

function test_sms_obj() {
    let sms = $('#id_sms').val();
    let user = $('#id_user').val();
    let pid = $('#id_country').val();
    let pwd = $('#id_pwd').val();
    let data = {'sms': sms, 'pid': pid, 'user': user, 'pwd': pwd};
    alert("检测短信平台账户状态！");
    $.post("/test_sms", data,
        function (data) {
            alert(data);
        });
    $("#test_sms").css("color", "green");
}


function proxy_platname_select() {
    let id_proxy_name = $("#id_proxy_name").val();
    $.post("/proxy_platname", {"proxy_name": id_proxy_name},
        function (data) {
            alert(data);
        });
    $("#start_task").css("color", "green");
}

function clear_data() {

    $.post("/clear_data", {},
        function (data) {
            alert(data);
        });
    $("#clear_data").css("color", "red");
}

function proxy_rotatorkey_func() {
    let id_proxy_rotatorkey = $("#id_proxy_rotatorkey").val();
    id_proxy_rotatorkey = id_proxy_rotatorkey.trim().replace('\n', '').replace('\t', '');
    let id_port_rotator = $("#id_port_rotator").val();
    id_port_rotator = id_port_rotator.trim().replace('\n', '').replace('\t', '');
    if (id_port_rotator.length === 0) {
        id_port_rotator = "blank"
    }
    let id_city_rotator = $("#id_city_rotator").val();
    id_city_rotator = id_city_rotator.trim().replace('\n', '').replace('\t', '');
    if (id_city_rotator.length === 0) {
        id_city_rotator = "blank"
    }
    let id_state_rotator = $("#id_state_rotator").val();
    id_state_rotator = id_state_rotator.trim().replace('\n', '').replace('\t', '');
    if (id_state_rotator.length === 0) {
        id_state_rotator = "blank"
    }
    let id_asn_rotator = $("#id_asn_rotator").val();
    id_asn_rotator = id_asn_rotator.trim().replace('\n', '').replace('\t', '');
    if (id_asn_rotator.length === 0) {
        id_asn_rotator = "blank"
    }

    let id_connType_rotator = $("#id_connType_rotator").val();
    id_connType_rotator = id_connType_rotator.trim().replace('\n', '').replace('\t', '');

    let id_country_rotator = $("#id_country_rotator").val();
    id_country_rotator = id_country_rotator.trim().replace('\n', '').replace('\t', '');
    let data = {
        "proxy_rotatorkey": id_proxy_rotatorkey,
        "port": id_port_rotator,
        "city": id_city_rotator,
        "state": id_state_rotator,
        "asn": id_asn_rotator,
        "country": id_country_rotator,
        "connectionType": id_connType_rotator
    };
    alert(JSON.stringify(data));
    $.post("/proxy_rotatorkey", data,
        function (data) {
            alert(data + "：设置成功！");
        });
    $("#id_submit_proxy_rotatorkey").css("color", "red");
}

function proxy_scraperapi_func() {
    let id_proxy_scraperapi = $("#id_proxy_scraperapi").val();
    id_proxy_scraperapi = id_proxy_scraperapi.trim().replace('\n', '').replace('\t', '');
    if (id_proxy_scraperapi.length === 0) {
        alert("请填写 scraperapi api_key");
    } else {
        let data = {
            "proxy_scraperapi": id_proxy_scraperapi,
        };
        alert(JSON.stringify(data));
        $.post("/proxy_scraperapi", data,
            function (data) {
                alert(data + "：设置成功！");
            });
        $("#id_submit_proxy_scraperapi").css("color", "red");
    }
}


function proxy_rotatorkey_check() {
    $.post("/proxy_rotatorkey_check", {},
        function (data) {
            if (data === "no") {
                alert("没有key可以用！请添加");
            } else {
                alert("已存在" + data);
            }
        });
}

function func_setting_prefix() {
    let id_setting_prefix = $("#id_setting_prefix").val();
    id_setting_prefix = id_setting_prefix.trim().replace('\n', '').replace('\t', '');
    if (id_setting_prefix.length === 0) {
        alert("请填写 前缀");
    } else {
        let data = {
            "setting_prefix": id_setting_prefix,
        };
        alert(JSON.stringify(data));
        $.post("/setting_prefix", data,
            function (data) {
                alert(data + "：设置成功！");
            });
        var setting_prefix_label = $("#id_setting_prefix_label");
        setting_prefix_label.text("设置成功: " + id_setting_prefix);
        setting_prefix_label.css("color", "green");
    }
}

function func_setting_prefix_check() {
    $.post("/setting_prefix_check",
        function (data) {
            if (data === "no") {
                alert("没有检测到前缀设置！");
            } else {
                alert("检测到前缀 ： " + data);
                let id_setting_prefix = $("#id_setting_prefix");
                id_setting_prefix.val(data)
            }
        });
}

function proxy_scraperapi_check() {
    $.post("/proxy_scraperapi_check", {},
        function (data) {
            if (data === "no") {
                alert("没有 api_key 可以用！请添加");
            } else {
                alert("已存在" + data);
            }
        });
}