<style lang="less" scoped>
    .layout{
        border: 1px solid #d7dde4;
        background: #f5f7f9;
        position: relative;
        border-radius: 4px;
        overflow: hidden;
        &-logo{
            background: #333941;
        }
        &-header{
            height: 46px !important;
            line-height: 46px !important;
            background: white !important;
            position: fixed;
            left: 0px;
            top: 0px;
            width: 100%;
            z-index: 999;
            padding: 0px !important;
            box-shadow: 0 2px 3px 2px rgba(0,0,0,.1);
            &-navline{
                height: 3px;
                width: 100%;
                bottom: 0px;
                left: 0px;
            }
            &-badge{
                min-width: 16px !important;
                height: 16px !important;
                line-height: 16px !important;
                padding: 0 3px !important;
                top: -7px !important;
            }
            &-borderleft{
                border-left: 1px solid #d3d8df;
                line-height: 56px;
                width: 46px;
            }
            &-borderight{
                border-right: 1px solid #d3d8df;
                line-height: 57px;
                width: 46px;
            }
        }
        &-slider{
            position: fixed !important;
            left: 0px;
            top: 46px;
            bottom: 0px;
            z-index: 999 !important;
            background: #333941 !important;
        }
        &-linear{
            padding: 61px 15px 15px 195px;
            background: #d3e6e7 !important;
            background: linear-gradient(to right, #d3e6e7, #eaeae1) !important;
            -webkit-background: linear-gradient(to right, #d3e6e7, #eaeae1) !important;
            -moz-background: linear-gradient(to right, #d3e6e7, #eaeae1) !important;
        }
    }
</style>
<template>
    <div class="layout">
        <Layout>
            <!--顶部导航-->
            <Header class="layout-header overHidden">
                <div class="layout-logo fLeft W180 h46 center">
                    <img src="../assets/image/logo.png" alt="">
                </div>
                <a href="javascript:;">
                    <div class="displayIB fLeft center layout-header-borderight">
                        <Icon type="navicon" class="color-black font28"></Icon>
                    </div>
                </a>
                <div class="layout-nav fLeft p-l-15 positionRL">
                    <zzui-tab :menu="childmenu" :check="checkRouter"></zzui-tab>
                </div>
                <a href="javascript:;" @click="showMask">
                    <div class="displayIB fRight center layout-header-borderleft">
                        <Badge count="19" class-name="layout-header-badge">
                            <Icon type="android-notifications-none" class="color-black font26"></Icon>
                        </Badge>
                    </div>
                </a>
            </Header>
            <!--自定义菜单组件-->
            <layout class="layout-slider">
                <zzui-slider :menu="menu" :check="routerName"></zzui-slider>
            </layout>
            <!--中部内容+右侧导航-->
            <Layout class="layout-linear overHidden">
                <Content>
                    <!--事件处置平台流程图-->
                    <div></div>
                    <div :style="{minHeight: 'calc(100vh - 80px)',background:'white'}" class="font12"><slot name="content"></slot></div>
                </Content>
                <transition name="bounce">
                    <zzui-realtime v-show="show" :width="'260'" v-clickoutside="initMask">
                        <div class="p-20 p-l-10 p-r-10">
                            <p class="font22"><span class="m-r-10">{{time.date}}</span><span>{{time.week}}</span></p>
                            <p class="font16"><span class="m-r-10">{{time.am}}</span><span>{{time.hms}}</span></p>
                        </div>
                        <div class="bottomline"></div>
                    </zzui-realtime>
                </transition>
            </Layout>
        </Layout>
    </div>
</template>
<script>
    import {menuConfig} from '../router';
    import zzuiRealtime from '../components/zzui-realtime';
    import zzuiSlider from '../components/zzui-sidebar.vue';
    import zzuiTab from '../components/zzui-tab.vue';
     import clickoutside from '../libs/clickoutside';
    export default {
        data() {
            return {
                navIndex:0,
                menu:[],
                show:false,
                btn:false,
                time:{
                    date:'',
                    week:'',
                    am:'',
                    hms:''
                },
                childmenu:[],
                formatChildmenu:[],
                routerName:'',
                checkRouter:'',
                first:true,
            }
        },
        directives: { clickoutside },
        mounted() {
            this.init();
        },
        methods: {
            /*
            *  初始化时间
            * */
            initTime(){
                setInterval(()=>{
                    this.time = this.$util.getTime();
                },1000);
            },
            init(){
                this.menu = menuConfig;
                this.initTime();
                this.changeRouter(this.$route);
            },
            /*
            * 根据点击位置 显示/隐藏 滑窗
            * */
            initMask(){
                if(this.show && !this.btn){
                     this.show = false;
                }
                this.btn = false;
            },
            /*
            * 显示滑动蒙板窗
            * */
            showMask(){
                this.btn = true;
                this.show = true;
            },
            /*
            * 导航定位
            * */
            changeRouter(params){
                this.routerName = params.meta.pid || params.name;
                for(let i=0;i<this.menu.length;i++){
                    if(this.menu[i].name == this.routerName){
                        this.childmenu = this.menu[i].children || [];
                    }
                }
                this.checkRouter = params.name;
            }
        },
        watch:{
            '$route'(){
                this.changeRouter(this.$route)
            }
        },
        components: {
            zzuiRealtime,
            zzuiSlider,
            zzuiTab
        }
    };
</script>