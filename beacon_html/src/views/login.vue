<style lang="less">
    .bg{
        width: 100%;
        height: 100%;
        background: url("../assets/image/login_bg.jpg") 50% center;
        background-size: cover;
        position: relative;
    }
    .login-content{
        width: 300px;
        padding: 20px 20px 0px 20px;
        position: absolute;
        top: 50%;
        right: 10%;
        border-radius: 10px;
        transform: translateY(-50%);
        background-color: rgba(255 , 255 , 255 ,0.5);
    }
</style>
<template>
    <div class="bg">
        <div class="login-content">
            <Form ref="formCustom" :model="formCustom" label-position="left" :rules="ruleCustom" :label-width="50">
                <Form-item label="用户名" prop="username">
                    <Input type="text" v-model="formCustom.username"></Input>
                </Form-item>
                <Form-item label="密码" prop="password">
                    <Input type="password" v-model="formCustom.password"></Input>
                </Form-item>
                <Form-item>
                    <Button type="primary" @click="handleSubmit('formCustom')">登录</Button>
                </Form-item>
            </Form>
        </div>
    </div>
</template>
<script>
    export default {
        data() {
            const validatePass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入密码'));
                } else {
                    callback();
                }
            };
            const validateUserName = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入用户名'));
                } else {
                    callback();
                }
            };
            return {
                formCustom: {
                    password: '',
                    username: '',
                },
                ruleCustom: {
                    password: [
                        {validator: validatePass, trigger: 'blur'}
                    ],
                    username: [
                        {validator: validateUserName, trigger: 'blur'}
                    ],
                }
            };
        },
        mounted() {

        },
        methods: {
            handleSubmit(params) {
                this.$refs[params].validate((valid) => {
                    if (valid) {
                        this.$axios.post('login', {
                            'username': this.formCustom.username,
                            'password': this.formCustom.password,
                        }, (response) => {
                            console.log(response.data);
                            if (response.data && response.data.return_code == 1) {
                                this.$Message.success('连接成功!');
                                localStorage.setItem('user_name',response.data.data.user_name);
                                this.$router.push({'name':'home'});
                            } else {
                                this.$Message.error('失败!');
                            }
                        })
                    }
                })
            }
        },
        components: {

        }
    };
</script>