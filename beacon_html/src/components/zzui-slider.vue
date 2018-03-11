<style lang="less" scoped>
    .slider{
        width: 575px;
        position: absolute;
        top: 0px;
        right: 0px;
        bottom: 0px;
        overflow: hidden;
        border-left: 1px solid #d3d8df;
        background-color: #f5f7f9;
        z-index: 1;
        &-inner{
            width: 595px;
            overflow-x: hidden;
            overflow-y: auto;
            height: 100%;
            padding-right: 20px;
        }
        &-close{
            font-size: 20px;
            position: absolute;
            top: 3px;
            right: 7px;
            z-index: 2;
        }
    }
</style>
<template>
    <div class="slider" :style="{'width':width}">
        <a href="javascript:;" @click="cancel"><Icon type="android-close" class="slider-close"></Icon></a>
        <div class="slider-inner">
            <slot></slot>
        </div>
    </div>
</template>
<script>
    export default {
        name: '',
        props: {
            width:''
        },
        data() {
            return {};
        },
        mounted() {

        },
        methods: {
            cancel(){
                this.$emit('cancel')
            }
        },
        components: {}
    };
</script>