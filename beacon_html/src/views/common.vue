<style lang="less" scoped>
    @bg-color : #eff1f4;
    .common{
        position: relative;
        .header{
            padding: 20px;
        }
        .detail{
            padding: 0px 20px 20px;
            &-content{
                padding: 20px;
                background: @bg-color;
            }
        }
        .result{
            padding: 0px 20px 10px;
            &-list{
                overflow: hidden;
                height: 30px;
                line-height: 30px;
                & span:last-child{
                    float: right;
                }
            }
            &-title{
                height: 20px;
                line-height: 20px;
                background: @bg-color;
            }
        }
        .file{
            &-fileload{
                width: 50px;
                height: 50px;
                color: #2D8cF0;
                line-height: 50px;
            }
        }
    }
    .H32{
        height: 32px;
        line-height: 32px;
    }
</style>
<template>
    <div class="common">
        <Form ref="formValidate" :model="formValidate" label-position="left" :rules="ruleValidate" :label-width="80">
            <div class="header">
                <p class="font18 tool-box">
                    <span v-if="!editing">{{formValidate.event_name}}</span>
                    <span v-if="editing">
                        <Input v-model="formValidate.event_name" placeholder="请输入事件名称"></Input>
                    </span>
                </p>
                <div class="p-t-10">
                    <zzui-btn size="small" type="get" class="btn-red"></zzui-btn>
                    <zzui-btn size="small" type="over" class="btn-red"></zzui-btn>
                    <zzui-btn size="small" type="out" class="btn-red"></zzui-btn>
                    <zzui-btn size="small" type="push" class="btn-red"></zzui-btn>
                    <zzui-btn size="small"  class="btn-red">审核通过</zzui-btn>
                    <zzui-btn size="small"  class="btn-red">审核不通过</zzui-btn>
                    <!--<zzui-btn size="small"  class="btn-red">他人办结</zzui-btn>-->
                    <zzui-btn size="small" @click="add">新增</zzui-btn>
                    <zzui-btn size="small" @click="edit">
                        <span v-if="!editing">编辑</span>
                        <span v-if="editing">撤销编辑</span>
                    </zzui-btn>
                    <zzui-btn @click="submit" size="small" type="save"></zzui-btn>
                </div>
            </div>
            <div class="bottomline"></div>
            <div class="info p-20 p-t-10 p-b-10">
                <div class="tool-box font14">描述信息</div>
                <div class="tool-box">
                    <div class="displayIB H32 W270">
                        <FormItem  label="类型:" prop="type">
                            <span v-if="!editing" class="W180 displayIB">
                                <span v-if="formValidate.type == 1">确凿类事件</span>
                                <span v-if="formValidate.type == 2">疑似类事件</span>
                                <span v-if="formValidate.type == 3">隐患/风险类事件</span>
                            </span>
                            <Select v-if="editing" v-model="formValidate.type" class="W180">
                                <Option :value="1" key="1">确凿类事件</Option>
                                <Option :value="2" key="2">疑似类事件</Option>
                                <Option :value="3" key="3">隐患/风险类事件</Option>
                            </Select>
                        </FormItem>
                    </div>
                    <div class="displayIB H32">
                        <FormItem  label="发生时间:" prop="beginTime">
                            <span v-if="!editing" class="W180 displayIB">{{formValidate.beginTime}}</span>
                            <DatePicker format="yyyy-MM-dd HH:mm" :value="formValidate.beginTime" @on-change="beginChange" class="W180" v-if="editing" type="datetime" ></DatePicker>
                        </FormItem>
                    </div>
                </div>
                <div class="tool-box">
                    <div class="displayIB H32 W270">
                        <FormItem  label="重要程度:" prop="urgent_level">
                            <span v-if="!editing" class="W180 displayIB">
                            <span v-if="formValidate.urgent_level == 1">一般</span>
                            <span v-if="formValidate.urgent_level == 2">严重</span>
                            </span>
                            <Select v-if="editing" :value="formValidate.urgent_level" class="W180">
                                <Option :value="1" key="1">一般</Option>
                                <Option :value="2" key="2">严重</Option>
                            </Select>
                        </FormItem>
                    </div>
                    <div class="displayIB H32">
                        <FormItem  label="创建时间:" prop="addTime">
                            <span v-if="!editing" class="W180 displayIB">{{formValidate.addTime}}</span>
                            <DatePicker :value="formValidate.addTime" @on-change="addChange" class="W180" v-if="editing" type="datetime" format="yyyy-MM-dd HH:mm"></DatePicker>
                        </FormItem>
                    </div>
                </div>
                <div class="tool-box">
                    <div class="displayIB H32 W270">
                        <FormItem  label="上报部门:" prop="orgnazition">
                            <span v-if="!editing" class="W180 displayIB">{{formValidate.orgnazition}}</span>
                            <Input v-if="editing" v-model="formValidate.orgnazition" placeholder="请输入" clearable class="W180"></Input>
                        </FormItem>
                    </div>
                    <div class="displayIB H32">
                        <FormItem  label="截止时间:" prop="endTime">
                            <span v-if="!editing" class="W180 displayIB">{{formValidate.endTime}}</span>
                            <DatePicker :value="formValidate.endTime" @on-change="endChange" class="W180" v-if="editing" type="datetime" format="yyyy-MM-dd HH:mm"></DatePicker>
                        </FormItem>
                    </div>
                </div>
                <div class="tool-box">
                    <div class="displayIB H32 W270">
                         <FormItem  label="报警时间:" prop="alarmTime">
                             <span v-if="!editing" class="W180 displayIB">{{formValidate.alarmTime}}</span>
                            <DatePicker :value="formValidate.alarmTime" @on-change="alarmChange" class="W180" v-if="editing" type="datetime" format="yyyy-MM-dd HH:mm"></DatePicker>
                         </FormItem>
                    </div>
                    <div class="displayIB H32">
                        <FormItem  label="危险程度:" prop="danger_level">
                            <span v-if="!editing" class="W180 displayIB">
                                <span v-if="formValidate.danger_level == 1">一般</span>
                                <span v-if="formValidate.danger_level == 2">危险</span>
                            </span>
                            <Select v-if="editing" v-model="formValidate.danger_level" class="W180">
                                <Option :value="1" key="1">一般</Option>
                                <Option :value="2" key="2">危险</Option>
                            </Select>
                        </FormItem>
                    </div>
                </div>
            </div>
            <div class="dottedline"></div>
            <div class="source p-20 p-t-10 p-b-10">
                 <div class="tool-box font14">源信息</div>
                <div class="tool-box">
                    <div class="displayIB H32 W270">
                        <FormItem  label="源IP:" prop="source_ip">
                            <span v-if="!editing" class="W180 displayIB">{{formValidate.source_ip}}</span>
                            <Input v-if="editing" v-model="formValidate.source_ip" placeholder="请输入"  class="W180"></Input>
                        </FormItem>
                    </div>
                    <div class="displayIB H32">
                        <FormItem  label="源端口:" prop="source_port">
                            <span v-if="!editing" class="W180 displayIB">{{formValidate.source_port}}</span>
                            <Input v-if="editing" v-model="formValidate.source_port" placeholder="请输入"  class="W180"></Input>
                        </FormItem>
                    </div>
                </div>
            </div>
            <div class="dottedline"></div>
            <div class="action p-20 p-t-10 p-b-10">
                <div class="tool-box font14">目标信息</div>
                <div class="tool-box">
                    <div class="displayIB H32 W270">
                        <FormItem  label="目标IP:" prop="target_ip">
                            <span v-if="!editing" class="W180 displayIB">{{formValidate.target_ip}}</span>
                            <Input v-if="editing" v-model="formValidate.target_ip" placeholder="请输入"  class="W180"></Input>
                        </FormItem>
                    </div>
                    <div class="displayIB H32">
                        <FormItem  label="目标端口:" prop="target_port">
                            <span v-if="!editing" class="W180 displayIB">{{formValidate.target_port}}</span>
                            <Input v-if="editing" v-model="formValidate.target_port" placeholder="请输入"  class="W180"></Input>
                        </FormItem>
                    </div>
                </div>
            </div>
            <div class="dottedline"></div>
            <div class="file p-20 p-t-10 p-b-10">
                <div class="tool-box font14">证据材料</div>
                <div class="tool-box overHidden">
                    <div class="file-content fLeft" style="width: 50px;margin-right: 10px" v-for="f in file">
                        <div class="center file-fileload">
                            <Icon style="font-size: 40px" type="clipboard"></Icon>
                        </div>
                        <p class="center">{{f.name}}</p>
                    </div>
                    <Upload
                        :before-upload="handleUpload"
                        action="//jsonplaceholder.typicode.com/posts/">
                        <Button type="ghost" class="font18"><Icon type="plus"></Icon></Button>
                    </Upload>
                </div>
            </div>
             <div class="dottedline"></div>
            <div class="tool-box p-l-20 font14">事件内容</div>
            <div class="detail">
                <div class="detail-content">
                    Cold calling can be a great way to generate quality leads. You get to speak to the gatekeepers and stakeholders, and you get a great insight into their requirements and influences. But cold calling is an art-form. It can be daunting, it’s always a lot of work, and you always need to make a good impression. So you need to do it right. Following are some tips which will help you do just that.

                    1) Record everything
                </div>
            </div>
             <div class="bottomline"></div>
            <div class="tool-box p-l-20 font14">处理结果</div>
            <div class="result">
                <div class="result-list result-title" >
                    <span>部门名称</span>
                    <span>事件状态</span>
                </div>
                <div class="result-list">
                    <span>部门名称</span>
                    <span>事件状态</span>
                </div>
            </div>
            <div class="bottomline"></div>
            <div class="tool-box p-l-20 font14">流转记录</div>
        </Form>
    </div>
</template>
<script>
    import zzuiBtn from '../components/zzui-btn.vue';
    export default {
        name: 'common',
        props: {
            eventInfo:{},
        },
        data() {
            return {
                formValidate: {
                    event_name: '郑州事件名称郑州事件名称',
                    status:'0',
                    type: '423432',
                    urgent_level: '432432',
                    orgnazition: '432',
                    event_code:'',
                    alarmTime: '',
                    beginTime: '',
                    addTime: '',
                    endTime: '',
                    danger_level: '范德萨',
                    source_ip:'范德萨',
                    source_port:'范德萨',
                    target_ip:'范德萨',
                    target_port:'范德萨',
                },
                ruleValidate: {
                    source_ip: [
                        {required: true, message: 'ip不能为空!', trigger: 'blur'}
                    ],
                     source_port: [
                        {required: true, message: '端口不能为空!', trigger: 'blur'}
                    ],
                    target_ip: [
                        {required: true, message: 'ip不能为空!', trigger: 'blur'}
                    ],
                     target_port: [
                        {required: true, message: '端口不能为空!', trigger: 'blur'}
                    ],
                },
                file:[],
                editing:false,
            };
        },
        mounted() {
            this.initStatusNull();
        },
        methods: {
            beginChange(val){
                this.formValidate.beginTime = val;
            },
            addChange(val){
                this.formValidate.addTime = val;
            },
            endChange(val){
                this.formValidate.endTime = val;
            },
            alarmChange(val){
                this.formValidate.alarmTime = val;
            },
            add(){
                this.editing = true;
            },
            edit(){
                this.editing = !this.editing;
            },
            submit(){
                this.$emit('submit',this.formValidate,()=> {
                    this.editing = false;
                });
            },
            initStatusNull(){
                this.editing = false;
            },
            handleUpload (file) {
                this.file.push(file);
                return false;
            },
        },
        watch:{
            'eventInfo'(){
                this.initStatusNull();
                for(let i in this.eventInfo){
                    this.formValidate[i] = this.eventInfo[i];
                }
            }
        },
        components: {
            zzuiBtn
        }
    };
</script>