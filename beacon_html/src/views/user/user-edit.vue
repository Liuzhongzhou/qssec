<template>
    <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
        <FormItem label="用户名" prop="username">
            <Input v-model="formValidate.username" placeholder="请输入用户名"></Input>
        </FormItem>
        <FormItem label="密码" prop="password">
            <Input type="password" v-model="formValidate.password" placeholder="请输入密码"></Input>
        </FormItem>
        <FormItem label="角色" prop="role">
            <Select v-model="formValidate.role">
                <Option v-for="item in roleList" :value="item.id" :key="item.id">{{ item.name }}</Option>
            </Select>
        </FormItem>
        <FormItem label="手机" prop="phone">
            <Input v-model="formValidate.phone" placeholder="请输入手机号码"></Input>
        </FormItem>
        <FormItem label="邮箱" prop="email">
            <Input v-model="formValidate.email" placeholder="请输入邮箱"></Input>
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
                formValidate: {
                    username: '',
                    password: '',
                    role: '',
                    phone: '',
                    email: '',
                },
                ruleValidate: {
                    username: [
                        {required: true, message: '用户名不能为空!', trigger: 'blur'}
                    ],
                    password: [
                        {required: true, message: '密码不能为空!', trigger: 'blur'},
                    ],
                    /*roleId: [
                        {required: true, message: '角色不能为空!', trigger: 'change'},
                    ],*/
                    email: [
                        {required: true, message: '邮箱不能为空!', trigger: 'blur'},
                        {type: 'email', message: '邮箱格式不正确!', trigger: 'blur'}
                    ],
                    phone: [
                        {required: true, message: '手机不能为空!', trigger: 'blur'}
                    ],
                },
                roleList: []
            }
        },
        methods: {
            init() {
                let id = parseInt(this.$route.params.id.toString());
                let data = {
                    action: 'user_info',
                    id: id
                }
                this.$axios.apipost(data, (response) => {
                    this.roleList = response.data.data.roleList
                    if (response.data.data.user) {
                        this.formValidate = response.data.data.user
                    }
                }, (err) => {
                    console.log(err);
                })
            },
            handleSubmit(name) {
                this.$refs[name].validate((valid) => {
                    if (valid) {
                        let data = {
                            action: 'user_save'
                        }
                        if (this.formValidate) {
                            data = Object.assign(data, this.formValidate);
                        }
                        this.$axios.apipost(data, (response) => {
                            this.$Message.success('保存成功!');
                            this.$router.push('/user');
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
            }
        },
        mounted() {
            this.init();
        },
    }
</script>
