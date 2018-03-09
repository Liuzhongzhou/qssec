<style lang="less" scoped>
    @bg-color : #eff1f4;
    .common{
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
    }
</style>
<template>
    <div class="common">
        <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
            <div class="header">
                <p class="font18 tool-box">
                    <span v-if="!editing">{{formValidate.eventName}}</span>
                    <span v-if="editing">
                        <Input v-model="formValidate.eventName" placeholder="请输入事件名称"></Input>
                    </span>
                </p>
                <div class="p-t-10">
                    <zzui-btn size="small" type="get" class="btn-red"></zzui-btn>
                    <zzui-btn size="small" type="over" class="btn-red"></zzui-btn>
                    <zzui-btn size="small" type="out" class="btn-red"></zzui-btn>
                    <zzui-btn size="small" type="wait" class="btn-red"></zzui-btn>
                    <zzui-btn size="small" @click="edit" type="edit"></zzui-btn>
                    <zzui-btn size="small" type="save"></zzui-btn>
                </div>
            </div>
            <div class="bottomline"></div>
            <div class="info p-20">
                <div class="tool-box">
                    <div class="displayIB W260">
                        <span class="W60 displayIB">类型：</span>
                        <span v-if="!editing" class="W180 displayIB">
                            <span v-if="formValidate.type == 1">确凿类事件</span>
                            <span v-if="formValidate.type == 2">疑似类事件</span>
                            <span v-if="formValidate.type == 3">隐患/风险类事件</span>
                        </span>
                        <Select v-if="editing" v-model="formValidate.type" class="W180">
                            <Option value="1" key="1">确凿类事件</Option>
                            <Option value="2" key="2">疑似类事件</Option>
                            <Option value="3" key="3">隐患/风险类事件</Option>
                        </Select>
                    </div>
                    <div class="displayIB">
                        <span class="W60 displayIB">发生时间:</span>
                        <span v-if="!editing" class="W180 displayIB">{{formValidate.beginTime}}</span>
                        <DatePicker v-model="formValidate.beginTime" class="W180" v-if="editing" type="datetime" format="yyyy-MM-dd HH:mm"></DatePicker>
                    </div>
                </div>
                <div class="tool-box">
                    <div class="displayIB W260">
                        <span class="W60 displayIB">重要程度：</span>
                        <span v-if="!editing" class="W180 displayIB">{{formValidate.level}}</span>
                        <Input v-if="editing" v-model="formValidate.level" placeholder="请输入" clearable class="W180"></Input>
                    </div>
                    <div class="displayIB">
                        <span class="W60 displayIB">创建时间:</span>
                       <span v-if="!editing" class="W180 displayIB">{{formValidate.addTime}}</span>
                        <DatePicker v-model="formValidate.addTime" class="W180" v-if="editing" type="datetime" format="yyyy-MM-dd HH:mm"></DatePicker>
                    </div>
                </div>
                <div class="tool-box">
                    <div class="displayIB W260">
                        <span class="W60 displayIB">上报部门：</span>
                        <span v-if="!editing" class="W180 displayIB">{{formValidate.orgnazition}}</span>
                        <Input v-if="editing" v-model="formValidate.orgnazition" placeholder="请输入" clearable class="W180"></Input>
                    </div>
                    <div class="displayIB">
                        <span class="W60 displayIB">截止时间:</span>
                       <span v-if="!editing" class="W180 displayIB">{{formValidate.endTime}}</span>
                        <DatePicker v-model="formValidate.endTime" class="W180" v-if="editing" type="datetime" format="yyyy-MM-dd HH:mm"></DatePicker>
                    </div>
                </div>
                <div class="tool-box">
                    <div class="displayIB W260">
                        <span class="W60 displayIB">报警时间：</span>
                        <span v-if="!editing" class="W180 displayIB">{{formValidate.alarmTime}}</span>
                        <DatePicker v-model="formValidate.alarmTime" class="W180" v-if="editing" type="datetime" format="yyyy-MM-dd HH:mm"></DatePicker>
                    </div>
                    <div class="displayIB">
                        <span class="W60 displayIB">危险程度:</span>
                        <span v-if="!editing" class="W180 displayIB">{{formValidate.errorLevel}}</span>
                        <Select v-if="editing" v-model="formValidate.errorLevel" class="W180">
                            <Option>一般</Option>
                            <Option>危险</Option>
                        </Select>
                    </div>
                </div>
            </div>
            <div class="dottedline"></div>
            <div class="source p-20">
                 <div class="tool-box">源信息</div>
                <div class="tool-box">
                    <div class="displayIB W260">
                        <span class="W60 displayIB">源IP：</span>
                        <span v-if="!editing" class="W180 displayIB">{{formValidate.sourceIp}}</span>
                        <Input v-if="editing" v-model="formValidate.sourceIp" placeholder="请输入" clearable class="W180"></Input>
                    </div>
                    <div class="displayIB">
                        <span class="W60 displayIB">源端口:</span>
                       <span v-if="!editing" class="W180 displayIB">{{formValidate.sourcePoint}}</span>
                        <Input v-if="editing" v-model="formValidate.sourcePoint" placeholder="请输入" clearable class="W180"></Input>
                    </div>
                </div>
            </div>
            <div class="dottedline"></div>
            <div class="action p-20">
                <div class="tool-box">目标信息</div>
                <div class="tool-box">
                    <div class="displayIB W260">
                        <span class="W60 displayIB">目的IP：</span>
                        <span v-if="!editing" class="W180 displayIB">{{formValidate.aimIp}}</span>
                        <Input v-if="editing" v-model="formValidate.aimIp" placeholder="请输入" clearable class="W180"></Input>
                    </div>
                    <div class="displayIB">
                        <span class="W60 displayIB">源端口:</span>
                       <span v-if="!editing" class="W180 displayIB">{{formValidate.aimPoint}}</span>
                        <Input v-if="editing" v-model="formValidate.aimPoint" placeholder="请输入" clearable class="W180"></Input>
                    </div>
                </div>
            </div>
            <div class="dottedline"></div>
            <div class="file p-20">
                <div class="tool-box">证据材料</div>
                <div class="tool-box overHidden">
                    <!--<div class="file-content fLeft" style="width: 50px">
                        <div style="width: 50px;height: 50px;background: white;" class="center">
                            <Icon style="font-size: 40px" type="clipboard"></Icon>
                        </div>
                        <p class="center">文件1</p>
                    </div>-->
                    <Upload action="">
                        <Button type="ghost" icon="ios-cloud-upload-outline">Upload files</Button>
                    </Upload>
                </div>
            </div>
             <div class="dottedline"></div>
            <div class="tool-box p-l-20">事件内容</div>
            <div class="detail">
                <div class="detail-content">
                    Cold calling can be a great way to generate quality leads. You get to speak to the gatekeepers and stakeholders, and you get a great insight into their requirements and influences. But cold calling is an art-form. It can be daunting, it’s always a lot of work, and you always need to make a good impression. So you need to do it right. Following are some tips which will help you do just that.

                    1) Record everything
                </div>
            </div>
             <div class="bottomline"></div>
            <div class="tool-box p-l-20">处理结果</div>
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
            <div class="tool-box p-l-20">流转记录</div>
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
                    eventName: '郑州事件名称郑州事件名称',
                    type: '423432',
                    level: '432432',
                    orgnazition: '432',
                    alarmTime: '',
                    beginTime: '',
                    addTime: '',
                    endTime: '',
                    errorLevel: '范德萨',
                    sourceIp:'范德萨',
                    sourcePoint:'范德萨',
                    aimIp:'范德萨',
                    aimPoint:'范德萨',
                },
                ruleValidate: {},
                editing:false,
            };
        },
        mounted() {

        },
        methods: {
            edit(){
                this.editing = !this.editing;
            }
        },
        components: {
            zzuiBtn
        }
    };
</script>