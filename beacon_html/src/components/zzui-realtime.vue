<style lang="less" scoped>
    .realInfo{
        position: fixed;
        right: 0px;
        top: 46px;
        bottom: 1px;
        background: rgba(248,248,246,0.7);
        border: 1px solid #ccc;
        z-index: 1;
        &::after{
            content: '';
            position: absolute;
            width: 260px;
            right: 0px;
            top: 0px;
            bottom: 0px;
            -webkit-filter: blur(15px);
            -moz-filter: blur(15px);
            filter: blur(15px);
        }
    }
</style>
<template>
    <div class="realInfo" :style="{'width':width+'px'}">
        <slot></slot>
    </div>
</template>
<script>
    export default {
        name: '',
        props: {
            width:{
                default:'260'
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