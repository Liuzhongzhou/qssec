<style lang="less" scoped>
    .filewrap{
        width: 180px;
        border-radius: 6px;
        margin-right: 16px;
        padding: 8px 8px 0px;
        cursor: pointer;
        border: dashed 2px transparent;
        &:hover{
             border: dashed 2px #f5a623;
        }
        &-active{
            border: dashed 2px #f5a623;
        }
        .filebg{
            text-align: center;
            position: relative;
            .filesign{
                position: absolute;
                left: -6px;
                top: 8px;
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
                    border-left: 9px solid transparent;
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
            .filecontent{
                position: absolute;
                width: 80%;
                left: 10%;
                right: 8%;
                bottom: 8%;
                top: 32%;
                color: #c9780b;
                &-name{
                    height: 36px;
                }
                &-time{
                    margin-top: 5%;
                }
                &-type{
                    margin-top: 5%;
                }
                &-btn{
                    position: absolute;
                    bottom: 0px;
                    width: 100%;
                }
            }
        }
    }
</style>
<template>
    <div @click="handleClick" class="filewrap" :style="{'width':width}" :class="{'filewrap-active':check}">
        <div class="filebg">
            <img src="../assets/image/file.png" style="width: 100%;font-size: 0px" alt="">
            <div class="filesign filesign-error" v-if="type == 'error'">严重</div>
            <div class="filesign filesign-normal" v-if="type == 'normal'">一般</div>
            <div class="filecontent">
                <p class="filecontent-name"><slot name="name"></slot></p>
                <p class="filecontent-time"><slot name="time"></slot></p>
                <p class="filecontent-type"><slot name="type"></slot></p>
                <p class="filecontent-btn"><slot name="btn"></slot></p>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'file',
        props: {
            type:{},
            check:'',
            width:'',
        },
        data() {
            return {};
        },
        mounted() {

        },
        methods: {
            handleClick(event){
                event.preventDefault();
                this.$emit('click', event);
            }
        },
        components: {}
    };
</script>