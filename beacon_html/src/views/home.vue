<style lang="less">
    @import "../assets/css/conf";
    .home{
        &-content{
            position: relative;
            overflow: auto;
            min-height: calc(~'100vh - 120px');
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
            <div class="home-left" v-if="type == 'home'|| type == 'really' ">
                <div class="title-box home-select p-l-20">
                    <Select v-model="select1" v-if="type == 'home' "  class="W180">
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
                    <Icon type="arrow-down-b"></Icon>
                    <span>已逾期</span>
                    <span class="fontw">·</span>
                    <span>4</span>
                </div>
                <div class="bottomline"></div>
                <div class="home-box p-l-20 p-t-20">
                    <div class="overHidden">
                        <zzui-file @click="showmask" class="fLeft" width="18%" type="normal">
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
                    <span>即将逾期</span>
                    <span class="fontw">·</span>
                    <span>4</span>
                </div>
                <div class="bottomline"></div>
                <div class="title-box p-l-20">
                    <Icon type="arrow-down-b"></Icon>
                    <span>正常待签收</span>
                    <span class="fontw">·</span>
                    <span>4</span>
                </div>
                <div class="bottomline"></div>
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
                        <zzui-file @click="showmask" class="fLeft" width="18%" type="normal">
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
                    <common :eventInfo="eventInfo"></common>
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
                eventInfo:''
            };
        },
        directives: { clickoutside },
        mounted() {
            this.changeType(this.$route.name);
        },
        watch:{
            '$route'(params){
                this.changeType(params.name);
            }
        },
        methods: {
            showmask(){
                this.show = true;
            },
            hideMask(){
                this.show = false;
            },
            changeType(params){
                this.type = params;
            },
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