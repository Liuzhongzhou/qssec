<style lang="less" scoped>
    @import "../assets/css/conf";
    @circle-prefix-cls:~"@{newcss-prefix}-circle";
    .@{circle-prefix-cls}{
        position: relative;
        &-content{
            position: absolute;
            width: 100%;
            top: 50%;
            transform: translate(0,-50%);
            text-align: center;
        }
        &-path2{
            transition:stroke-dasharray .25s;
        }
    };
</style>
<template>
    <div :style="circleSize" :class="wrapClass">
        <div>
            <svg :width="size" :height="size">
                <circle class="path" :fill-opacity="0" :cx="size/2" :cy="size/2" :r="crSize" stroke="#eaeef2" fill="none" :stroke-width="strokeWidth1" stroke-dashoffset="1"></circle>
                <circle :class="path2" :style="move" :fill-opacity="0" :cx="size/2" :cy="size/2" :r="crSize" stroke="#2db7f5" fill="none" :stroke-width="strokeWidth2"  :transform="rotate"></circle>
            </svg>
        </div>
        <div :class="conentClass">
            <slot></slot>
        </div>
    </div>
</template>
<script>
    const prefixCls = 'zzui-circle';
    export default {
        name:'zzuiCircle',
        props:{
            size:{
                type:Number,
                default:500
            },
            percent:{
                type:Number,
                default:0
            }
        },
        data() {
            return {
                dasharray:"0px,0px",
                strokeWidth1:8,
                strokeWidth2:12,
            };
        },
        mounted() {

        },
        computed:{
            circleSize(){
                return {
                    width:`${this.size}`+'px',
                    height:`${this.size}`+'px'
                }
            },
            move(){
                return `stroke-dasharray:${6.28 * this.size /2 * this.percent}px,${6.28 * this.size /2 + 1}px`;
            },
            wrapClass(){
                return `${prefixCls}`
            },
            conentClass(){
                return `${prefixCls}-content`
            },
            path2(){
                return `${prefixCls}-path2`
            },
            crSize(){
                return (this.size - this.strokeWidth2 ) / 2;
            },
            rotate(){
                return  `rotate(-90,${this.size/2},${this.size/2})`
            }
        },
        methods: {},
        components: {}
    };
</script>