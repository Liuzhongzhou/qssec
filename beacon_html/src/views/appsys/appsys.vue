<style lang="less">

</style>
<template>
    <div class="p-20">
        <div class="title-box">应用系统操作</div>
        <div class="bottomline m-b-10"></div>
        <div class="tool-box">
            <div class="displayIB m-r-10">
                <span class="W80 displayIB">应用系统名称</span>
                <Input v-model="form.app_name" placeholder="Enter something..." clearable class="W240"></Input>
            </div>
            <div class="displayIB">
                <span class="W80 displayIB">ip地址</span>
                <Input v-model="form.app_ip" placeholder="Enter something..." clearable class="W240"></Input>
            </div>
            <div class="displayIB ">
                <Button type="primary" @click="search">查询数据</Button>
            </div>
        </div>
        <Modal
                v-model="modal"
                title="Common Modal dialog box title"
                @on-ok="ok"
                @on-cancel="cancel">
            <p>Content of dialog</p>
            <p>Content of dialog</p>
            <p>Content of dialog</p>
        </Modal>
        <appsys-content :form="form" ref="appsysContent"></appsys-content>
    </div>
</template>
<script>
    import appsysContent from './appsys-content.vue';

    export default {
        data() {
            return {
                modal: false,
                form: {
                    app_name: '',
                    app_ip: '',
                    city_code: '',
                }
            };
        },
        mounted() {
        },
        methods: {
            modalfn() {
                this.modal = true;
            },
            ok() {
                this.$Message.info('Clicked ok');
            },
            search() {
                this.$refs.appsysContent.initAjax();
            },
            cancel() {
                this.$Message.info('Clicked cancel');
            }
        },
        components: {
            appsysContent
        }
    };
</script>