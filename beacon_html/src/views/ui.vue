<style lang="less">

</style>
<template>
    <div class="p-l-25">
        <h3 class="tool-box">按钮</h3>
        <zzui-btn>项目开发</zzui-btn>
        <zzui-btn @click="alert(1)" class="btn-red">项目开发</zzui-btn>
        <zzui-btn class="btn-disabled" size="small" type="wait"></zzui-btn>
        <zzui-btn class="btn-disabled" type="over"></zzui-btn>
        <zzui-btn class="btn-disabled" type="get"></zzui-btn>
        <zzui-btn class="btn-disabled" type="out"></zzui-btn>

        <h3 class="tool-box">文件夹</h3>
        <zzui-file @click="checkfile(0)" type="normal" :check="0 == index"></zzui-file>
        <zzui-file @click="checkfile(1)" type="error" :check="1 == index"></zzui-file>
    </div>
</template>
<script>
    import zzuiBtn from '../components/zzui-btn.vue';
    import zzuiFile from '../components/zzui-file.vue';
    export default {
        data() {
            return {
                index:0,
            };
        },
        mounted() {
        },
        methods: {
            checkfile(index){
                this.index = index;
            },
            alert(index){
                alert(index)
            }
        },
        components: {
            zzuiBtn,
            zzuiFile
        }
    };
</script>