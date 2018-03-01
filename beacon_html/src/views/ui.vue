<style lang="less">

</style>
<template>
    <div class="p-l-25">

        <h3 class="tool-box">按钮</h3>
        <zzui-btn class="btn-red">项目开发</zzui-btn>
        <zzui-btn class="btn-disabled" type="wait"></zzui-btn>
        <zzui-btn class="btn-disabled" type="over"></zzui-btn>
        <zzui-btn class="btn-disabled" type="get"></zzui-btn>
        <zzui-btn class="btn-disabled" type="out"></zzui-btn>

        <h3 class="tool-box">文件夹</h3>
        <zzui-file type="normal"></zzui-file>
        <zzui-file type="error"></zzui-file>
    </div>
</template>
<script>
    import zzuiBtn from '../components/zzui-btn.vue';
    import zzuiFile from '../components/zzui-file.vue';
    export default {
        data() {
            return {};
        },
        mounted() {
            setflow();
        },
        methods: {

        },
        components: {
            zzuiBtn,
            zzuiFile
        }
    };
</script>