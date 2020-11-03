import re

html = """<div class="rF0 nui-txt-flag0 ik0" tabindex="0" id="1575117077969_1041tbiaBt7H1pD-H9hdAAAsY1575117091367Dom" role="link"
     aria-label="新 Steam 帐户电子邮件验证 发件人 ： Steam 时间： 2019年11月29日 00:39 (星期五)" sign="letter">
    <div class="nl0 hA0 ck0">
        <div class="gB0" sign="start">
            <div class="dS0" id="1575117077969_1041tbiaBt7H1pD-H9hdAAAsY1575117091367DragDiv" title="最近阅读邮件"><b
                    class="nui-ico nui-ico-drag2" id="1575117077969_1041tbiaBt7H1pD-H9hdAAAsY1575117091367DragB"></b>
            </div>
            <label aria-checked="false" sign="checkbox" class="nui-chk cS0" title="选中此邮件" role="checkbox" tabindex="0"
                   aria-label="选中此邮件"><span class="nui-chk-symbol"><b class="nui-ico nui-ico-checkbox"
                                                                      id="1575117077969_1041tbiaBt7H1pD-H9hdAAAsY1575117091367CheckboxB"></b></span></label><b
                class="dT0 nui-ico nui-ico-read" title="已读" tabindex="-1" aria-label="已读" sign="logo"
                id="1575117077969_1041tbiaBt7H1pD-H9hdAAAsY1575117091367LogoB"></b>
            <div class="dP0" sign="start-from"><span id="_mail_userlabel_0_202" class="nui-user ci0"
                                                     title="">Steam</span></div>
            <div class="dU0" title="设为红旗" style="" role="button" tabindex="-1" aria-label="设为红旗" sign="flag"><b
                    class="nui-ico nui-ico-flag nui-ico-flag-0"
                    id="1575117077969_1041tbiaBt7H1pD-H9hdAAAsY1575117091367FlagB"></b></div>
        </div>
        <div class="il0" id="1575117077969_1041tbiaBt7H1pD-H9hdAAAsY1575117091367MidDiv"><span class="da0">新 Steam 帐户电子邮件验证</span>
        </div>
        <div class="hV0" id="1575117077969_1041tbiaBt7H1pD-H9hdAAAsY1575117091367EndDiv">
            <div id="1575117077969_1041tbiaBt7H1pD-H9hdAAAsY1575117091367DateDiv" class="eO0"
                 title="2019年11月29日 00:39 (星期五)">昨日
            </div>
            <div class="nui-ico  dQ0" title="" style="display: none"></div>
            <b id="_mail_icon_40_207" class="js-component-icon cC0 nui-ico nui-ico-delete  " title="删除邮件"
               sign="trash"></b><b id="_mail_icon_41_208" class="js-component-icon cT0 nui-ico nui-ico-todo  "
                                   title="设置待办" sign="defermanage"></b><b id="_mail_icon_42_209"
                                                                          class="js-component-icon dK0 nui-ico nui-ico-tags  "
                                                                          title="选择邮件标签" sign="tagmanage"></b></div>
        <div class="im0" id="1575117077969_1041tbiaBt7H1pD-H9hdAAAsY1575117091367TagDiv" sign="tag" tabindex="-1"></div>
    </div>
</div>"""

match_group = re.match(r'<div class="rF0 nui-txt-flag0 ik0" tabindex="0" id="(.*?)" role="link"', html,
                       re.M | re.I | re.S | re.IGNORECASE)
print(match_group.group(1))

match_result = re.findall(r'<div class="rF0 nui-txt-flag0 ik0" tabindex="0" id="(.*?)" role="link"', html,
                          re.M | re.I | re.S | re.IGNORECASE)
print(match_result)
