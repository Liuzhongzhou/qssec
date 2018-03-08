<style lang="less">

</style>
<template>
    <div class="p-20">
        <div class="title-box">角色操作</div>
        <div class="bottomline m-b-10"></div>
        <div class="tool-box">
            <div class="displayIB m-r-10">
                <span class="W80 displayIB">角色名</span>
                <Input v-model="form.name" placeholder="Enter something..." clearable class="W240"></Input>
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
        <role-content :form="form" ref="userContent"></role-content>
    </div>
</template>
<script>
    import roleContent from './role-content.vue';

    export default {
        data() {
            return {
                modal: false,
                form: {
                    name: '',
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
                this.$refs.roleContent.initAjax();
            },
            cancel() {
                this.$Message.info('Clicked cancel');
            }
        },
        components: {
            roleContent
        }
    };
</script>