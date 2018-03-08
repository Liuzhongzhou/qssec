<style lang="less">
    #myCanvas {
        width: 600px;
        height: 300px;
        border: 1px solid #000;
    }

    .treeIntroduce {
        font-size: 12px;
        border: 1px solid #000;
        background-color: lightblue;
        width: 600px;
    }

    #treeCanvas {
        width: 90%;
        border: 1px solid #000;
        height: 400px;
    }
</style>
<template>

    <div class="p-l-25">
        <h3 class="tool-box">按钮</h3>
        <zzui-btn>项目开发</zzui-btn>
        <zzui-btn @click="alert(1)" class="btn-red">项目开发</zzui-btn>
        <zzui-btn class="btn-disabled" size="small" type="wait"></zzui-btn>
        <zzui-btn class="btn-disabled" type="over"></zzui-btn>
        <zzui-btn class="btn-disabled" type="get"></zzui-btn>
        <zzui-btn class="btn-disabled" type="out"></zzui-btn>

        <h3 class="tool-box">文件夹</h3>

        <zzui-file @click="checkfile(0)" type="normal" :check="0 == index"></zzui-file>
        <zzui-file @click="checkfile(1)" type="error" :check="1 == index"></zzui-file>

        <zzui-file type="normal"></zzui-file>
        <zzui-file type="error"></zzui-file>

        <h3 class="tool-box">流程图模块</h3>
        <div id="myCanvas"></div>
        <p class="tool-box treeIntroduce m-t-20">
            初始化：var paper = Raphael('myCanvas', width, height);<br>
            attr(): 可以给图像添加属性(颜色，大小，边框。。。。)<br>
            基本图形：reat(x, y, width, height) 方形，circle(x, y, 半径) 圆形，ellipse(x, y, 最左到最右距离，最上到最下距离) 椭圆,createDiamond(x, y, 最左到最右距离, 最上到最下距离) 菱形<br>
            复杂图形: path() 可参照canvas <br>
            clone(): 复制一个图形 <br>
            text(x, y, 'word'): 添加文字 <br>
            让添加的字体在图像居中：rectTextCenter(rect, text, paper, fontAttr) rect创建的图形 text要添加的文字 paper初始化的画布 fontAttr给字体添加的对象模型样式 (圆形，菱形，椭圆形皆如此)<br>
            translate(x, y): 平移 <br>
            rotate(角度): 旋转 <br>
            创建下折线：brokenLineBottom(x, y, 横向长度, 垂直长度, paper, attr) 上折线同理(brokenLineTop) <br>
            创建箭头(等腰三角形)：createArrow(x, y, 底边长度, 高度, paper, attr) <br>
            带弧度的下折线：circleArrowBottom(x, y, 折线长度, 垂直长度, 弧度半径, paper, attr) 上折线同理 <br>
        </p>
        <h3 class="tool-box">流程图展示</h3>
        <div id="treeCanvas" @click="change()"></div>

    </div>
</template>
<script>
    import zzuiBtn from '../components/zzui-btn.vue';
    import zzuiFile from '../components/zzui-file.vue';
    import Raphael from 'raphael'

    export default {
        data() {
            return {

                index: 0,
            };
        },
        mounted() {
        },
        methods: {
            checkfile(index) {
                this.index = index;
            },
            alert(index) {
                alert(index)
            }
        },
        mounted() {
            //setflow();
            this.canvasInitModel();
            this.treeCanvasInit();
        },
        methods: {
            treeCanvasInit() {
                var attr = {
                    "fill": "#17A9C6", //filling with background color
                    "stroke": "#2A6570", // border color of the rectangle
                    "stroke-width": 2 // the width of the border
                };
                var fontAttr = {
                    'font-size': '11',
                    'fill': 'blue'
                };
                var arrowAttr = {
                    fill: "#5B9BD5",
                    stroke: "#5B9BD5"
                };
                var paper = Raphael('treeCanvas', '100%', 400);
                var rect = paper.rect(20, 100, 120, 40, 6).attr(attr);
                var rect1 = paper.rect(20, 220, 120, 40, 6).attr(attr);
                var rect2 = paper.rect(220, 160, 120, 40, 6).attr(attr);
                var diamond = this.createDiamond(480, 180, 80, 60, paper, attr);
                var rect3 = paper.rect(660, 100, 120, 40, 6).attr(attr);
                var rect4 = paper.rect(660, 220, 120, 40, 6).attr(attr);
                var rect5 = paper.rect(860, 220, 120, 40, 6).attr(attr);
                var diamond1 = this.createDiamond(1120, 240, 80, 60, paper, attr);
                var rect6 = paper.rect(1240, 220, 120, 40, 6).attr(attr);
                var rect7 = paper.rect(1240, 100, 120, 40, 6).attr(attr);
                var rect8 = paper.rect(860, 320, 120, 40, 6).attr(attr);
                /*图形内添加文字*/
                this.rectTextCenter(rect, '手动填写事件', paper, fontAttr);
                this.rectTextCenter(rect1, '安全设备自动发现', paper, fontAttr);
                this.rectTextCenter(rect2, '编辑事件信息', paper, fontAttr);
                this.rectTextCenter(rect3, '自己结办', paper, fontAttr);
                this.rectTextCenter(rect4, '事件上报', paper, fontAttr);
                this.rectTextCenter(rect5, '上级审核', paper, fontAttr);
                this.rectTextCenter(rect6, '通过', paper, fontAttr);
                this.rectTextCenter(rect7, '结束', paper, fontAttr);
                this.rectTextCenter(rect8, '不通过', paper, fontAttr);
                this.diamondTextCenter(diamond, '可自己结办', paper, fontAttr);
                this.diamondTextCenter(diamond1, '审核结果', paper, fontAttr);
                /*添加指向箭头*/
                var arrow1 = this.brokenLineBottom(140, 120, 50, 60, paper, attr);
                var arrow2 = this.brokenLineTop(140, 240, 50, 60, paper, attr);
                var rect9 = paper.rect(190, 180, 20, 2).attr(attr);
                var arrow3 = this.createArrow(214, 178, 8, 6, paper, attr).rotate(-90);
                var rect10 = paper.rect(340, 180, 90, 2).attr(attr);
                var arrow4 = this.createArrow(434, 178, 8, 6, paper, attr).rotate(-90);
                var arrow5 = this.brokenLineBottom(544, 56, 30, 160, paper, attr).rotate(-90);
                var arrow6 = this.brokenLineTop(544, 306, 30, 160, paper, attr).rotate(90);
                var arrow7 = this.createArrow(644, 237, 8, 6, paper, attr).rotate(-90);
                var arrow8 = this.createArrow(644, 119, 8, 6, paper, attr).rotate(-90);
                var rect11 = paper.rect(780, 120, 440, 2).attr(attr);
                var arrow9 = this.createArrow(1224, 118, 8, 6, paper, attr).rotate(-90);
                var rect12 = paper.rect(780, 240, 60, 2).attr(attr);
                var arrow10 = this.createArrow(844, 238, 8, 6, paper, attr).rotate(-90);
                var rect13 = paper.rect(980, 240, 80, 2).attr(attr);
                var arrow11 = this.createArrow(1064, 238, 8, 6, paper, attr).rotate(-90);
                var rect14 = paper.rect(1160, 240, 60, 2).attr(attr);
                var arrow12 = this.createArrow(1224, 238, 8, 6, paper, attr).rotate(-90);
                var arrow13 = this.brokenLineTop(992, 340, 130, 70, paper, attr);
                var arrow14 = this.createArrow(987, 336, 8, 6, paper, attr).rotate(90);
                var arrow15 = this.brokenLineTop(756, 374, 70, 138, paper, attr).rotate(90);
                var arrow16 = this.createArrow(723, 262, 8, 6, paper, attr).rotate(180);
                var rect15 = paper.rect(1300, 160, 2, 60).attr(attr);
                var arrow17 = this.createArrow(1301, 152, 8, 6, paper, attr).rotate(180);
            },
            canvasInitModel() {
                var attr = {
                    "fill": "#17A9C6", //filling with background color
                    "stroke": "#2A6570", // border color of the rectangle
                    "stroke-width": 2 // the width of the border
                };
                var fontAttr = {
                    'font-size': '11',
                    'fill': 'blue'
                };
                var paper = Raphael('myCanvas', 600, 300);
                /*长方形*/
                var rect1 = paper.rect(20, 20, 120, 40, 6).attr(attr);
                this.rectTextCenter(rect1, '矩形', paper, fontAttr);
                this.rect = rect1;
                /*圆形*/
                var cir = paper.circle(200, 40, 30).attr(attr);
                this.circleTextCenter(cir, '圆形', paper, fontAttr);
                /*椭圆形*/
                var ellipse = paper.ellipse(320, 50, 60, 40).attr(attr);
                this.ellipseTextCenter(ellipse, '椭圆形', paper, fontAttr);
                /*箭头*/
                var arrow3 = this.createArrow(200, 140, 8, 10, paper, attr).rotate(180);
                paper.text(200, 130, '箭头').attr(fontAttr);
                /*菱形*/
                var diamond = this.createDiamond(60, 140, 80, 60, paper, attr);
                this.diamondTextCenter(diamond, '菱形', paper, fontAttr);
                /*箭头*/
                /*下折线*/
                var a = this.brokenLineBottom(20, 200, 100, 40, paper, attr);
                paper.text(50, 220, '下折线').attr(fontAttr);
                /*上折线*/
                var arrow6 = this.brokenLineTop(160, 240, 100, 40, paper, attr);
                paper.text(200, 220, '上折线').attr(fontAttr);
                /*带弧度的下折线*/
                var arrow = this.circleArrowBottom(300, 200, 40, 20, 20, paper, attr);
                paper.text(320, 220, '带弧度的下折线').attr(fontAttr);
                /*带弧度的上折线*/
                var arrow = this.circleArrowTop(400, 240, 40, 20, 20, paper, attr);
                paper.text(420, 220, '带弧度的上折线').attr(fontAttr);
            },
            /*方形字体剧中*/
            rectTextCenter(rect, text, paper, fontAttr) {
                var x = rect.attrs.x + rect.attrs.width / 2;
                var y = rect.attrs.y + rect.attrs.height / 2;
                paper.text(x, y, text).attr(fontAttr);
            },
            /*圆形形字体居中*/
            circleTextCenter(circle, text, paper, fontAttr) {
                paper.text(circle.attrs.cx, circle.attrs.cy, text).attr(fontAttr);
            },
            /*椭圆形字体居中*/
            ellipseTextCenter(ellipse, text, paper, fontAttr) {
                paper.text(ellipse.attrs.cx, ellipse.attrs.cy, text).attr(fontAttr);
            },
            /*创建菱形*/
            createDiamond(x, y, width, height, paper, attr) {
                var firstStep = (x - width / 2) + ',' + y;
                var secondStep = x + ',' + (y - height / 2);
                var thirdStep = (x + width / 2) + ',' + y;
                var forthStep = x + ',' + (y + height / 2);
                var diamond = paper.path('M' + firstStep + 'L' + secondStep + 'L' + thirdStep + 'L' + forthStep + 'Z').attr(attr);
                return diamond;
            },
            /*菱形文字居中*/
            diamondTextCenter(diamond, text, paper, fontAttr) {
                var x = diamond.attrs.path[1][1];
                var y = diamond.attrs.path[2][2];
                paper.text(x, y, text).attr(fontAttr);
            },
            /*下折线*/
            brokenLineBottom(x, y, w, h, paper, attr) {
                var a = x + ',' + y;
                var arrow = paper.path('M' + a + 'H' + (x + w) + 'V' + (y + h) + 'H' + (x + w - 2) + 'V' + (y + 2) + 'H' + x + 'Z').attr(attr);
                return arrow;
            },
            /*上折线*/
            brokenLineTop(x, y, w, h, paper, attr) {
                var a = x + ',' + y;
                var arrow = paper.path('M' + a + 'H' + (x + w) + 'V' + (y - h) + 'H' + (x + w - 2) + 'V' + (y - 2) + 'H' + x + 'Z').attr(attr);
                return arrow;
            },
            /*箭头(等腰三角形)*/
            createArrow(x, y, e, h, paper, attr) {
                var a = (x - e / 2) + ',' + y;
                var b = x + ',' + (y + h);
                var c = (x + e / 2) + ',' + y;
                var arrow = paper.path('M' + a + 'L' + b + 'L' + c + 'Z').attr(attr);
                return arrow;
            },
            /*带弧度的下折线*/
            circleArrowBottom(x, y, w, h, r, paper, attr) {
                var a = x + ',' + y;
                var b = (x + w) + ',' + (y + 2);
                var c = (x + w + r) + ',' + (y + r);
                var arrow = paper.path('M' + a + 'H' + (x + w) + 'A' + r + ',' + r + ',0,0,1,' + c + 'V' + (y + r + h) + 'H' + (x + w + r - 2) + 'V' + (y + r) + 'A' + (r - 2) + ',' + (r - 2) + ',0,0,0,' + b + 'H' + x + 'Z').attr(attr);
                return arrow;
            },
            /*带有弧度的上折线*/
            circleArrowTop(x, y, w, h, r, paper, attr) {
                var a = x + ',' + y;
                var b = (x + w + r) + ',' + (y - r);
                var c = (x + w) + ',' + (y + 2);
                var arrow = paper.path('M' + a + 'H' + (x + w) + 'A' + r + ',' + r + ',0,0,0,' + b + 'V' + (y - r - h) + 'H' + (x + w + r + 2) + 'V' + (y - r) + 'A' + (r + 2) + ',' + (r + 2) + ',0,0,1,' + c + 'H' + x + 'Z').attr(attr);

            }
        },
        components: {
            zzuiBtn,
            zzuiFile
        }
    };
</script>