<style lang="less">
    .node rect {
        stroke: #333;
              fill: #999;
    }

    .edgePath path {
        stroke: #333;
        fill: #333;
        stroke - width: 1.5px;
    }
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

        <h3 class="tool-box">流程图demo</h3>
        <div>
             <svg width=960 height=600><g/></svg>
        </div>
    </div>
</template>
<script>
    import zzuiBtn from '../components/zzui-btn.vue';
    import zzuiFile from '../components/zzui-file.vue';
    import {setflow} from '../assets/js/flowsheet';
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