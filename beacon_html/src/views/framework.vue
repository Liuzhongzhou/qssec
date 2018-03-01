<style lang="less" scoped>
    .layout{
        border: 1px solid #d7dde4;
        background: #f5f7f9;
        position: relative;
        border-radius: 4px;
        overflow: hidden;
        &-header{
            height: 56px !important;
            line-height: 56px !important;
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
                left: 20px;
                bottom: 0px;
                transition: left 0.3s;
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
            }
            &-borderight{
                border-right: 1px solid #d3d8df;
                line-height: 67px;
            }
        }
        &-slider{
            position: fixed !important;
            left: 0px;
            top: 56px;
            bottom: 0px;
            z-index: 999 !important;
            background: #181d20 !important;
        }
        &-linear{
            padding: 71px 15px 15px 195px;
            background: #d3e6e7 !important;
            background: linear-gradient(to right, #d3e6e7, #eaeae1) !important;
            -webkit-background: linear-gradient(to right, #d3e6e7, #eaeae1) !important;
            -moz-background: linear-gradient(to right, #d3e6e7, #eaeae1) !important;
        }
    }
    .bounce-enter-active {
      animation: bounce-in .4s;
    }
    .bounce-leave-active{
      animation: bounce-in .3s reverse;
    }
    @keyframes bounce-in {
      0% {
        transform: translate(100%);
      }
      100% {
        transform: translate(0);
      }
    }
</style>
<template>
    <div class="layout">
        <Layout :style="{minHeight: '100vh'}">
            <!--顶部导航-->
            <Header class="layout-header overHidden">
                <div class="layout-logo fLeft W180 bg-red h56 center">
                    <img src="../assets/image/logo.png" alt="">
                </div>
                <!--缩小菜单按钮-->
                <!--<a href="javascript:;">
                    <div class="displayIB fLeft W70 center layout-header-borderight">
                        <Icon type="navicon" class="color-black font28"></Icon>
                    </div>
                </a>-->
                <div class="layout-nav fLeft p-l-15 positionRL">
                    <a href="javascript:;" @click="navMovePush(list,index)" :key="index" v-for="(list,index) in menu">
                        <div class="layout-navItem displayIB W80 h56 center" :class="{'color-red':index == navIndex}">
                            <Icon :type="list.meta.icon"></Icon>
                            <span>{{list.meta.title}}</span>
                        </div>
                    </a>
                    <span class="layout-header-navline bg-red W70 positionAB" :style="{'left':moveLeft}"></span>
                </div>
                <a href="javascript:;" @click="showMask">
                    <div class="displayIB fRight W70 center layout-header-borderleft">
                        <Badge count="19" class-name="layout-header-badge">
                            <Icon type="android-notifications-none" class="color-black font28"></Icon>
                        </Badge>
                    </div>
                </a>
            </Header>
            <!--自定义菜单组件-->
            <layout class="layout-slider">
                <zzui-slider :menu="childmenu" :check="routerName" :isfirst="first"></zzui-slider>
            </layout>
            <!--中部内容+右侧导航-->
            <Layout class="layout-linear overHidden">
                <Content>
                    <Card class="font12"><slot name="content"></slot></Card>
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
                moveLeft:'20px',
                childmenu:[],
                routerName:'',
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
            navMove(name){
                let index = 0;
                for(let i=0;i<this.menu.length;i++){
                    if(name == this.menu[i].name){
                        index = i;
                    }
                }
               this.moveLeft = index * 80+20+'px';
               this.navIndex = index;
               this.childmenu = this.menu[index].children || [];
               this.first = index == 0 ? true : false;
            },
            /*
            * 定位跳转
            * */
            navMovePush(params){
                this.changeRouter(params);
                this.$router.push({'name':params.name});
            },
            changeRouter(params){
                this.routerName = params.name;
                let name = params.meta.pid || params.name;
                this.navMove(name);
            }
        },
        watch:{
            '$route'(){
                this.changeRouter(this.$route)
            }
        },
        components: {
            zzuiRealtime,
            zzuiSlider
        }
    };
</script>