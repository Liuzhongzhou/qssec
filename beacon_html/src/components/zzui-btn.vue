<style lang="less" scoped>
    @import "../assets/css/conf";
.btn{
    height: 32px;
    display: inline-block;
    border-radius: 16px;
    text-align: center;
    line-height: 32px;
    border: solid 1px #cacdd3;
    padding: 0 15px;
    cursor: pointer;
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
    <span class="btn">
        <slot></slot>
        <span v-if="type == 'get'"><Icon type="edit"></Icon><span class="m-l-5">签收</span></span>
        <span v-if="type == 'out'"><Icon type="shuffle"></Icon><span class="m-l-5">下发</span></span>
        <span v-if="type == 'over'"><Icon type="ios-checkmark-outline"></Icon><span class="m-l-5">办结</span></span>
        <span v-if="type == 'wait'"><Icon type="ios-timer-outline"></Icon><span class="m-l-5">待反馈</span></span>
    </span>
</template>
<script>
    export default {
        name: '',
        props: {
            type:{
                type:String,
                default:''
            },
            width:{

            }
        },
        data() {
            return {};
        },
        mounted() {

        },
        methods: {},
        components: {}
    };
</script>