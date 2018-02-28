<style lang="less" scoped>

</style>
<template>
    <div>
        <div class="title-box">用户操作</div>
        <div class="bottomline m-b-10"></div>
        <div class="tool-box">
            <div class="displayIB m-r-10">
                <span class="W80 displayIB">用户名</span>
                <Input v-model="form.username" placeholder="Enter something..." clearable class="W240"></Input>
            </div>
            <div class="displayIB">
                <span class="W80 displayIB">电话号码</span>
                <Input v-model="form.phone" placeholder="Enter something..." clearable class="W240"></Input>
            </div>
        </div>
        <div class="tool-box">
            <div class="displayIB m-r-10">
                <span class="W80 displayIB">邮箱 </span>
                <Input v-model="form.email" placeholder="Enter something..." clearable class="W240"></Input>
            </div>
            <div class="displayIB ">
                <Button type="primary" @click="search">查询数据</Button>
            </div>
        </div>
        <!--<zzui-slider></zzui-slider>-->
        <Modal
                v-model="modal"
                title="Common Modal dialog box title"
                @on-ok="ok"
                @on-cancel="cancel">
            <p>Content of dialog</p>
            <p>Content of dialog</p>
            <p>Content of dialog</p>
        </Modal>
        <user-content :form="form" ref="userContent"></user-content>
    </div>
</template>
<script>
    import userContent from './user-content.vue';
    import Btn from '../../components/zzui-btn.vue';
    import zzuiSlider from '../../components/zzui-slider.vue';
    import zzuiFile from '../../components/zzui-file.vue';

    export default {
        data() {
            return {
                modal: false,
                form: {
                    username: '',
                    phone: '',
                    email: '',
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
                this.$refs.userContent.initAjax();
            },
            cancel() {
                this.$Message.info('Clicked cancel');
            }
        },
        components: {
            userContent,
            Btn,
            zzuiFile,
            zzuiSlider
        }
    };
</script>