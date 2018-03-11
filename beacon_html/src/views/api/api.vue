<style lang="less" scoped>

</style>
<template>
    <div>
        <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
            <FormItem label="接口json" prop="json">
                <Input v-model="formValidate.json" placeholder="{action:''}" type="textarea" :rows="12"></Input>
            </FormItem>
            <FormItem>
                <Button type="primary" @click="handleSubmit('formValidate')">提交</Button>
                <Button type="ghost" @click="handleReset('formValidate')" style="margin-left: 8px">重置</Button>
            </FormItem>
            <FormItem label="返回结果">
                <Input v-model="content" placeholder="返回结果" type="textarea" :rows="22"></Input>
            </FormItem>
        </Form>
    </div>
</template>
<script>

    export default {
        data() {
            return {
                formValidate: {
                    json: '{\'action\':\'\'}',
                },
                content: '',
                ruleValidate: {
                    json: [
                        {required: true, message: '接口json不能为空!', trigger: 'blur'}
                    ],
                },
            };
        },
        methods: {
            handleSubmit(name) {
                this.$refs[name].validate((valid) => {
                    if (valid) {
                        let data = eval('(' + this.formValidate.json + ')');
                        this.$axios.apipost(data, (response) => {
                            this.content = JSON.stringify(response);
                        }, (err) => {
                            this.content = err;
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
    };
</script>