<style lang="less" scoped>
    @import "../assets/css/conf";
.btn{
    height: 32px;
    display: inline-block;
    border-radius: 16px;
    text-align: center;
    line-height: 30px;
    border: solid 1px #cacdd3;
    padding: 0 15px;
    cursor: pointer;
    &-small{
        height: 26px;
        line-height: 26px;
        padding: 0 8px;
    }
    &-red{
        background-color: @deep-color;
	    border: solid 1px @deep-color;
        color: #fff;
        &:hover{
            background-color: @default-color;
        }
        &:active{
            background-color: @deep-color;
            box-shadow: inset 0 2px 5px 0 rgba(0, 0, 0, 0.3);
        }
    }
    &-disabled{
        border: solid 1px #cacdd3;
        background-color: transparent;
        color: #878787;
        cursor: not-allowed;
    }
}
</style>
<template>
    <span class="btn" :class="{'btn-small':size =='small'}" :style="{'width':width}" @click="handleClick">
        <slot></slot>
        <span v-if="type == 'get'"><Icon type="edit" v-if="size!='small'" class="m-r-5"></Icon><span >签收</span></span>
        <span v-if="type == 'push'"><Icon type="android-upload" v-if="size!='small'" class="m-r-5"></Icon><span>上报</span></span>
        <span v-if="type == 'out'"><Icon type="shuffle" v-if="size!='small'" class="m-r-5"></Icon><span>下发</span></span>
        <span v-if="type == 'over'"><Icon type="ios-checkmark-outline" class="m-r-5" v-if="size!='small'"></Icon><span >办结</span></span>
        <span v-if="type == 'wait'"><Icon type="ios-timer-outline" class="m-r-5" v-if="size!='small'"></Icon><span >待反馈</span></span>
        <span v-if="type == 'edit'"><Icon type="ios-timer-outline" class="m-r-5" v-if="size!='small'"></Icon><span >编辑</span></span>
        <span v-if="type == 'save'"><Icon type="ios-timer-outline" class="m-r-5" v-if="size!='small'"></Icon><span >保存</span></span>
    </span>
</template>
<script>
    export default {
        name: '',
        props: {
            type:{
                type:String,
            },
            size:{
                type:String,
            },
            width:''
        },
        data() {
            return {};
        },
        mounted() {

        },
        methods: {
            handleClick(event){
                event.stopPropagation();
                this.$emit('click', event);
            }
        },
        components: {}
    };
</script>