<style lang="less" scoped>
    .navline{
        height: 3px;
        bottom: 0px;
        left: 10px;
        right: 10px;
    }
</style>
<template>
    <div>
        <router-link :to="{'name':list.name}"  :key="index" v-if="list.meta.hide != true" v-for="(list,index) in formatChildmenu">
            <div class="displayIB p-l-10 p-r-10 h46 center positionRL" :class="{'color-red':index == navIndex}">
                <Icon :type="list.meta.icon"></Icon>
                <span>{{list.meta.title}}</span>
                <span class="navline bg-red positionAB " v-if="index == navIndex"></span>
            </div>
        </router-link>
    </div>
</template>
<script>
    export default {
        name: '',
        props: {
            menu:{
                default:[]
            },
            check:{},
        },
        data() {
            return {
                formatChildmenu:[],
                navIndex:0,
            };
        },
        mounted() {

        },
        methods: {
            navMove(){
                let index = 0;
                this.formatChildmenu = [];
                for(let i=0;i<this.menu.length;i++){
                    if(!this.menu[i].meta.hide){
                        this.formatChildmenu.push(this.menu[i]);
                    }
                }
                for(let i=0;i<this.formatChildmenu.length;i++){
                    if(this.check == this.formatChildmenu[i].name){
                        index = i;
                    }
                }
               this.navIndex = index;
            },
        },
        watch:{
            'check'(){
                this.navMove();
            }
        },
        components: {}
    };
</script>