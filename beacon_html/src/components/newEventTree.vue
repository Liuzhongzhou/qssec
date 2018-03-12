<template>
    <div class="canvasContent ">
        <table width="100%" border="1" cellspacing="0">
            <tr>
                <td>
                    <div id="eventCanvas"></div>
                </td>
                <td width="100% ">
                    <div class="leftWord">
                        <div>
                            <h4>考核量化标准</h4>
                            <h4>加分标准：</h4>
                            <ul>
                                <li>系统发现安全类事件超出3天未及时处理5分，超出7天含7天扣除10分。</li>
                            </ul>
                            <h4>扣分标准：</h4>
                            <ul>
                                <li>发现其他地区攻击本地区的确凿类安全事件加3分（一般）、5分（严重）</li>
                                <li>发现内部确凿类安全事件加5分（一般）、10分（严重）</li>
                                <li>发现疑似类安全事件 加3分</li>
                                <li>发现隐患风险类安全事件 加3分</li>
                            </ul>
                        </div>
                    </div>
                </td>
            </tr>
        </table>
    </div>
</template>

<script>
    import Raphael from 'raphael';
    export default{
        data () {
            return {
                paper: ''
            };
        },
        mounted () {
            this.newEventTreeInit();
        },
        methods: {
            /*新事件发现*/
            newEventTreeInit () {
                var attr = {
                    "stroke": "#38569c",
                    "stroke-width": 2
                };
                var attr1 = {
                    "stroke": "#f28c26",
                    "stroke-width": 2
                };
                var attr2 = {
                    "stroke": "#8d4f92",
                    "stroke-width": 2
                };
                var fontAttr = {
                    'font-size': 10 ,
                    'font-weight': 500,
                    'fill': '#38569c'
                };
                var fontAttr1 = {
                    'font-size': 10,
                    'font-weight': 500,
                    'fill': '#f28c26'
                };
                var fontAttr2 = {
                    'font-size': 10,
                    'font-weight': 500,
                    'fill': '#8d4f92'
                };
                var circleAttr = {
                    "stroke": "#38569c",
                    "stroke-width": 2,
                    "fill": "#fff"
                };
                var circleAttr1 = {
                    "stroke": "#f28c26",
                    "stroke-width": 2,
                    "fill": "#fff"
                };
                var circleAttr2 = {
                    "stroke": "#8d4f92",
                    "stroke-width": 2,
                    "fill": "#fff"
                };
                var paper = Raphael('eventCanvas', '100%', 300);
                this.paper = paper;
                var rect1 = paper.rect(60, 94, 68, 23, 4).attr(attr);
                var rect2 = paper.rect(45, 185, 85, 23, 4).attr(attr);
                var rect1_1 = paper.rect(183, 139, 68, 23, 4).attr(attr);
                var rect3 = paper.rect(289, 139, 56, 23, 4).attr(attr);
                var rect4 = paper.rect(403, 94, 30, 23, 4).attr(attr);
                var rect4_1 = paper.rect(403, 185, 30, 23, 4).attr(attr2);
                var rect4_2 = paper.rect(403, 139, 30, 23, 4).attr(attr1);
                var rect3_1 = paper.rect(481, 94, 56, 23, 4).attr(attr);
                var rect3_2 = paper.rect(481, 139, 56, 23, 4).attr(attr1);
                var rect3_3 = paper.rect(481, 185, 56, 23, 4).attr(attr2);
                var rect1_2 = paper.rect(605, 94, 68, 23, 4).attr(attr);
                var rect1_3 = paper.rect(605, 139, 68, 23, 4).attr(attr1);
                var rect1_4 = paper.rect(605, 185, 68, 23, 4).attr(attr2);
                this.rectTextCenter(rect1, '手动填写事件', paper, fontAttr).translate(80, 0);
                this.rectTextCenter(rect2, '安全设备自动发现', paper, fontAttr).translate(80, 0);
                this.rectTextCenter(rect1_1, '编辑事件信息', paper, fontAttr).translate(80, 0);
                this.rectTextCenter(rect3, '内部结办', paper, fontAttr).translate(80, 0);
                this.rectTextCenter(rect4, '是', paper, fontAttr).translate(80, 0);
                this.rectTextCenter(rect4_1, '否', paper, fontAttr2).translate(80, 0);
                this.rectTextCenter(rect4_2, '否', paper, fontAttr1).translate(80, 0);
                this.rectTextCenter(rect3_1, '他人办结', paper, fontAttr).translate(80, 0);
                this.rectTextCenter(rect3_2, '事件上报', paper, fontAttr1).translate(80, 0);
                this.rectTextCenter(rect3_3, '事件下发', paper, fontAttr2).translate(80, 0);
                this.rectTextCenter(rect1_2, '他人办理中', paper, fontAttr).translate(80, 0);
                this.rectTextCenter(rect1_3, '上报办理中', paper, fontAttr1).translate(80, 0);
                this.rectTextCenter(rect1_4, '下发办理中', paper, fontAttr2).translate(80, 0);
                var raphaelSet = paper.set();
                raphaelSet.push(rect1,rect2,rect1_1,rect3,rect4,rect4_1,rect4_2,rect3_1,rect3_2,rect3_3,rect1_2,rect1_3,rect1_4);
                raphaelSet.translate(80, 0);
                var circle = paper.circle(208, 105, 3).attr(circleAttr);
                var circle1 = circle.clone().translate(2, 92);
                var circle2 = paper.circle(263, 150, 3).attr(circleAttr);
                var circle3 = paper.circle(425, 150, 3).attr(circleAttr);
                var circle4 = paper.circle(331, 150, 3).attr(circleAttr);
                var circle5 = paper.circle(369, 150, 3).attr(circleAttr);
                var circle6 = paper.circle(483, 105, 3).attr(circleAttr);
                var circle7 = paper.circle(483, 150, 3).attr(circleAttr1);
                var circle8 = paper.circle(483, 197, 3).attr(circleAttr2);
                var circle9 = paper.circle(513, 197, 3).attr(circleAttr2);
                var circle10 = paper.circle(513, 105, 3).attr(circleAttr);
                var circle11 = paper.circle(513, 150, 3).attr(circleAttr1);
                var circle12 = paper.circle(561, 197, 3).attr(circleAttr2);
                var circle13 = paper.circle(561, 105, 3).attr(circleAttr);
                var circle14 = paper.circle(561, 150, 3).attr(circleAttr1);
                var circle15 = paper.circle(617, 197, 3).attr(circleAttr2);
                var circle16 = paper.circle(617, 105, 3).attr(circleAttr);
                var circle17 = paper.circle(617, 150, 3).attr(circleAttr1);
                var circle18 = paper.circle(685, 197, 3).attr(circleAttr2);
                var circle19 = paper.circle(685, 105, 3).attr(circleAttr);
                var circle20 = paper.circle(685, 150, 3).attr(circleAttr1);
                var arrow = this.circleArrowBottom(210, 105, 20, 20, 5, paper, attr);
                var arrow1 = this.circleArrowTop(212, 197, 18, 20, 5, paper, attr);
                var arrow2 = this.circleArrowBottom(235, 130, 20, 20, 5, paper, attr).rotate(-90).translate(-20, 0);
                var arrow3 = this.circleArrowTop(235, 132, 18, 20, 5, paper, attr).rotate(90).translate(20, -1);
                var arrow4 = paper.path('M333 150L367 150').attr(attr);
                var arrow5 = paper.path('M427 150L481 150').attr(attr1);
                var arrow6 = paper.path('M515 150L559 150').attr(attr1);
                var arrow7 = paper.path('M619 150L683 150').attr(attr1);
                var arrow8 = paper.path('M515 105L559 105').attr(attr);
                var arrow9 = paper.path('M619 105L683 105').attr(attr);
                var arrow10 = paper.path('M515 197L559 197').attr(attr2);
                var arrow11 = paper.path('M619 197L683 197').attr(attr2);
                var arrow12 = this.circleArrowTop(427, 150, 20, 20, 5, paper, attr);
                var arrow13 = this.circleArrowBottom(427, 150, 20, 20, 5, paper, attr2);
                var arrow14 = this.circleArrowTop(453, 175, 20, 22, 5, paper, attr2).rotate(90).translate(23, 0);
                var arrow15 = this.circleArrowBottom(453, 125, 20, 22, 5, paper, attr).rotate(-90).translate(22, 0);
            },
            /*上报办理*/
            reportEventTree () {
                var paper = this.paper;
                paper.clear();
                var attr = {
                    "stroke": "#38569c",
                    "stroke-width": 2
                };
                var fontAttr = {
                    'font-size': 10 ,
                    'font-weight': 500,
                    'fill': '#38569c'
                };
                var circleAttr = {
                    "stroke": "#38569c",
                    "stroke-width": 2,
                    "fill": "#fff"
                };
                var rect1 = paper.rect(100, 94, 68, 23, 4).attr(attr);
                var rect2 = paper.rect(85, 185, 85, 23, 4).attr(attr);
                var rect1_1 = paper.rect(223, 139, 68, 23, 4).attr(attr);
                var rect3 = paper.rect(329, 139, 56, 23, 4).attr(attr);
                var rect4 = paper.rect(429, 139, 56, 23, 4).attr(attr);
                var rect5 = paper.rect(529, 139, 56, 23, 4).attr(attr);
                var rect6 = paper.rect(629, 139, 56, 23, 4).attr(attr);
                var rect7 = paper.rect(729, 139, 56, 23, 4).attr(attr);
                var rect8 = paper.rect(429, 185, 56, 23, 4).attr(attr);
                var text1 = this.rectTextCenter(rect1, '手动填写事件', paper, fontAttr);
                var text2 = this.rectTextCenter(rect2, '安全设备自动发现', paper, fontAttr);
                var text3 = this.rectTextCenter(rect1_1, '编辑事件信息', paper, fontAttr);
                var text4 = this.rectTextCenter(rect3, '事件上报', paper, fontAttr);
                var text5 = this.rectTextCenter(rect4, '上级审核', paper, fontAttr);
                var text6 = this.rectTextCenter(rect5, '审核结果', paper, fontAttr);
                var text7 = this.rectTextCenter(rect6, '通过', paper, fontAttr);
                var text8 = this.rectTextCenter(rect7, '办结', paper, fontAttr);
                var text9 = this.rectTextCenter(rect8, '不通过', paper, fontAttr);
                this.addCircleToRectRight (rect1, 3, paper, circleAttr);
                this.addCircleToRectRight (rect2, 3, paper, circleAttr);
                this.addCircleToRectRight (rect1_1, 3, paper, circleAttr);
                this.addCircleToRectRight (rect3, 3, paper, circleAttr);
                this.addCircleToRectRight (rect4, 3, paper, circleAttr);
                this.addCircleToRectRight (rect5, 3, paper, circleAttr);
                this.addCircleToRectRight (rect6, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect6, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect7, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect5, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect4, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect3, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect1_1, 3, paper, circleAttr);
                this.addCircleToRectRight (rect8, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect8, 3, paper, circleAttr);
                var circle_no = paper.circle(557, 162, 3).attr(circleAttr);
                var circle_1 = paper.circle(357, 162, 3).attr(circleAttr);
                var arrow = this.circleArrowBottom(172, 105, 20, 20, 5, paper, attr);
                var arrow1 = this.circleArrowTop(174, 197, 18, 20, 5, paper, attr);
                var arrow2 = this.circleArrowBottom(197, 130, 20, 20, 5, paper, attr).rotate(-90).translate(-20, 0);
                var arrow3 = this.circleArrowTop(197, 132, 18, 20, 5, paper, attr).rotate(90).translate(20, -1);
                var arrow4 = paper.path('M293 150L327 150').attr(attr);
                var arrow6 = paper.path('M387 150L427 150').attr(attr);
                var arrow7 = paper.path('M487 150L527 150').attr(attr);
                var arrow8 = paper.path('M587 150L627 150').attr(attr);
                var arrow5 = paper.path('M687 150L727 150').attr(attr);
                var arrow9 = this.circleArrowBottom(506, 145, 28, 65, 5, paper, attr).rotate(90);
                var arrow10 = this.circleArrowTop(376, 216, 27, 65, 5, paper, attr).rotate(90);
                var raphaelSet = paper.set();
                raphaelSet.push(1?rect1:rect2,rect1_1,rect3,rect4,rect5,rect6,rect7);
                var raphaelSet1 = paper.set();
                raphaelSet1.push(1?text1:text2,text3,text4,text5,text6,text7,text8);
                this.addHighlight(raphaelSet, raphaelSet1, 4);
            },
            /*10哥模块的流程图*/
            tenTree (arr, num) {
                var paper = this.paper;
                paper.clear();
                var attr = {
                    "stroke": "#38569c",
                    "stroke-width": 2
                };
                var fontAttr = {
                    'font-size': 10 ,
                    'font-weight': 500,
                    'fill': '#38569c'
                };
                var circleAttr = {
                    "stroke": "#38569c",
                    "stroke-width": 2,
                    "fill": "#fff"
                };
                var rect = paper.rect(109, 79, 90, 23, 4).attr(attr);
                var rect1 = paper.rect(120, 139, 68, 23, 4).attr(attr);
                var rect2 = paper.rect(225, 139, 105, 23, 4).attr(attr);
                var rect1_1 = paper.rect(383, 139, 68, 23, 4).attr(attr);
                var rect3 = paper.rect(489, 139, 56, 23, 4).attr(attr);
                var rect4 = paper.rect(574, 139, 86, 23, 4).attr(attr);
                var rect5 = paper.rect(689, 139, 56, 23, 4).attr(attr);
                var rect6 = paper.rect(789, 139, 56, 23, 4).attr(attr);
                var rect7 = paper.rect(789, 185, 56, 23, 4).attr(attr);
                var rect8 = paper.rect(589, 185, 56, 23, 4).attr(attr);
                var rect9 = paper.rect(789, 231, 56, 23, 4).attr(attr);
                var rect10 = paper.rect(689, 231, 56, 23, 4).attr(attr);
                var rect11 = paper.rect(589, 231, 56, 23, 4).attr(attr);
                var rect12 = paper.rect(689, 185, 56, 23, 4).attr(attr);
                var rect13 = paper.rect(389, 220, 56, 23, 4).attr(attr);
                var text10 = this.rectTextCenter(rect1_1, arr[3], paper, fontAttr);
                var text11 = this.rectTextCenter(rect3, arr[4], paper, fontAttr);
                var text12 = this.rectTextCenter(rect4, arr[5], paper, fontAttr);
                var text13 = this.rectTextCenter(rect5, arr[6], paper, fontAttr);
                var text14 = this.rectTextCenter(rect6, arr[7], paper, fontAttr);
                var text2 = this.rectTextCenter(rect7, arr[8], paper, fontAttr);
                var text1 = this.rectTextCenter(rect8, '不通过', paper, fontAttr);
                var text3 = this.rectTextCenter(rect12, '不通过', paper, fontAttr);
                var text7 = this.rectTextCenter(rect, arr[0], paper, fontAttr);
                var text8 = this.rectTextCenter(rect1, arr[1], paper, fontAttr);
                var text9 = this.rectTextCenter(rect2, arr[2], paper, fontAttr);
                var text4 = this.rectTextCenter(rect10, arr[10], paper, fontAttr);
                var text5 = this.rectTextCenter(rect11, arr[11], paper, fontAttr);
                var text = this.rectTextCenter(rect9, arr[9], paper, fontAttr);
                this.addCircleToRectRight (rect1_1, 3, paper, circleAttr);
                var text6 = this.rectTextCenter(rect13, '不通过', paper, fontAttr);
                this.addCircleToRectRight (rect3, 3, paper, circleAttr);
                this.addCircleToRectRight (rect4, 3, paper, circleAttr);
                this.addCircleToRectRight (rect5, 3, paper, circleAttr);
                var circleAdd12 = this.addCircleToRectRight (rect12, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect6, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect5, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect4, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect3, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect1_1, 3, paper, circleAttr);
                var circleAdd1 = this.addCircleToRectLeft (rect10, 3, paper, circleAttr);
                var circleAdd5 = this.addCircleToRectLeft (rect9, 3, paper, circleAttr);
                var circleAdd7 = this.addCircleToRectLeft (rect7, 3, paper, circleAttr);
                var circleAdd6 = this.addCircleToRectRight (rect8, 3, paper, circleAttr);
                var circleAdd2 = this.addCircleToRectLeft (rect8, 3, paper, circleAttr);
                var circleAdd3 = this.addCircleToRectRight (rect10, 3, paper, circleAttr);
                var circleAdd4 = this.addCircleToRectRight (rect11, 3, paper, circleAttr);
                this.addCircleToRectRight (rect1, 3, paper, circleAttr);
                this.addCircleToRectRight (rect2, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect2, 3, paper, circleAttr);
                var circle_no = paper.circle(717, 162, 3).attr(circleAttr);
                var circle_1 = paper.circle(517, 162, 3).attr(circleAttr);
                var circle_2 = paper.circle(154, 102, 3).attr(circleAttr);
                var circle_3 = paper.circle(154, 139, 3).attr(circleAttr);
                var circle_4 = paper.circle(817, 162, 3).attr(circleAttr);
                var circle_5 = paper.circle(817, 185, 3).attr(circleAttr);
                var circle_6 = paper.circle(817, 208, 3).attr(circleAttr);
                var circle_7 = paper.circle(817, 231, 3).attr(circleAttr);
                var circle_8 = paper.circle(717, 185, 3).attr(circleAttr);
                var circle_9 = paper.circle(717, 254, 3).attr(circleAttr);
                var circle_10 = paper.circle(419, 162, 3).attr(circleAttr);
                var circle_11 = paper.circle(419, 220, 3).attr(circleAttr);
                var circle_12 = paper.circle(419, 243, 3).attr(circleAttr);
                var arrow1 = paper.path('M154 104L154 137').attr(attr);
                var arrow2 = paper.path('M817 164L817 183').attr(attr);
                var arrow5 = paper.path('M817 210L817 229').attr(attr);
                var arrow3 = paper.path('M332 150L380 150').attr(attr);
                var arrow11 = paper.path('M190 150L222 150').attr(attr);
                var arrow4 = paper.path('M453 150L487 150').attr(attr);
                var arrow6 = paper.path('M547 150L572 150').attr(attr);
                var arrow7 = paper.path('M662 150L687 150').attr(attr);
                var arrow8 = paper.path('M747 150L787 150').attr(attr);
                var arrow11 = paper.path('M747 242L787 242').attr(attr);
                var arrow12 = paper.path('M647 242L687 242').attr(attr);
                var arrow13 = paper.path('M717 164L717 183').attr(attr);
                var arrow14 = paper.path('M787 197L747 197').attr(attr);
                var arrow15 = paper.path('M419 164L419 218').attr(attr);
                var arrow9 = this.circleArrowBottom(666, 145, 28, 65, 5, paper, attr).rotate(90);
                var arrow10 = this.circleArrowTop(536, 216, 27, 65, 5, paper, attr).rotate(90);
                var arrow16 = this.circleArrowTop(444, 292, 15, 65, 5, paper, attr).rotate(90);
                var arrow17 = this.circleArrowBottom(582, 132, 5, 255, 5, paper, attr).rotate(90);
                var raphaelSet = paper.set();
                raphaelSet.push(arrow17, arrow16, text6, arrow15, circle_12, circle_11, rect13, circle_10, circle_9, rect9, arrow2, circle_5, circle_4, text, arrow9, arrow10, rect8, text1, circleAdd1, circleAdd2, circle_no, circle_1,rect7,text2,circle_6,circle_7,arrow5,rect10,rect11,arrow12,arrow11,circleAdd1,circleAdd2,circleAdd3,circleAdd4,circleAdd5,circleAdd6,rect12,circleAdd12,circle_8,text3,circleAdd7,arrow13,arrow14,text4,text5);
                var raphaelSet1 = paper.set();
                raphaelSet1.push(rect8, arrow9, arrow10, text1, circleAdd2, circleAdd6, circle_1);
                var raphaelSet2 = paper.set();
                raphaelSet2.push(rect11, text5, circle_10, circle_9, rect13, arrow12, circleAdd4, circleAdd1, arrow17, arrow16, text6, arrow15, circle_12, circle_11, rect13, rect8, arrow9, arrow10, text1, circleAdd2, circleAdd6, circle_1);
                var raphaelSet3 = paper.set();
                raphaelSet3.push(rect,rect1,rect2,rect1_1,rect3,rect4,rect5,rect6,rect7,rect9,rect10,rect11);
                var raphaelSet4 = paper.set();
                raphaelSet4.push(text7,text8,text9,text10,text11,text12,text13,text14,text2,text,text4,text5);
                this.addHighlight(raphaelSet3,raphaelSet4,4);
                if(num == 8){
                    raphaelSet.hide();
                }else if(num == 12){
                    raphaelSet1.hide();
                }else if(num == 11){
                    raphaelSet2.hide();
                }
            },
            /*确凿类签收内部办理*/
            confirmEvent () {
                var arr = ['上级下发安全事件','事件类别','确凿类安全事件','事件签收','内部办结','他人办结','他人签收','办结'];
                this.tenTree(arr, 8);
            },
            /*确凿类签收下发*/
            confirmEventNo () {
                var arr = ['上级下发安全事件','事件类别','确凿类安全事件','事件签收','内部办结','下发','事件签收','办结'];
                this.tenTree(arr, 8);
            },
            /*开始有两个模块的内部办结*/
            haveTwoModel (arr) {
                var attr = {
                    "stroke": "#38569c",
                    "stroke-width": 2
                };
                var fontAttr = {
                    'font-size': 10 ,
                    'font-weight': 500,
                    'fill': '#38569c'
                };
                var circleAttr = {
                    "stroke": "#38569c",
                    "stroke-width": 2,
                    "fill": "#fff"
                };
                var paper = this.paper;
                paper.clear();
                var rect1 = paper.rect(60, 94, 68, 23, 4).attr(attr);
                var rect2 = paper.rect(45, 185, 85, 23, 4).attr(attr);
                var rect1_1 = paper.rect(183, 139, 68, 23, 4).attr(attr);
                var rect3 = paper.rect(289, 139, 56, 23, 4).attr(attr);
                var rect4 = paper.rect(389, 139, 56, 23, 4).attr(attr);
                var rect5 = paper.rect(489, 139, 56, 23, 4).attr(attr);
                var rect6 = paper.rect(589, 139, 80, 23, 4).attr(attr);
                var rect7 = paper.rect(689, 139, 56, 23, 4).attr(attr);
                var rect8 = paper.rect(789, 139, 56, 23, 4).attr(attr);
                var rect9 = paper.rect(889, 139, 56, 23, 4).attr(attr);
                var rect10 = paper.rect(589, 185, 56, 23, 4).attr(attr);
                this.addCircleToRectRight (rect3, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect3, 3, paper, circleAttr);
                this.addCircleToRectRight (rect4, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect4, 3, paper, circleAttr);
                this.addCircleToRectRight (rect5, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect5, 3, paper, circleAttr);
                this.addCircleToRectRight (rect6, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect6, 3, paper, circleAttr);
                this.addCircleToRectRight (rect7, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect7, 3, paper, circleAttr);
                this.addCircleToRectRight (rect8, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect8, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect9, 3, paper, circleAttr);
                this.addCircleToRectRight (rect1, 3, paper, circleAttr);
                this.addCircleToRectRight (rect2, 3, paper, circleAttr);
                this.addCircleToRectRight (rect1_1, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect1_1, 3, paper, circleAttr);
                this.addCircleToRectRight (rect10, 3, paper, circleAttr);
                this.addCircleToRectLeft (rect10, 3, paper, circleAttr);
                var circle_no = paper.circle(717, 162, 3).attr(circleAttr);
                var circle_1 = paper.circle(517, 162, 3).attr(circleAttr);
                var arrow = this.circleArrowBottom(130, 105, 20, 20, 5, paper, attr);
                var arrow1 = this.circleArrowTop(132, 197, 18, 20, 5, paper, attr);
                var arrow2 = this.circleArrowBottom(155, 130, 20, 20, 5, paper, attr).rotate(-90).translate(-20, 0);
                var arrow3 = this.circleArrowTop(155, 132, 18, 20, 5, paper, attr).rotate(90).translate(20, -1);
                var arrow4 = paper.path('M253 150L286 150').attr(attr);
                var arrow5 = paper.path('M348 150L386 150').attr(attr);
                var arrow6 = paper.path('M448 150L486 150').attr(attr);
                var arrow7 = paper.path('M548 150L586 150').attr(attr);
                var arrow8 = paper.path('M672 150L686 150').attr(attr);
                var arrow9 = paper.path('M748 150L786 150').attr(attr);
                var arrow10 = paper.path('M848 150L886 150').attr(attr);
                var text1 = this.rectTextCenter(rect1, arr[0], paper, fontAttr);
                var text2 = this.rectTextCenter(rect2, arr[1], paper, fontAttr);
                var text3 = this.rectTextCenter(rect1_1, arr[2], paper, fontAttr);
                var text4 = this.rectTextCenter(rect3, arr[3], paper, fontAttr);
                var text5 = this.rectTextCenter(rect4, arr[4], paper, fontAttr);
                var text6 = this.rectTextCenter(rect5, arr[5], paper, fontAttr);
                var text7 = this.rectTextCenter(rect6, arr[6], paper, fontAttr);
                var text8 = this.rectTextCenter(rect7, arr[7], paper, fontAttr);
                var text9 = this.rectTextCenter(rect8, arr[8], paper, fontAttr);
                var text10 = this.rectTextCenter(rect9, arr[9], paper, fontAttr);
                this.rectTextCenter(rect10, '不通过', paper, fontAttr);
                var arrow9 = this.circleArrowBottom(666, 145, 28, 65, 5, paper, attr).rotate(90);
                var arrow10 = this.circleArrowTop(536, 216, 27, 65, 5, paper, attr).rotate(90);
                var raphaelSet = paper.set();
                raphaelSet.push(1?rect1:rect2,rect1_1,rect3,rect4,rect5,rect6,rect7,rect8,rect9);
                var raphaelSet1 = paper.set();
                raphaelSet1.push(1?text1:text2,text3,text4,text5,text6,text7,text8,text9,text10);
                this.addHighlight(raphaelSet, raphaelSet1, 5);
            },
            /*下发办理手动或设备发现 内部办理*/
            byHand () {
                var arr = ['手动填写事件','安全设备自动发现','编辑事件信息','内部办结','他人办结','他人签收','待我审核办结','审核结果','通过','结束'];
                this.haveTwoModel(arr);
            },
            /*下发办理手动或设备发现 事件下发*/
            byHandNo () {
                var arr = ['手动填写事件','安全设备自动发现','编辑事件信息','内部办结','事件下发','下级签收','待我审核办结','审核结果','通过','结束'];
                this.haveTwoModel(arr);
            },
            /*签收办理 上级下发  疑似类事件 下发*/
            suspectedEvent () {
                var arr = ['上级下发安全事件','事件类别','疑似/风险类安全事件','事件签收','是否可下发','事件下发(待签收)','事件签收','申请办结','本级审核','通过','上级审核','办结'];
                this.tenTree(arr, 12);
            },
            /*签收办理 上级下发  疑似类事件 不下发*/
            suspectedEventNo () {
                var arr = ['上级下发安全事件','事件类别','疑似/风险类安全事件','事件签收','是否可下发','他人办结','他人签收','申请办结','待我审核','通过','上级审核','办结'];
                this.tenTree(arr, 12);
            },
            /*下发 疑似 事件下发*/
            suspectedEventBottom () {
                var arr = ['上级下发安全事件','事件类别','疑似/风险类安全事件','事件签收','是否可下发','事件下发(待签收)','事件签收','申请办结','本级审核','通过','办结'];
                this.tenTree(arr, 11);
            },
            /*下发 疑似 内部办理*/
            suspectedEventBottomNo () {
                var arr = ['上级下发安全事件','事件类别','疑似/风险类安全事件','事件签收','是否可下发','他人办结','他人签收','申请办结','待我审核','通过','上级审核','办结'];
                this.tenTree(arr, 11);
            },
            /*方形字体剧中*/
            rectTextCenter (rect, text, paper, fontAttr) {
                var x = rect.attrs.x + rect.attrs.width/2;
                var y = rect.attrs.y + rect.attrs.height/2;
                var text = paper.text(x, y, text).attr(fontAttr);
                return text;
            },
            /*带弧度的下折线*/
            circleArrowBottom(x, y, w, h, r, paper, attr){
                var a = x +','+ y;
                var d = (x+w) +','+ y;
                var c = (x+w+r) +','+ (y+r);
                var e = (x+w+r) +','+ (y+r+h);
                var arrow = paper.path('M'+a+'L'+d+'A'+r+','+r+',0,0,1,'+c+'L'+e+'').attr(attr);
                return arrow;
            },
            /*带有弧度的上折线*/
            circleArrowTop(x, y, w, h, r, paper, attr){
                var a = x +','+ y;
                var b = (x+w+r) +','+ (y-r);
                var c = (x+w) +','+ (y+2);
                var d = (x+w) +','+ y;
                var e = (x+w+r) +','+ (y-r-h);
                var arrow = paper.path('M'+a+'L'+d+'A'+r+','+r+',0,0,0,'+b+'L'+e+'').attr(attr);
                return arrow;
            },
            /*在方形两边添加圆点*/
            addCircleToRectRight (rect, r, paper, attr) {
                var x = rect.attrs.x + rect.attrs.width;
                var y = rect.attrs.y + rect.attrs.height/2;
                var circle = paper.circle(x, y, r).attr(attr);
                return circle;
            },
            addCircleToRectLeft (rect, r, paper, attr) {
                var x = rect.attrs.x;
                var y = rect.attrs.y + rect.attrs.height/2;
                var circle = paper.circle(x, y, r).attr(attr);
                return circle;
            },
            /*addHighlight*/
            addHighlight (arr, arr1, num) {
                var attr = {
                    'fill': '#405da0'
                };
                var fontAttr = {
                    'fill': '#fff'
                };
                for(var i=0 ; i<num ; i++){
                    arr[i].attr(attr);
                    arr1[i].attr(fontAttr);
                }
            }
        },
        components: {

        }
    }
</script>

<style>
    #eventCanvas{
        width: 959px;
        height: 300px;
    }
    .leftWord{
        width: 100%;
        height: 300px;
    }
    .canvasContent{
        width: 100%;
    }
    .leftWord h4{
        font-size: 12px;
        color: #363636;
        margin-top: 10px;
    }
    .leftWord li{
        font-size: 12px;
        color: #868686;
        margin-top: 10px;
    }
    .leftWord div{
        margin-left: 26px;
        margin-top: 20px;
    }
</style>