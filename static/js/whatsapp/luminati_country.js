let country_list = [
    {'name': '-country-AF', 'full_name': 'Afghanistan'},
    {'name': '-country-AL', 'full_name': 'Albania'},
    {'name': '-country-DZ', 'full_name': 'Algeria'},
    {'name': '-country-AX', 'full_name': 'Aland Islands'},
    {'name': '-country-AS', 'full_name': 'American Samoa'},
    {'name': '-country-AD', 'full_name': 'Andorra'},
    {'name': '-country-AO', 'full_name': 'Angola'},
    {'name': '-country-AI', 'full_name': 'Anguilla'},
    {'name': '-country-AQ', 'full_name': 'Antarctica'},
    {'name': '-country-AG', 'full_name': 'Antigua And Barbuda'},
    {'name': '-country-AR', 'full_name': 'Argentina'},
    {'name': '-country-AM', 'full_name': 'Armenia'},
    {'name': '-country-AW', 'full_name': 'Aruba'},
    {'name': '-country-AU', 'full_name': 'Australia'},
    {'name': '-country-AT', 'full_name': 'Austria'},
    {'name': '-country-AZ', 'full_name': 'Azerbaijan'},
    {'name': '-country-BS', 'full_name': 'Bahamas'},
    {'name': '-country-BH', 'full_name': 'Bahrain'},
    {'name': '-country-JE', 'full_name': 'Bailiwick of Jersey'},
    {'name': '-country-BD', 'full_name': 'Bangladesh'},
    {'name': '-country-BB', 'full_name': 'Barbados'},
    {'name': '-country-BY', 'full_name': 'Belarus'},
    {'name': '-country-BE', 'full_name': 'Belgium'},
    {'name': '-country-BZ', 'full_name': 'Belize'},
    {'name': '-country-BJ', 'full_name': 'Benin'},
    {'name': '-country-BM', 'full_name': 'Bermuda'},
    {'name': '-country-BT', 'full_name': 'Bhutan'},
    {'name': '-country-BO', 'full_name': 'Bolivia'},
    {'name': '-country-BA', 'full_name': 'Bosnia And Herzegovina'},
    {'name': '-country-BW', 'full_name': 'Botswana'},
    {'name': '-country-BR', 'full_name': 'Brazil'},
    {'name': '-country-BN', 'full_name': 'Brunei'},
    {'name': '-country-BG', 'full_name': 'Bulgaria'},
    {'name': '-country-BF', 'full_name': 'Burkina Faso'},
    {'name': '-country-BI', 'full_name': 'Burundi'},
    {'name': '-country-KH', 'full_name': 'Cambodia'},
    {'name': '-country-CM', 'full_name': 'Cameroon'},
    {'name': '-country-CA', 'full_name': 'Canada'},
    {'name': '-country-CV', 'full_name': 'Cape Verde'},
    {'name': '-country-KY', 'full_name': 'Cayman Islands'},
    {'name': '-country-CF', 'full_name': 'Central African Republic'},
    {'name': '-country-TD', 'full_name': 'Chad'},
    {'name': '-country-CL', 'full_name': 'Chile'},
    {'name': '-country-CN', 'full_name': 'China'},
    {'name': '-country-CX', 'full_name': 'Christmas Island'},
    {'name': '-country-CC', 'full_name': 'Cocos (Keeling) Islands'},
    {'name': '-country-CO', 'full_name': 'Colombia'},
    {'name': '-country-KM', 'full_name': 'Comoros'},
    {'name': '-country-CG', 'full_name': 'Congo'},
    {'name': '-country-CK', 'full_name': 'Cook Islands'},
    {'name': '-country-CR', 'full_name': 'Costa Rica'},
    {'name': '-country-CI', 'full_name': "Cote D'Ivoire (Ivory Coast)"},
    {'name': '-country-HR', 'full_name': 'Croatia (Hrvatska)'},
    {'name': '-country-CU', 'full_name': 'Cuba'},
    {'name': '-country-CW', 'full_name': 'Curacao'},
    {'name': '-country-CY', 'full_name': 'Cyprus'},
    {'name': '-country-CZ', 'full_name': 'Czech Republic'},
    {'name': '-country-CD', 'full_name': 'Democratic Republic Of Congo (Zaire)'},
    {'name': '-country-DK', 'full_name': 'Denmark'},
    {'name': '-country-DJ', 'full_name': 'Djibouti'},
    {'name': '-country-DM', 'full_name': 'Dominica'},
    {'name': '-country-DO', 'full_name': 'Dominican Republic'},
    {'name': '-country-EC', 'full_name': 'Ecuador'},
    {'name': '-country-EG', 'full_name': 'Egypt'},
    {'name': '-country-SV', 'full_name': 'El Salvador'},
    {'name': '-country-GQ', 'full_name': 'Equatorial Guinea'},
    {'name': '-country-ER', 'full_name': 'Eritrea'},
    {'name': '-country-EU', 'full_name': 'European Union'},
    {'name': '-country-EE', 'full_name': 'Estonia'},
    {'name': '-country-ET', 'full_name': 'Ethiopia'},
    {'name': '-country-FK', 'full_name': 'Falkland Islands (Malvinas)'},
    {'name': '-country-FO', 'full_name': 'Faroe Islands'},
    {'name': '-country-FJ', 'full_name': 'Fiji'},
    {'name': '-country-FI', 'full_name': 'Finland'},
    {'name': '-country-FR', 'full_name': 'France'},
    {'name': '-country-PF', 'full_name': 'French Polynesia'},
    {'name': '-country-TF', 'full_name': 'French Southern Territories'},
    {'name': '-country-GA', 'full_name': 'Gabon'},
    {'name': '-country-GM', 'full_name': 'Gambia'},
    {'name': '-country-GE', 'full_name': 'Georgia'},
    {'name': '-country-DE', 'full_name': 'Germany'},
    {'name': '-country-GH', 'full_name': 'Ghana'},
    {'name': '-country-GI', 'full_name': 'Gibraltar'},
    {'name': '-country-GB', 'full_name': 'Great Britain'},
    {'name': '-country-GR', 'full_name': 'Greece'},
    {'name': '-country-GL', 'full_name': 'Greenland'},
    {'name': '-country-GD', 'full_name': 'Grenada'},
    {'name': '-country-GU', 'full_name': 'Guam'},
    {'name': '-country-GT', 'full_name': 'Guatemala'},
    {'name': '-country-GG', 'full_name': 'Guernsey'},
    {'name': '-country-GN', 'full_name': 'Guinea'},
    {'name': '-country-GW', 'full_name': 'Guinea-Bissau'},
    {'name': '-country-GY', 'full_name': 'Guyana'},
    {'name': '-country-HT', 'full_name': 'Haiti'},
    {'name': '-country-HN', 'full_name': 'Honduras'},
    {'name': '-country-HK', 'full_name': 'Hong Kong'},
    {'name': '-country-HU', 'full_name': 'Hungary'},
    {'name': '-country-IS', 'full_name': 'Iceland'},
    {'name': '-country-IN', 'full_name': 'India'},
    {'name': '-country-ID', 'full_name': 'Indonesia'},
    {'name': '-country-IR', 'full_name': 'Iran'},
    {'name': '-country-IQ', 'full_name': 'Iraq'},
    {'name': '-country-IE', 'full_name': 'Ireland'},
    {'name': '-country-IM', 'full_name': 'Isle of Man'},
    {'name': '-country-IL', 'full_name': 'Israel'},
    {'name': '-country-IT', 'full_name': 'Italy'},
    {'name': '-country-JM', 'full_name': 'Jamaica'},
    {'name': '-country-JP', 'full_name': 'Japan'},
    {'name': '-country-JO', 'full_name': 'Jordan'},
    {'name': '-country-KZ', 'full_name': 'Kazakhstan'},
    {'name': '-country-KE', 'full_name': 'Kenya'},
    {'name': '-country-KI', 'full_name': 'Kiribati'},
    {'name': '-country-KW', 'full_name': 'Kuwait'},
    {'name': '-country-KG', 'full_name': 'Kyrgyzstan'},
    {'name': '-country-LA', 'full_name': 'Laos'},
    {'name': '-country-LV', 'full_name': 'Latvia'},
    {'name': '-country-LB', 'full_name': 'Lebanon'},
    {'name': '-country-LS', 'full_name': 'Lesotho'},
    {'name': '-country-LR', 'full_name': 'Liberia'},
    {'name': '-country-LY', 'full_name': 'Libya'},
    {'name': '-country-LI', 'full_name': 'Liechtenstein'},
    {'name': '-country-LT', 'full_name': 'Lithuania'},
    {'name': '-country-LU', 'full_name': 'Luxembourg'},
    {'name': '-country-MO', 'full_name': 'Macau'},
    {'name': '-country-MK', 'full_name': 'Macedonia'},
    {'name': '-country-MG', 'full_name': 'Madagascar'},
    {'name': '-country-MW', 'full_name': 'Malawi'},
    {'name': '-country-MY', 'full_name': 'Malaysia'},
    {'name': '-country-MV', 'full_name': 'Maldives'},
    {'name': '-country-ML', 'full_name': 'Mali'},
    {'name': '-country-MT', 'full_name': 'Malta'},
    {'name': '-country-MH', 'full_name': 'Marshall Islands'},
    {'name': '-country-MQ', 'full_name': 'Martinique'},
    {'name': '-country-MR', 'full_name': 'Mauritania'},
    {'name': '-country-MU', 'full_name': 'Mauritius'},
    {'name': '-country-YT', 'full_name': 'Mayotte'},
    {'name': '-country-MX', 'full_name': 'Mexico'},
    {'name': '-country-FM', 'full_name': 'Micronesia'},
    {'name': '-country-MD', 'full_name': 'Moldova'},
    {'name': '-country-MC', 'full_name': 'Monaco'},
    {'name': '-country-MN', 'full_name': 'Mongolia'},
    {'name': '-country-ME', 'full_name': 'Montenegro'},
    {'name': '-country-MS', 'full_name': 'Montserrat'},
    {'name': '-country-MA', 'full_name': 'Morocco'},
    {'name': '-country-MZ', 'full_name': 'Mozambique'},
    {'name': '-country-MM', 'full_name': 'Myanmar (Burma)'},
    {'name': '-country-NA', 'full_name': 'Namibia'},
    {'name': '-country-NR', 'full_name': 'Nauru'},
    {'name': '-country-NP', 'full_name': 'Nepal'},
    {'name': '-country-NL', 'full_name': 'Netherlands'},
    {'name': '-country-AN', 'full_name': 'Netherlands Antilles'},
    {'name': '-country-NC', 'full_name': 'New Caledonia'},
    {'name': '-country-NZ', 'full_name': 'New Zealand'},
    {'name': '-country-NI', 'full_name': 'Nicaragua'},
    {'name': '-country-NE', 'full_name': 'Niger'},
    {'name': '-country-NG', 'full_name': 'Nigeria'},
    {'name': '-country-NU', 'full_name': 'Niue'},
    {'name': '-country-NF', 'full_name': 'Norfolk Island'},
    {'name': '-country-KP', 'full_name': 'North Korea'},
    {'name': '-country-MP', 'full_name': 'Northern Mariana Islands'},
    {'name': '-country-NO', 'full_name': 'Norway'},
    {'name': '-country-OM', 'full_name': 'Oman'},
    {'name': '-country-PK', 'full_name': 'Pakistan'},
    {'name': '-country-PW', 'full_name': 'Palau'},
    {'name': '-country-PS', 'full_name': 'Palestine'},
    {'name': '-country-PA', 'full_name': 'Panama'},
    {'name': '-country-PG', 'full_name': 'Papua New Guinea'},
    {'name': '-country-PY', 'full_name': 'Paraguay'},
    {'name': '-country-PE', 'full_name': 'Peru'},
    {'name': '-country-PH', 'full_name': 'Philippines'},
    {'name': '-country-PN', 'full_name': 'Pitcairn'},
    {'name': '-country-PL', 'full_name': 'Poland'},
    {'name': '-country-PT', 'full_name': 'Portugal'},
    {'name': '-country-PR', 'full_name': 'Puerto Rico'},
    {'name': '-country-QA', 'full_name': 'Qatar'},
    {'name': '-country-RO', 'full_name': 'Romania'},
    {'name': '-country-RU', 'full_name': 'Russia'},
    {'name': '-country-RW', 'full_name': 'Rwanda'},
    {'name': '-country-BL', 'full_name': 'Saint Barthelemy'},
    {'name': '-country-SH', 'full_name': 'Saint Helena'},
    {'name': '-country-KN', 'full_name': 'Saint Kitts And Nevis'},
    {'name': '-country-LC', 'full_name': 'Saint Lucia'},
    {'name': '-country-MF', 'full_name': 'Saint Martin'},
    {'name': '-country-VC', 'full_name': 'Saint Vincent And The Grenadines'},
    {'name': '-country-SM', 'full_name': 'San Marino'},
    {'name': '-country-ST', 'full_name': 'Sao Tome And Principe'},
    {'name': '-country-SA', 'full_name': 'Saudi Arabia'},
    {'name': '-country-SN', 'full_name': 'Senegal'},
    {'name': '-country-RS', 'full_name': 'Serbia'},
    {'name': '-country-SC', 'full_name': 'Seychelles'},
    {'name': '-country-SL', 'full_name': 'Sierra Leone'},
    {'name': '-country-SG', 'full_name': 'Singapore'},
    {'name': '-country-SK', 'full_name': 'Slovak Republic'},
    {'name': '-country-SI', 'full_name': 'Slovenia'},
    {'name': '-country-SB', 'full_name': 'Solomon Islands'},
    {'name': '-country-SO', 'full_name': 'Somalia'},
    {'name': '-country-ZA', 'full_name': 'South Africa'},
    {'name': '-country-GS', 'full_name': 'South Georgia And South Sandwich Islands'},
    {'name': '-country-KR', 'full_name': 'South Korea'},
    {'name': '-country-SS', 'full_name': 'South Sudan'},
    {'name': '-country-ES', 'full_name': 'Spain'},
    {'name': '-country-LK', 'full_name': 'Sri Lanka'},
    {'name': '-country-SD', 'full_name': 'Sudan'},
    {'name': '-country-SR', 'full_name': 'Suriname'},
    {'name': '-country-SZ', 'full_name': 'Swaziland'},
    {'name': '-country-SE', 'full_name': 'Sweden'},
    {'name': '-country-CH', 'full_name': 'Switzerland'},
    {'name': '-country-SY', 'full_name': 'Syria'},
    {'name': '-country-TW', 'full_name': 'Taiwan'},
    {'name': '-country-TJ', 'full_name': 'Tajikistan'},
    {'name': '-country-TZ', 'full_name': 'Tanzania'},
    {'name': '-country-TH', 'full_name': 'Thailand'},
    {'name': '-country-TL', 'full_name': 'Timor-Leste'},
    {'name': '-country-TG', 'full_name': 'Togo'},
    {'name': '-country-TK', 'full_name': 'Tokelau'},
    {'name': '-country-TO', 'full_name': 'Tonga'},
    {'name': '-country-TT', 'full_name': 'Trinidad And Tobago'},
    {'name': '-country-TN', 'full_name': 'Tunisia'},
    {'name': '-country-TR', 'full_name': 'Turkey'},
    {'name': '-country-TM', 'full_name': 'Turkmenistan'},
    {'name': '-country-TC', 'full_name': 'Turks And Caicos Islands'},
    {'name': '-country-TV', 'full_name': 'Tuvalu'},
    {'name': '-country-UG', 'full_name': 'Uganda'},
    {'name': '-country-UA', 'full_name': 'Ukraine'},
    {'name': '-country-AE', 'full_name': 'United Arab Emirates'},
    {'name': '-country-UK', 'full_name': 'United Kingdom'},
    {'name': '-country-US', 'full_name': 'United States'},
    {'name': '-country-UY', 'full_name': 'Uruguay'},
    {'name': '-country-UZ', 'full_name': 'Uzbekistan'},
    {'name': '-country-VU', 'full_name': 'Vanuatu'},
    {'name': '-country-VA', 'full_name': 'Vatican City (Holy See)'},
    {'name': '-country-VE', 'full_name': 'Venezuela'},
    {'name': '-country-VN', 'full_name': 'Vietnam'},
    {'name': '-country-VG', 'full_name': 'Virgin Islands (British)'},
    {'name': '-country-VI', 'full_name': 'Virgin Islands (US)'},
    {'name': '-country-WF', 'full_name': 'Wallis And Futuna Islands'},
    {'name': '-country-EH', 'full_name': 'Western Sahara'},
    {'name': '-country-WS', 'full_name': 'Western Samoa'},
    {'name': '-country-YE', 'full_name': 'Yemen'},
    {'name': '-country-ZM', 'full_name': 'Zambia'},
    {'name': '-country-ZW', 'full_name': 'Zimbabwe'}];


function luminati_proxy_country() {
    let id_proxy_country = $("#id_luminati_proxy_country");
    id_proxy_country.empty("");
    id_proxy_country.append('<option value="any" selected>Any country</option>');
    $.each(country_list, function (i, n) {
        id_proxy_country.append('<option value=' + n.name + '>' + n.full_name + '</option>');
    })
}

function rotator_proxy_country() {
    let id_country_rotator = $("#id_country_rotator");
    id_country_rotator.empty("");
    id_country_rotator.append('<option value="any" selected>Any country</option>');
    $.each(country_list, function (i, n) {
        id_country_rotator.append('<option value=' + n.name + '>' + n.full_name + '</option>');
    })
}


function luminati_confirm() {
    let luminati_model = $('#id_luminati_model').val();
    let luminati_proxy_country = $('#id_luminati_proxy_country').val();
    let luminati_proxy_account = $('#id_luminati_proxy_account').val();
    let luminati_proxy_pwd = $('#id_luminati_proxy_pwd').val();
    if (luminati_proxy_account.length === 0){
        alert("请输入 luminati 账号！");
        return false;
    }

    if (luminati_proxy_pwd.length === 0){
        alert("请输入 luminati 密码！");
        return false;
    }


    let data = {
        'luminati_model': luminati_model,
        'luminati_proxy_country': luminati_proxy_country,
        'luminati_proxy_account': luminati_proxy_account,
        'luminati_proxy_pwd': luminati_proxy_pwd
    };
    $.post("/luminati_info", data,
        function (data) {
            alert(data);
            // alert("代理平台选择成功！");
        });
    $("#id_luminati_confirm").css("color", "green");

}

function clear_listfile_proxyelite(){
    $.post("/clear_listfile_proxyelite", {},
        function (data) {
            alert(data);
            // alert("代理平台选择成功！");
        });
    $("#id_clear_listfile_proxyelite").css("color", "red");
}

function clear_listfile_superProxy(){
    $.post("/clear_listfile_superProxy", {},
        function (data) {
            alert(data);
            // alert("代理平台选择成功！");
        });
    $("#clear_listfile_superProxy").css("color", "red");
}