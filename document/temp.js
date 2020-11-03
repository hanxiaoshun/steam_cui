function fCheckLoginNow() {
    if (!fGetCookie("cm_last_info")) return void (document.documentElement.style.display = "block");
    if (document.documentElement.style.display = "none", !$id("loginjustnowiframe")) {
        var t = document.createElement("iframe");
        t.id = "loginjustnowiframe", t.style.display = "none", t.src = gOption.url + fUrlP("df", "loginjustnow" + gOption.product, !0) + fUrlP("funcid", "loginjustnow") + fUrlP("iframe", "1");
        try {
            document.body.appendChild(t), setTimeout(function () {
                document.documentElement.style.display = "block"
            }, 500)
        } catch (t) {
            setTimeout(function () {
                fCheckLoginNow()
            }, 80)
        }
    }
}

function fCheckAutoLogin() {
    try {
        -1 != window.location.href.indexOf("#return") && ("163.com" == gOption.sDomain ? fSetCookie("P_INFO", "", !1, gOption.sDomain) : fSetCookie("P_INFO", ""))
    } catch (t) {
    }
}

function fAutoLogin() {
    try {
        var t = (fGetCookie("S_INFO"), fGetCookie("P_INFO")), e = "", n = "", o = "", i = 0;
        if (t) {
            var a = t.split("|");
            e = a[0], n = a[1], o = a[2], i = (new Date).getTime() - (n + "000")
        }
        !location.hash && e.indexOf("@" + gOption.sDomain) > -1 && "1" == o && i < 864e6 && (gUserInfo && gUserInfo.style ? window.location.href = gOption.sAutoLoginUrl + "&style=" + gUserInfo.style : window.location.href = gOption.sAutoLoginUrl)
    } catch (t) {
    }
    "yeah.net" != gOption.sDomain && "126.com" != gOption.sDomain && "163.com" != gOption.sDomain || fCheckLoginNow()
}

function fCheckBrowser() {
    if (!(gbForcepc = "pc" == fGetQuery("dv"))) for (var t, e = navigator.userAgent.toLowerCase(), n = {
        ipad: "https://ipad.mail." + gOption.sDomain + "/?dv=ipad",
        pad: "https://pad.mail." + gOption.sDomain + "/",
        smart: "https://smart.mail." + gOption.sDomain + "/?dv=smart",
        m: "https://m.mail." + gOption.sDomain + "/"
    }, o = ["ipad", "iphone os", "android", "ucweb", "rv:1.2.3.4", "windows ce", "windows mobile", "midp"], i = 0; i < o.length; i++) if (-1 != e.indexOf(o[i])) {
        switch (o[i]) {
            case"ipad":
                t = n.ipad;
                break;
            case"iphone os":
                t = n.smart;
                break;
            case"pad":
                t = n.pad;
                break;
            case"android":
                return n.smart || (n.smart = "https://email.163.com/?dv=pc"), n.pad || (n.pad = "https://email.163.com/?dv=pc"), oAndroidRedirect = {
                    sPhoneUrl: n.smart,
                    sPadUrl: n.pad
                }, top.location.href = "https://mail.163.com/html/android_device/v1.htm?smart=" + encodeURIComponent(oAndroidRedirect.sPhoneUrl) + "&pad=" + encodeURIComponent(oAndroidRedirect.sPadUrl), !1;
            default:
                t = n.m
        }
        window.location.href = t
    }
}

function fHtml5Tag() {
    var t = ["aside", "figcaption", "figure", "footer", "header", "hgroup", "nav", "section"], e = 0;
    for (e in t) document.createElement(t[e])
}

function fCheckCookie() {
    navigator.cookieEnabled || alert("鎮ㄥソ锛屾偍鐨勬祻瑙堝櫒璁剧疆绂佹浣跨敤cookie\n璇疯缃偍鐨勬祻瑙堝櫒锛屽惎鐢╟ookie鍔熻兘锛屽啀閲嶆柊鐧诲綍銆�")
}

function fGetQuery(t, e) {
    var n = window.location.search.substr(1), o = n.match(new RegExp("(^|&)" + t + "=([^&]*)(&|$)"));
    return e ? null == o ? null : o[2] : null == o ? null : unescape(o[2])
}

function fGetQueryHash(t) {
    var e = window.location.hash.substr(1), n = e.match(new RegExp("(^|&)" + t + "=([^&]*)(&|$)"));
    return null == n ? null : unescape(n[2])
}

function $id(t) {
    return document.getElementById(t)
}

function fTrim(t) {
    return t.replace(/(^\s*)|(\s*$)/g, "").replace(/(^銆€*)|(銆€*$)/g, "")
}

function fParseMNum(t) {
    return /^0?(13|14|15|18)\d{9}$/.test(fTrim(t))
}

function fCheckAccount(t) {
    var e, n = t;
    if (e = n.toLowerCase(), !(-1 == e.indexOf("@" + gOption.sDomain))) {
        var o;
        o = t.split("@"), t = o[0]
    }
    return t
}

function fGetScript(t, e, n) {
    var o = document.createElement("script");
    o.setAttribute("type", "text/javascript"), o.setAttribute("src", t);
    try {
        o.setAttribute("defer", "defer")
    } catch (t) {
    }
    window.document.body.appendChild(o), void 0 !== o.onreadystatechange ? o.onreadystatechange = function () {
        this.readyState && "loaded" != this.readyState && "complete" != this.readyState || e && e()
    } : o.onload = function () {
        this.readyState && "loaded" != this.readyState && "complete" != this.readyState || e && e()
    }, o.onerror = function () {
        n && n()
    }
}

function fGetCookie(t) {
    var e = t + "=";
    if (document.cookie.length > 0) {
        if (offset = document.cookie.indexOf(e), -1 != offset) {
            offset += e.length, end = document.cookie.indexOf(";", offset), -1 == end && (end = document.cookie.length);
            var n = unescape(document.cookie.substring(offset, end));
            return "string" == typeof n && n.constructor == String && (n = n.replace(/[\<\>\'\"\;]/g, "")), n
        }
        return ""
    }
}

function fSetCookie(t, e, n, o) {
    "string" == typeof e && e.constructor == String && (e = e.replace(/[\<\>\'\"\;]/g, ""));
    var i = ";domain=" + (o || gOption.sCookieDomain);
    document.cookie = t + "=" + escape(e) + i + (n ? ";expires=" + new Date(2099, 12, 31).toGMTString() : "")
}

function fEventListen(t, e, n, o) {
    o = !!o, t.addEventListener ? t.addEventListener(e, n, o) : t.attachEvent && t.attachEvent("on" + e, n)
}

function fEventUnlisten(t, e, n, o) {
    o = !!o, t.removeEventListener ? t.removeEventListener(e, n, o) : t.detachEvent && t.detachEvent("on" + e, n)
}

function fRandom(t) {
    return Math.floor(t * Math.random())
}

function fUrlP(t, e, n) {
    return arguments[2] || (n = !1), n ? t + "=" + e : "&" + t + "=" + e
}

function fResize() {
    var t, e = document.body.offsetHeight, n = document.documentElement.clientHeight;
    t = e > n ? e : n, $id("mask").style.height = t + "px"
}

function fJSONP(t, e) {
    if (t) {
        var n = "&";
        for (var o in e) n += o + "=" + e[o] + "&";
        var i = n.split("&");
        i.pop(), i.shift(), n = i.join("&"), fGetScript(t + "?" + n + "&rnd=" + Math.random())
    }
}

function fFQ() {
    var t = fGetQuery("fq"), e = /^[0-9]/.test(t), n = fGetQuery("uid"),
        o = new RegExp("(@" + gOption.sDomain + ")$").test(n);
    if (e && o) {
        var i = (new Date).getTime();
        fSetCookie("fq", t + "_" + i, !1);
        var a = document.createElement("img"),
            r = "https://count.mail.163.com/beacon/login.gif?uid=" + n + "&fq=" + i + "&lf=" + fGetQuery("fq");
        a.setAttribute("src", r), a.setAttribute("alt", ""), a.style.display = "none", document.body.appendChild(a)
    }
}

function fStartTime() {
    var t = fGetCookie("starttime");
    "" == t && (t = (new Date).getTime(), fSetCookie("starttime", t, !1))
}

function fEnData(t) {
    if (!window.RSAKey) return window.bGettingAlgorithm || (fGetScript("https://mimg.127.net/p/freemail/index/lib/scripts/algorithm.js"), window.bGettingAlgorithm = !0), void setTimeout(function () {
        fEnData(t)
    }, 200);
    if (null == t || 0 == t.length) return alert("鍙傛暟闈炴硶"), !1;
    var e = new Array;
    e = t.split("\n");
    var n = e[0];
    if ("401" == n) alert("鍙傛暟闈炴硶"); else if ("500" == n) alert("鏈嶅姟绔紓甯�"); else if ("200" == n) {
        var o = e[1], i = e[2], a = $id("pwdInput").value, r = new RSAKey;
        r.setPublic(i, o);
        var c = r.encrypt(MD5(a));
        window.location.href = "https://reg.163.com/httpLoginVerifyNew.jsp?" + fUrlP("product", gOption.product, !0) + fUrlP("rcode", c) + fUrlP("savelogin", $id("savelogin").value) + fUrlP("url", encodeURIComponent(window.sHttpAction)) + fUrlP("url2", encodeURIComponent(gOption.url2)) + fUrlP("username", $id("idInput").value + "@" + gOption.sDomain)
    }
}

function loginRequest(t) {
    var e = getRnd($id("idInput").value + "@" + gOption.sDomain);
    c_url = "https://reg.163.com/services/httpLoginExchgKeyNew?rnd=" + e, c_url += "&jsonp=" + t, fGetScript(c_url)
}

function getRnd(t) {
    return base64encode(utf16to8(t))
}

function base64encode(t) {
    var e, n, o, i, a, r;
    for (o = t.length, n = 0, e = ""; n < o;) {
        if (i = 255 & t.charCodeAt(n++), n == o) {
            e += base64EncodeChars.charAt(i >> 2), e += base64EncodeChars.charAt((3 & i) << 4), e += "==";
            break
        }
        if (a = t.charCodeAt(n++), n == o) {
            e += base64EncodeChars.charAt(i >> 2), e += base64EncodeChars.charAt((3 & i) << 4 | (240 & a) >> 4), e += base64EncodeChars.charAt((15 & a) << 2), e += "=";
            break
        }
        r = t.charCodeAt(n++), e += base64EncodeChars.charAt(i >> 2), e += base64EncodeChars.charAt((3 & i) << 4 | (240 & a) >> 4), e += base64EncodeChars.charAt((15 & a) << 2 | (192 & r) >> 6), e += base64EncodeChars.charAt(63 & r)
    }
    return e
}

function utf16to8(t) {
    var e, n, o, i;
    for (e = "", o = t.length, n = 0; n < o; n++) i = t.charCodeAt(n), i >= 1 && i <= 127 ? e += t.charAt(n) : i > 2047 ? (e += String.fromCharCode(224 | i >> 12 & 15), e += String.fromCharCode(128 | i >> 6 & 63), e += String.fromCharCode(128 | i >> 0 & 63)) : (e += String.fromCharCode(192 | i >> 6 & 31), e += String.fromCharCode(128 | i >> 0 & 63));
    return e
}

function fGetLocator(t) {
    try {
        var e = t.split("&");
        if (window.gLocationProvince = "common", window.gLocationCity = "common", e.length > 0) for (var n = 0; n < e.length; n++) {
            var o = e[n].split("=");
            if (2 == o.length) {
                var i = o[0], a = o[1];
                switch (i) {
                    case"province":
                        window.gLocationProvince = a;
                        break;
                    case"city":
                        window.gLocationCity = a
                }
            }
        }
        window.fSetLocation && fSetLocation(t)
    } catch (t) {
    }
}

var gbForcepc, oAndroidRedirect = {sPhoneUrl: "", sPadUrl: ""};
Object.extend = function (t, e, n) {
    t = t || {}, e = e || {};
    for (var o in e) if ("prototype" !== o) try {
        (!n || this.has && !this.has(t, o)) && (t[o] = e[o])
    } catch (t) {
    }
    try {
        n || e.toString === e.constructor.prototype.toString || (t.toString = e.toString)
    } catch (t) {
    }
    return t
}, function (t) {
    t.CapsLock = function (t) {
        function e(t) {
            var e = this, n = e.el = t.el, o = {
                keypress: function (t) {
                    e._keyPress(t)
                }, keydown: function (t) {
                    e._keyDown(t)
                }, blur: function (t) {
                    e._blur(t)
                }
            };
            e.capsLockInfo = o, e.change = t.change, fEventListen(n, "keypress", o.keypress), fEventListen(n, "keydown", o.keydown), fEventListen(n, "blur", o.blur)
        }

        function n() {
            return this.status
        }

        function o() {
            var t = this;
            t.change && t.change(t.status)
        }

        function i(t) {
            var e = this;
            20 === (t.which || t.keyCode) && void 0 !== e.status && (e.preStatus = e.status = !e.status, e.trigger(e.status))
        }

        function a(t) {
            var e = this, n = t.which || t.keyCode, o = !1;
            t.shiftKey ? o = !0 : t.modifiers && (o = !!(4 & t.modifiers));
            var i = e.preStatus;
            e.preStatus = e.status, e.status = !!(n >= 65 && n <= 90 && !o || n >= 97 && n < 122 && o) || !(n >= 65 && n <= 90 && o || n >= 97 && n < 122 && !o) && i, e.status !== e.preStatus && e.trigger(e.status)
        }

        function r() {
            var t = this;
            t.preStatus = t.status = void 0, t.trigger(t.status)
        }

        var c = {
            preStatus: void 0,
            status: void 0,
            initialize: e,
            isOn: n,
            trigger: o,
            _keyDown: i,
            _keyPress: a,
            _blur: r
        };
        Object.extend(CapsLock.prototype, c), Object.extend(CapsLock.prototype, t), this.initialize(t)
    }
}(window);
var gUserInfo = {username: null, style: null, safe: null}, gVisitorCookie = function () {
    var t = function () {
        var t = fGetCookie("nts_mail_user");
        if (void 0 != t) {
            var e = t.split(":");
            3 == e.length && (gUserInfo.username = e[0], gUserInfo.style = e[1], gUserInfo.safe = e[2])
        }
    }, e = function () {
        var t = gUserInfo.username + ":" + gUserInfo.style + ":" + gUserInfo.safe;
        n("nts_mail_user", t, !0)
    }, n = function (t, e, n, o) {
        var i = ";domain=" + (o || gOption.sCookieDomain);
        document.cookie = t + "=" + e + i + (n ? ";expires=" + new Date(2099, 12, 31).toGMTString() : "")
    };
    return {
        init: function () {
            return t(), this
        }, saveInfo: function () {
            e()
        }, loadInfo: function () {
            t()
        }
    }
}().init(), gMobileNumMailIsForbidden, gMobileNumMailResult, gMobileNumMail = function () {
    var t, e, n, o, i, a = {}, r = ["xxxxx", "xxx"], c = Math.round((new Date).getTime() / 864e5) + "",
        d = function () {
            return 1 == fGetCookie("MTip")
        }, s = function () {
            fSetCookie("MTip", "1", !0), $id("mobtips").style.display = "none"
        }, l = function (e) {
            var i, r;
            return i = e + "@" + gOption.sDomain, -1 === (r = h(e, i)) ? void MobCallback({
                nCode: "private",
                sNum: "invalidMail"
            }) : 0 === r ? void (void 0 === o ? MobCallback({nCode: "404"}) : MobCallback({
                nCode: "200",
                sNum: o
            })) : (t = i, a.all = fGetCookie("P_INFO"), a.all && a.all.length > 0 && (a.uid = a.all.split("|")[0], a.num = a.all.split("|")[6]), a.uid && a.uid !== i ? void f(i) : a.num && a.num.indexOf("&") > -1 ? (n = a.num.split("&")[0], void ("" == n ? MobCallback({nCode: "404"}) : MobCallback({
                nCode: "200",
                sNum: n
            }))) : void f(i))
        }, u = function (t) {
            var e = "", n = t;
            return 6 === n.length && (e = n.substr(0, 3) + r[0] + n.substr(3, 3)), 8 === n.length && (e = n.substr(0, 4) + r[1] + n.substr(4, 4)), e
        }, m = function (t) {
            var n = fTrim(t);
            return n == e ? void (void 0 == i ? MobCallback({nCode: "404"}) : MobCallback({
                nCode: "200",
                sNum: i
            })) : fParseMNum(n) ? (e = n, void p(n)) : void MobCallback({nCode: "private", sNum: "invalidNum"})
        }, f = function (t) {
            fGetScript("https://mbind.mail.126.com/mbind/qn.do?uid=" + t + "&t=" + c)
        }, p = function (t) {
            fGetScript("https://mbind.mail.126.com/mbind/qu.do?pn=" + t + "&t=" + c)
        }, h = function (e, n) {
            return !/^[a-zA-Z0-9_\.-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/.test(n) || fParseMNum(e) ? -1 : "string" == typeof t && t === n ? 0 : 1
        };
    return window.MobCallback = function (t) {
        var n, a, r = $id("mobtips"), c = $id("mobtips_txt");
        $id("mobtips_close");
        try {
            var d = t;
            if ("private" == d.nCode && ("invalidMail" != (gMobileNumMailResult = d.sNum) && "invalidNum" != gMobileNumMailResult || (r.style.display = "none")), 200 == d.nCode) {
                if (d.sNum && d.sNum.length > 8) if (i = d.sNum, gMobileNumMailResult = i, (a = gMobileNumMailResult.split("@")[1]) != gOption.sDomain) {
                    var s = e + "@" + a;
                    r.style.height = "auto", n = "姝ゆ墜鏈哄彿鐮佺殑閭鏄�<br/><em>" + s + '</em>锛�<a style="text-decoration:none;" href="https://email.163.com/index.htm#uid=' + s + '">鐐规鐧诲綍</a>'
                } else n = "姝ゅ彿鐮佸凡涓庡笎鍙凤細<em>" + gMobileNumMailResult + "</em> 缁戝畾"; else o = d.sNum, gMobileNumMailResult = u(o), n = "鐢ㄤ綘鐨勬墜鏈哄彿 <em>" + gMobileNumMailResult + "</em> 涔熷彲鐧诲綍";
                c.innerHTML = n, r.style.display = "block"
            }
            404 == d.nCode && (1 == ntabOn ? (n = '鎵嬫満鍙风爜涔熷彲鐧诲綍锛�<a href="https://e.mail.163.com/mobilemail/home.do?from=mail163">鍏嶈垂婵€娲�</a>', o = void 0) : (n = "姝ゅ彿鐮佽繕鏈墜鏈哄彿鐧诲綍", i = void 0), c.innerHTML = n, r.style.display = "block")
        } catch (t) {
            r.style.display = "none"
        }
    }, {
        init: function () {
            return this
        }, forbidden: function () {
            if (gMobileNumMailIsForbidden = d()) return !1;
            s()
        }, getNumFromMail: function (t) {
            if (gMobileNumMailIsForbidden = d()) return !1;
            l(t)
        }, getMailFromNum: function (t) {
            if (gMobileNumMailIsForbidden = d()) return !1;
            m(t)
        }
    }
}().init();
window.bGettingAlgorithm = !1;
var DOMContentLoaded, DOMREADY = function (t) {
    function e() {
        if (!n.isReady) {
            try {
                document.documentElement.doScroll("left")
            } catch (t) {
                return void setTimeout(e, 1)
            }
            n.isReady = !0, n.ready()
        }
    }

    var n = {
        isReady: !1, ready: t, bindReady: function () {
            try {
                if ("complete" === document.readyState) return n.isReady = !0, setTimeout(n.ready, 1);
                if (document.addEventListener) document.addEventListener("DOMContentLoaded", DOMContentLoaded, !1); else if (document.attachEvent) {
                    document.attachEvent("onreadystatechange", DOMContentLoaded);
                    var t = !1;
                    try {
                        t = null == window.frameElement
                    } catch (t) {
                    }
                    document.documentElement.doScroll && t && e()
                }
            } catch (t) {
            }
        }
    };
    document.addEventListener ? DOMContentLoaded = function () {
        document.removeEventListener("DOMContentLoaded", DOMContentLoaded, !1), n.ready()
    } : document.attachEvent && (DOMContentLoaded = function () {
        if ("complete" === document.readyState) {
            if (document.detachEvent("onreadystatechange", DOMContentLoaded), n.isReady) return;
            n.isReady = !0, n.ready()
        }
    }), n.bindReady()
}, base64EncodeChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
!function (t) {
    function e() {
        var t = this;
        t.initData(), t.initParam(), t.initInterface(), t.getData()
    }

    function n() {
        var t = this, e = "";
        if (t._curDomain = "email.163.com", gOption.sCookieDomain != t._curDomain && (t._curDomain = gOption.sDomain), t._dftAD.length > 0) {
            for (var n = 0, o = t._dftAD.length; n < o; n++) t._dftAD[n].index = t._dftAD[n].pid;
            e = t.outputHtml(t._dftAD)
        }
        t._data = {
            domain: {"163.com": !0, "126.com": !0, "yeah.net": !0, "email.163.com": !0},
            html: e
        }, setTimeout(function () {
            if (!t._bSuc) {
                $id("extText").innerHTML = t._data.html
            }
        }, 3e3)
    }

    function o() {
        var t = this, e = t._param, n = "";
        if ("email.163.com" == t._curDomain) {
            var o = fGetCookie("alllogindomain");
            n = "163" == o ? "163.com" : "126" == o ? "126.com" : "yeah" == o ? "yeah.net" : "email.163.com", gLoginInfo[o] ? e.uid = (gLoginInfo[o].username ? gLoginInfo[o].username : "nt") + "@" + n : e.uid = "nt@" + t._curDomain
        } else e.uid = (gUserInfo.username ? gUserInfo.username : "nt") + "@" + t._curDomain;
        e.domain = t._curDomain, e.ver = t._ver, e.ph = -1, e.callback = "loginExtAD.callback"
    }

    function i() {
        var t = this, e = "https://ir.mail.163.com/get.do";
        try {
            "163.com" != t._curDomain && "email.163.com" != t._curDomain || (e = "https://ir.mail.163.com/get.do"), "126.com" == t._curDomain && (e = "https://ir.mail.126.com/get.do"), "yeah.net" == t._curDomain && (e = "https://ir.mail.yeah.net/get.do")
        } catch (t) {
        }
        t._interface = e
    }

    function a() {
        var e = this;
        if (!e.isOpen) return void e.callback();
        e._param.uid = t.themeHandler._param.uid;
        var n = e._param, o = e._interface;
        e._data.domain[e._curDomain] ? fJSONP(o, n) : e.callback()
    }

    function r(t) {
        var e = this, n = e._data, o = [];
        void 0 == t.templateUrl || fGetScript(t.templateUrl, function () {
            if (t && t.lt) try {
                if (void 0 != typeof gAdTemplate && gAdTemplate.parse) {
                    e._bSuc = !0, o = t.lt;
                    for (var i = o.length - 1; i > 0; --i) for (var a = 0; a < i; ++a) if (o[a].pid > o[a + 1].pid) {
                        var r = o[a];
                        o[a] = o[a + 1], o[a + 1] = r
                    }
                    t.lt = o, n.html = e.outputHtml(gAdTemplate.parse(t).lt)
                }
            } catch (t) {
            }
            $id("extText").innerHTML = n.html, "yeah.net" == e._curDomain && indexLogin.shadowFix(!0)
        })
    }

    function c(t) {
        var e = this, n = "", o = e._adNum[e._curDomain];
        if (e._bSuc) {
            for (var i = 0, a = t.length; i < a; i++) t[i].index = i + 1;
            if (t.length < o) {
                for (var r = 0; r < o; r++) e._dftAD[r].index = t.length + r + 1;
                t = t.concat(e._dftAD)
            }
        }
        for (var i = 0; i < o; i++) n += e.template(e._tpl[e._curDomain], t[i]);
        return n
    }

    function d(t, e) {
        var n = /#\{([^\{\}]*?)\}/g;
        return t.replace(n, function (t, n) {
            return void 0 == typeof e[n] ? "" : e[n]
        })
    }

    t.loginExtAD = {
        isOpen: !0,
        init: e,
        initData: n,
        initParam: o,
        initInterface: i,
        getData: a,
        callback: r,
        template: d,
        outputHtml: c,
        _data: {},
        _dftData: {},
        _curDomain: "",
        _interface: "",
        _param: {},
        _ver: 4,
        _tpl: {
            "163.com": '<li class="ext-#{index}">#{div}</li>',
            "126.com": '<li class="ext-#{index}">#{div}</li>',
            "yeah.net": "#{div}",
            "email.163.com": '<li class="ext-#{index}"><span>路</span>#{div}</li>'
        },
        _adNum: {"163.com": 2, "126.com": 2, "yeah.net": 1, "email.163.com": 3},
        _dftAD: [{
            pid: 1,
            div: '<a href="https://mail.163.com/dashi/?from=mail1&gotodownload=1" target="_blank" style="">鎺ㄨ崘浣跨敤閭澶у笀瀹樻柟App</a>'
        }, {
            pid: 3,
            div: '<a href="http://mail.163.com/html/ntesmail6/?from=sy" target="_blank" style="">缃戞槗閭6.0鐗堜粙缁�</a>'
        }],
        _bSuc: !1
    }
}(window);