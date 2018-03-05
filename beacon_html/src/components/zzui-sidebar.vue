<style lang="less" scoped>
    .sidebar{
        width: 180px;
        height: 100%;
        color: #848788;
        position: relative;
    }
    .sidebar-box{
        height: 40px;
        line-height: 40px;
        position: relative;
        &-item{
            display: inline-block;
            width: 9px;
            position: absolute;
            left: 0px;
            top: 0px;
            bottom: 0px;
        }
        &-top{
            width: 1px;
            top: 0px;
            height:15px;
            background: #0c0f11;
            position: absolute;
            left: 5px;
        }
        &-middle{
            width: 9px;
            overflow: hidden;
            margin: 0 auto;
            color: #0c0f11;
            position: absolute;
            top: 14px;
            left: 1px;
        }
        &-bottom{
            width: 1px;
            height: 15px;
            background: #0c0f11;
            position: absolute;
            bottom: 0px;
            left: 5px;
        }
    }
    .sidebar-menu-title-active{
        background: #2d323a;
        color: white;
    }
    .sidebar-menu-title-check{
        width: 3px;
        background: #d33131;
        position: absolute;
        left: 0px;
        top: 0px;
        bottom: 0px;
    }
    .title-user{
        position: absolute;
        top: 0px;
        left: 0px;
        width: 100%;
        transition:all 0.5s;
        img{
            width: 60px;
            height: 60px;
            border-radius:50%;
        }
        .user{
            color: white;
        }
        .line{
            border-bottom: 1px solid #2d323a;
        }
        .score{
            display: inline-block;
            width: 50px;
            height: 28px;
            border-radius: 4px;
            border: solid 1px #f5a623;
            color: #f5a623;
            line-height: 28px;
        }
    }
    .sidebar-wrap{
        position: absolute;
        top:218px;
        left: 0px;
        width: 100%;
        transition:all 0.5s;
    }
    .color-red .sidebar-box-middle{
        color: #d33131;
    }
    a{color: #848788;}
    a:hover{color: #fff}
</style>
<template>
    <div class="sidebar font12">
        <div class="title-user center p-t-20">
            <img src="../assets/image/login_bg.jpg" alt="">
            <p class="user p-t-10">系统管理员</p>
            <p class=" p-t-10" ><span>上次登录：</span><span>2018-12-12 09:00</span></p>
            <p class=" p-t-10" ><span class="score">100</span></p>
            <p class="line p-t-20"></p>
        </div>
        <div class="sidebar-wrap" >
            <div class="title-box p-l-20 m-t-10">菜单</div>
            <div class="sidebar-group" v-for="(list,index) in menu">
                <a href="javascript:;" @click="checkMenu(list.name,index)">
                    <div class="sidebar-menu-title title-box p-l-20 p-r-20 overHidden positionRL" :class="{'sidebar-menu-title-active':index == cur}">
                        <span :class="{'sidebar-menu-title-check':index == cur}"></span>
                        <Icon class="font14" :type="list.meta.icon"></Icon>
                        <span class="m-l-5">{{list.meta.title}}</span>
                        <span class="fRight" v-if="list.children">
                            <Icon type="ios-arrow-right"></Icon>
                        </span>
                    </div>
                </a>
                <!--<ul class="sidebar-menu-content p-l-20 p-r-20" v-if="list.children && index == cur">
                    <a href="javascript:;" @click="checkchildMenu(childindex,child.name)" v-for="(child,childindex) in list.children">
                        <li class="sidebar-box" :class="{'color-red':childCur == childindex}">
                            <div class="sidebar-box-item">
                                <div class="sidebar-box-top"></div>
                                <Icon type="stop" class="sidebar-box-middle"></Icon>
                                <div class="sidebar-box-bottom"></div>
                            </div>
                            <span class="p-l-20">{{child.meta.title}}</span>
                        </li>
                    </a>
                </ul>-->
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        props: {
            menu:{
                type:Array,
            },
            check:'',
        },
        data() {
            return {

            };
        },
        computed:{
            cur(){
                for(let i=0;i<this.menu.length;i++){
                    if(this.menu[i].name == this.check){
                        return i;
                    }
                }
                return 0;
            }
        },
        mounted() {
            this.init();
        },
        methods: {
            checkMenu(name,index){
                this.$router.push({'name':name});
            },
            init(){

            },
        },
        components: {}
    };
</script>