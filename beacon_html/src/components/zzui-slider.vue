<style lang="less" scoped>
    .slider{
        width: 600px;
        position: absolute;
        top: 0px;
        bottom: 0px;
        right: 0px;
        padding: 40px 30px 0px 30px;
        background-color: #fffcf5;
        z-index: 1;
        &-close{
            font-size: 20px;
            position: absolute;
            top: 3px;
            right: 7px;
        }
    }
</style>
<template>
    <div class="slider">
        <a href="javascript:;"><Icon type="android-close" class="slider-close"></Icon></a>
        <slot></slot>
    </div>
</template>
<script>
    export default {
        name: '',
        props: {},
        data() {
            return {};
        },
        mounted() {

        },
        methods: {},
        components: {}
    };
</script>