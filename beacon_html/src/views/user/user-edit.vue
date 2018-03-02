<template>
    <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
        <FormItem label="用户名" prop="username">
            <Input v-model="formValidate.username" placeholder="请输入用户名"></Input>
        </FormItem>
        <FormItem label="密码" prop="password">
            <Input type="password" v-model="formValidate.password" placeholder="请输入密码"></Input>
        </FormItem>
        <FormItem label="姓名" prop="user_info__chinese_name">
           <Input v-model="formValidate.user_info__chinese_name" placeholder="请输入姓名"></Input>
        </FormItem>
        <FormItem label="地址信息" prop="user_info__addr">
            <Input v-model="formValidate.user_info__addr" placeholder="请输入地址信息"></Input>
        </FormItem>
        <FormItem label="性别" prop="user_info__sex">
            <Input v-model="formValidate.user_info__sex" placeholder="请输入性别"></Input>
        </FormItem>
        <FormItem label="电话" prop="user_info__telephone">
            <Input v-model="formValidate.user_info__telephone" placeholder="请输入电话号码"></Input>
        </FormItem>
        <FormItem label="手机" prop="user_info__phone">
            <Input v-model="formValidate.user_info__phone" placeholder="请输入手机号码"></Input>
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
                    user_info__chinese_name: '',
                    user_info__addr: '',
                    user_info__sex: '',
                    user_info__telephone: '',
                    user_info__phone: '',
                },
                ruleValidate: {
                    username: [
                        {required: true, message: '用户名不能为空!', trigger: 'blur'}
                    ],
                    password: [
                        {required: true, message: '密码不能为空!', trigger: 'blur'},
                    ],
                    user_info__chinese_name: [
                        {required: true, message: '姓名不能为空!', trigger: 'blur'},
                    ],
                    user_info__telephone: [
                        {required: true, message: '电话不能为空!', trigger: 'blur'}
                    ],
                    user_info__phone: [
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
                    //this.roleList = response.data.data.roleList
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
