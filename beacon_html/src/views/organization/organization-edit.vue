<template>
    <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
        <FormItem label="父机构" prop="name">
            <Input v-model="formValidate.name" placeholder="请输入角色名"></Input>
        </FormItem>
        <FormItem label="备注" prop="comment">
            <Input v-model="formValidate.comment" type="textarea" placeholder="请输入备注"></Input>
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
                ruleValidate: {
                    name: [
                        {required: true, message: '角色名不能为空!', trigger: 'blur'}
                    ],
                }
            }
        },
        methods: {
            init() {
                let id = parseInt(this.$route.params.id.toString());
                let data = {
                    action: 'role_info',
                    id: id
                }
                this.$axios.apipost(data, (response) => {
                    this.menudata = response.data.data.menu_lists;
                    if (response.data.data.role) {
                        this.formValidate = response.data.data.role;
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
                            action: 'role_save'
                        }
                        if (this.formValidate) {
                            data = Object.assign(data, this.formValidate);
                        }
                        this.$axios.apipost(data, (response) => {
                            this.$Message.success('保存成功!');
                            this.$router.push('/role');
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
