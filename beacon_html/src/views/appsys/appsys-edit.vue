<template>
    <Form ref="formValidate" :model="formValidate" :appsys="appsysValidate" :label-width="80">
        <FormItem label="应用系统名" prop="app_name" >
            <Input v-model="formValidate.name" placeholder="请输入应用系统名称"></Input>
        </FormItem>
         <FormItem label="ip地址" prop="app_ip">
            <Input v-model="formValidate.name" placeholder="请输入ip地址"></Input>
        </FormItem>
         <FormItem label="端口" prop="app_port">
            <Input v-model="formValidate.name" placeholder="请输入端口"></Input>
        </FormItem>
         <FormItem label="所属地市" prop="city_code">
            <Input v-model="formValidate.name" placeholder="请输入所属地市"></Input>
        </FormItem>

        <FormItem>
            <Button type="primary" @click="handleSubmit('formValidate')">提交</Button>
            <Button type="ghost" @click="handleReset('formValidate')" style="margin-left: 8px">重置</Button>
        </FormItem>
    </Form>
</template>
<script>
    export default {
        data() {
            return {
                menudata: [],
                formValidate: {
                    name: '',
                    comment: '',
                    menus: ''
                },
                appsysValidate: {
                    app_name: [
                        {required: true, message: '应用系统名称不能为空!', trigger: 'blur'}
                    ],
                     app_ip: [
                        {required: true, message: 'ip地址不能为空!', trigger: 'blur'}
                    ],
                     app_port: [
                        {required: true, message: '端口不能为空!', trigger: 'blur'}
                    ],
                     city_code: [
                        {required: true, message: '所属地市不能为空!', trigger: 'blur'}
                    ],
                }
            }
        },
        methods: {
            init() {
                let app_code = this.$route.params.app_code.toString();
                let data = {
                    action: 'appsys_info',
                    app_code: app_code
                }
                this.$axios.apipost(data, (response) => {
                    if (response.data.data) {
                        this.formValidate = response.data.data;
                    }
                    this.$nextTick(() => {
                        this.checkChange();
                    });
                }, (err) => {
                    console.log(err);
                })
            },
            handleSubmit(name) {
                this.$refs[name].validate((valid) => {
                    if (valid) {
                        let data = {
                            action: 'appsys_save'
                        }
                        if (this.formValidate) {
                            data = Object.assign(data, this.formValidate);
                        }
                        this.$axios.apipost(data, (response) => {
                            this.$Message.success('保存成功!');
                            this.$router.push('/appsys');
                        }, (err) => {
                            console.log(err);
                        })
                    } else {
                        this.$Message.error('验证失败!');
                    }
                })
            },
            handleReset(name) {
                this.$refs[name].resetFields();
            },
            checkChange() {
                let nodes = this.$refs.tree.getCheckedNodes();
                let codes = '';
                if (nodes.length) {
                    nodes.forEach(function (i, index) {
                        codes += ((index > 0 ? ',' : '') + i.code)
                    })
                }
                this.formValidate.menus = codes;
            },

        },
        mounted() {
            this.init();
        }
    }
</script>
