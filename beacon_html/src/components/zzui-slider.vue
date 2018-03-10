<style lang="less" scoped>
    .slider{
        width: 575px;
        position: absolute;
        top: 0px;
        right: 0px;
        border-left: 1px solid #d3d8df;
        background-color: #f5f7f9;
        z-index: 1;
        overflow-x: hidden;
        overflow-y: auto;
        &-close{
            font-size: 20px;
            position: absolute;
            top: 3px;
            right: 7px;
        }
    }
</style>
<template>
    <div class="slider" :style="{'width':width}">
        <a href="javascript:;" @click="cancel"><Icon type="android-close" class="slider-close"></Icon></a>
        <slot></slot>
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