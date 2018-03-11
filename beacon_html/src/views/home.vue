<style lang="less">
    @import "../assets/css/conf";
    .home{
        &-content{
            position: relative;
            min-height: calc(~'100vh - 120px');
            overflow-x: hidden;
            overflow-y: auto;
        }
        &-info{
            width: 250px;
            border-left: 1px solid @border-color;
            position: absolute;
            top: 0px;
            right: 0px;
            bottom: 0px;
            background: #fcfdfd;
            &-img{
                width:42px;
                height: 42px;
                border-radius: 50%;
            }
            &-msg{
                padding-left: 50px;
            }
        }
        &-left{
            padding-right: 250px;
        }
        &-select{
            background: #f5f7f9;
        }
        &-box{
            padding-bottom: 20px;
        }
    }
</style>
<template>
    <div class="home">
        <div class="title-box">
            <span class="p-l-20 color-gray">与我相关的任务</span>
        </div>
        <div class="bottomline"></div>
        <div class="home-content">
            <div class="home-info float-right">
                <div class="positionRL p-15">
                    <div class="fLeft">
                        <img class="home-info-img" src="../assets/image/login_bg.jpg" alt="">
                    </div>
                    <div class="home-info-msg">
                        <p>下午好!,运动起来</p>
                        <p>今天是星期三，2018年2月7日</p>
                    </div>
                </div>
            </div>
            <div class="home-left" v-if="type == 'sure'|| type == 'really' ">
                <div class="title-box home-select p-l-20">
                    <Select v-model="select1" v-if="type == 'sure' "  class="W180">
                        <Option value="1" >所有事件</Option>
                        <Option value="2" >一般事件</Option>
                        <Option value="3" >严重事件</Option>
                    </Select>
                    <Select v-model="select2" multiple class="W180" v-if="type == 'really'">
                        <Option value="-1" >所有事件</Option>
                        <Option value="0" >一般事件</Option>
                        <Option value="1" >严重事件</Option>
                    </Select>
                </div>
                <div class="bottomline"></div>
                <div class="title-box p-l-20">
                    <a @click="btnList('outDate')">
                        <Icon type="arrow-down-b" v-if="module.outDate"></Icon>
                        <Icon type="arrow-right-b" v-if="!module.outDate"></Icon>
                        <span>已逾期</span>
                        <span class="fontw">·</span>
                        <span>4</span>
                    </a>
                </div>
                <div class="bottomline" v-if="module.outDate"></div>
                <div class="home-box p-l-20 p-t-20" v-if="module.outDate">
                    <div class="overHidden">
                        <zzui-file @click="showMask('code')" :check="code==true"  class="fLeft" width="18%" type="normal">
                            <p slot="name">郑州事件名称郑州事件名称</p>
                            <p slot="time">2018-8-9</p>
                            <p slot="type">疑似类事件</p>
                            <zzui-btn v-if="0" class="btn-red" @click="getFile" width="100%" type="get" slot="btn"></zzui-btn>
                            <zzui-btn v-if="!0" class="btn-yellow" width="100%" type="wait" slot="btn"></zzui-btn >
                        </zzui-file>
                    </div>
                    <div class="tool-box overHidden">
                        <Page class="fRight" :current="2" :total="50" simple></Page>
                    </div>
                </div>
                <div class="bottomline"></div>
                <div class="title-box p-l-20">
                    <a @click="btnList('fastDate')" >
                        <Icon type="arrow-down-b" v-if="module.fastDate"></Icon>
                        <Icon type="arrow-right-b" v-if="!module.fastDate"></Icon>
                        <span>即将逾期</span>
                        <span class="fontw">·</span>
                        <span>4</span>
                    </a>
                </div>
                <div class="bottomline" v-if="module.fastDate"></div>
                <div class="home-box p-l-20 p-t-20" v-if="module.fastDate">
                    <div class="overHidden">
                        <zzui-file @click="showMask('code')" :check="code==true"  class="fLeft" width="18%" type="normal">
                            <p slot="name">郑州事件名称郑州事件名称</p>
                            <p slot="time">2018-8-9</p>
                            <p slot="type">疑似类事件</p>
                            <zzui-btn v-if="0" class="btn-red" @click="getFile" width="100%" type="get" slot="btn"></zzui-btn>
                            <zzui-btn v-if="!0" class="btn-yellow" width="100%" type="wait" slot="btn"></zzui-btn >
                        </zzui-file>
                    </div>
                    <div class="tool-box overHidden">
                        <Page class="fRight" :current="2" :total="50" simple></Page>
                    </div>
                </div>
                <div class="bottomline"></div>
                <div class="title-box p-l-20">
                    <a @click="btnList('nowDate')">
                        <Icon type="arrow-down-b" v-if="module.nowDate"></Icon>
                        <Icon type="arrow-right-b" v-if="!module.nowDate"></Icon>
                        <span>正常待签收</span>
                        <span class="fontw">·</span>
                        <span>4</span>
                    </a>
                </div>
                <div class="bottomline"></div>
                <div class="home-box p-l-20 p-t-20" v-if="module.nowDate">
                    <div class="overHidden">
                        <zzui-file @click="showMask('code')" :check="code==true"  class="fLeft" width="18%" type="normal">
                            <p slot="name">郑州事件名称郑州事件名称</p>
                            <p slot="time">2018-8-9</p>
                            <p slot="type">疑似类事件</p>
                            <zzui-btn v-if="0" class="btn-red" @click="getFile" width="100%" type="get" slot="btn"></zzui-btn>
                            <zzui-btn v-if="!0" class="btn-yellow" width="100%" type="wait" slot="btn"></zzui-btn >
                        </zzui-file>
                    </div>
                    <div class="tool-box overHidden">
                        <Page class="fRight" :current="2" :total="50" simple></Page>
                    </div>
                </div>
            </div>
            <div class="home-left" v-if="type == 'report'">
                <div class="title-box home-select p-l-20">
                    <Select v-model="select1" class="W180">
                        <Option value="-1" >所有事件</Option>
                        <Option value="0" >一般事件</Option>
                        <Option value="1" >严重事件</Option>
                    </Select>
                </div>
                <div class="bottomline"></div>
                <div class="title-box p-l-20">
                    <Icon type="arrow-down-b"></Icon>
                    <span>新事件</span>
                    <span class="fontw">·</span>
                    <span>4</span>
                </div>
                <div class="bottomline"></div>
                <div class="home-box p-l-20 p-t-20">
                    <div class="overHidden">
                        <zzui-file @click="showMask" class="fLeft" width="18%" type="normal">
                        <p slot="name">郑州事件名称郑州事件名称</p>
                        <p slot="time">2018-8-9</p>
                        <p slot="type">疑似类事件</p>
                        <zzui-btn class="btn-red" width="100%" type="get" slot="btn"></zzui-btn>
                    </zzui-file>
                    </div>
                    <div class="tool-box overHidden">
                        <Page class="fRight" :current="2" :total="50" simple></Page>
                    </div>
                </div>
                <div class="bottomline"></div>
                <div class="title-box p-l-20">
                    <Icon type="arrow-down-b"></Icon>
                    <span>审核不通过</span>
                    <span class="fontw">·</span>
                    <span>4</span>
                </div>
                <div class="bottomline"></div>
            </div>
             <transition name="bounce">
                <zzui-slider v-show="show" @cancel="hideMask">
                    <common :eventInfo="eventInfo" :submit="editInfo"></common>
                </zzui-slider>
             </transition>
        </div>
    </div>
</template>
<script>
    import zzuiBtn from '../components/zzui-btn.vue';
    import zzuiFile from '../components/zzui-file.vue';
    import zzuiSlider from '../components/zzui-slider.vue';
    import clickoutside from '../libs/clickoutside';
    import common from './common.vue';
    export default {
        name: '',
        props: {},
        data() {
            return {
                select1:'',
                select2:'',
                show:false,
                type:'sure',
                eventInfo:'',
                code:'',
                module:{
                    outDate:false,
                    fastDate:false,
                    nowDate:false,
                }
            };
        },
        directives: { clickoutside },
        mounted() {
            this.changeType(this.$route.name);
            this.eventInfo = {
                "comment":"123", //备注
                "status":1, //事件状态 0-未签收 1-签收办理中 2-下发办理中 3-上报办理中 4-已办结
                "urgent_level":1,//紧急程度
                "user_name":"中天新",//用户名
                "event_code":"b113fcc0-2122-11e8-960f-8c8590711a03",//唯一编码
                "source_ip":"111.233.23.23",//源ip
                "danger_level":1,//严重等级
                "event_name":"信阳攻击事件",//事件名称
                "target_ip":"1.1.1.1",//目的ip
                "time":"2018-03-06T17:06:56",//发生时间
                "source_port":"9909",//源端口
                "target_port":"8809",//目的端口
                "type":1   //事件类型 1-确凿类事件 2-疑似类事件 3-隐患/风险类事件
            }
        },
        watch:{
            '$route'(params){
                this.changeType(params.name);
            }
        },
        methods: {
            showMask(code){
                //this.getEventInfo(code);
                this.show = true;
            },
            hideMask(){
                this.show = false;
                this.code = '';
            },
            changeType(params){
                this.type = params;
            },
            //获取事件详情
            getEventInfo(code){
                let data = {
                    action: 'event_info',
                    event_code:code,
                };
                this.$axios.apipost(data, (response) => {
                    this.eventInfo = response.data.data;
                }, (err) => {
                    console.log(err);
                })
            },
            getFile(event){
                console.log(event);
            },
            editInfo(info){
                let data = {
                    action:'event_save',
                };
                data.assign(info);
                /*this.$axios.apipost(data, (response) => {
                    this.$Message.info('保存成功');
                }, (err) => {
                    console.log(err);
                })*/
            },
            btnList(mod){
                console.log(mod);
                this.module[mod] = !this.module[mod]
            }
        },
        components: {
            zzuiBtn,
            zzuiFile,
            zzuiSlider,
            common
        }
    };
</script>