<style lang="less" scoped>
    @import "../assets/css/conf";
    @num-prefix-cls:~"@{newcss-prefix}-aninum";
    .@{num-prefix-cls}{
        font-size: 30px;
        text-align: center;
        &-primary{
            color: @primary-color;
        }
        &-success{
            color: @success-color;
        }
        &-warning{
            color: @warning-color;
        }
        &-error{
            color: @error-color;
        }
    }
</style>
<template>
    <div>
        <p :class="className" :style="styles"><span :id="'count'+id">{{numItem}}</span><span>{{unit}}</span></p>
    </div>
</template>
<script>
    import CountUp from 'countup';
    const prefixCls = 'zzui-aninum';
    export default {
        name:'AnimateNumber',
        props:{
            id:{
                type:String,
                default:'0',
            },
            num:{
                type:Number,
                default:0
            },
            styles:{
                type:Object,
            },
            color:{
                type:String,
            }
        },
        data() {
            return {
                unit:'',
                numItem:0,
            };
        },
        computed: {
            className(){
                return [
                    `${prefixCls}`,
                    {
                        [`${prefixCls}-primary`]:this.color === 'primary',
                        [`${prefixCls}-success`]:this.color === 'success',
                        [`${prefixCls}-warning`]:this.color === 'warn',
                        [`${prefixCls}-error`]:this.color === 'error',
                    }
                ]
            }
        },
        methods: {
            init(){
                let num_for = this.formatNumber(this.num);
                this.unit = num_for.unit;
                let target = 'count'+this.id,
                    startval = 0,
                    endval = num_for.count,
                    decimals = num_for.decimals,
                    duration = 2;
                try {
                    let ani = new CountUp(target,startval,endval, decimals,duration);
                    if (!ani.error) {
                      ani.start();
                    } else {
                        this.numItem = num_for.count;
                        console.error(ani.error);
                    }
                }catch(e){
                    console.error(e);
                    this.numItem = num_for.count;
                }

            },
            formatNumber(param){
                let count = 0 , unit = '',decimals = 2;
                if(param < 10000){
                    count = param;
                    decimals = 0;
                }else if(param >= 10000 && param < 100000000){
                    count = param / 10000 , unit = '万+'
                }else{
                    count = param / 100000000, unit = '亿+'
                };
                return {
                    count,
                    unit,
                    decimals
                }
            }
        },
        watch:{
            'num':function () {
                setTimeout(()=>{
                    this.init();
                },500);
            }
        }
    };
</script>