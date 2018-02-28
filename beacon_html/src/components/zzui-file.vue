<style lang="less" scoped>
    .filewrap{
        width: 202px;
        height: 248px;
        border-radius: 6px;
        padding-left: 16px;
        padding-top: 11px;
        display: inline-block;
        cursor: pointer;
        border: dashed 2px transparent;
        &:hover{
             border: dashed 2px #f5a623;
        }
        &:active{
             border: dashed 2px #f5a623;
        }
        .filebg{
            width: 166px;
            height: 224px;
            background: url("../assets/image/file.png") 0 0;
            background-size: cover;
            padding-top: 80px;
            text-align: center;
            position: relative;
            .filesign{
                position: absolute;
                left: -8px;
                top: 11px;
                color: #fff;
                width: 64px;
                height: 25px;
                line-height: 25px;
                border-radius: 2px;
                z-index: 0;
                &:after{
                    content: '';
                    width: 0;
                    height: 0;
                    position: absolute;
                    left: 0px;
                    top:-7px;
                    z-index: 0;
                    border-left: 11px solid transparent;
                }
            }
            .filesign-error{
                background-image: linear-gradient(111deg, #e93535, #cb1b1b);
                box-shadow: 2px 1px 5px 0 rgba(113, 0, 0, 0.5);
                &:after{
                     border-bottom: 8px solid #c32515;
                }
            }
            .filesign-normal{
                background-image: linear-gradient(111deg, #35bde9, #1b60cb);
	            box-shadow: 2px 1px 5px 0 rgba(53,189,233, 0.5);
                &:after{
                     border-bottom: 8px solid #1b60cb;
                }
            }
        }
    }
</style>
<template>
    <div class="filewrap">
        <div class="filebg">
            <div class="filesign filesign-error" v-if="type == 'error'">严重</div>
            <div class="filesign filesign-normal" v-if="type == 'normal'">一般</div>
            <slot></slot>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'file',
        props: {
            type:{}
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