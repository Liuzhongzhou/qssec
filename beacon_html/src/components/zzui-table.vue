<style scoped>
    #tableList {
        width: 100%;
        height: 100%;
        min-height: 500px;
        position: relative;
    }

    .table-title {
        line-height: 40px;
        height: 40px;
        overflow: hidden;
    }

    .table-bottom {
        position: absolute;
        height: 30px;
        bottom: 0px;
        left: 0px;
        padding-right: 20px;
        width: 100%;
        overflow: hidden;
    }

    .table-btmLeft {
        overflow: hidden;
        padding-right: 10px;
        padding-top: 5px;
    }
    .table-btmRight {
        float: right;
    }
</style>
<template>
    <div id="tableList" class="font12">
        <!--表格公用组件模板-->
        <div v-if="bool">
            <div class="table-title" v-if="title">
                <Button class="table-btmLeft" v-if="showNew" @click="newObj" type="primary" icon="ios-search">新建</Button>
            </div>
            <Table highlight-row stripe size="small"
                   :columns="columns" :data="dataTable.list"
                   @on-row-click="rowClick">
            </Table>
            <div class="table-bottom" v-if="!pageHide">
                <div class="table-btmRight">
                    <Page :total="dataTable.page.totalCount" show-elevator show-total
                          @on-change="goPage" size="small"
                          :page-size="dataTable.page.pageSize"
                          :current="dataTable.page.curPage"
                    ></Page>
                </div>
            </div>
        </div>
        <div class="center" v-else>查询不到任何相关数据</div>
    </div>
</template>
<script>
    export default {
        /*@
        * param columnsList 表格标题字段
        * param dataTable 表格数据
        * param columnsProp 通过条件判断、判断表格配置项
        * param extendColumns 通过新增表格配置项
        * */
        props: {
            'columnsList': {
                type: [Array],
            },
            'dataTable': {
                type: [Object],
            },
            'columnsProp': {
                type: [String, Object],
            },
            'extendColumns': {
                type: [String, Object],
            },
            'extendWidth': {
                type: [Array, Object],
            },
            'showDelete': {
                type: [String, Boolean],
                default: false
            },
            'showNew': {
                type: [String, Boolean],
                default: false
            },
            'showEdit': {
                type: [String, Boolean],
                default: false
            },
            'title': {
                type: String,
            },
            'pageHide': {
                type: [String, Boolean],
                default: false
            }
        },
        data() {
            return {
                list: null,
                bool: false,
                columns: [],
            }
        },
        watch: {
            dataTable() {
                if (this.dataTable.page && this.dataTable.list) this.formatData();
            }
        },
        methods: {
            /*列表格式化*/
            formatData() {
                let arr = [];
                this.columnsList.forEach((item, index) => {
                    let obj = {
                        align: item.align ? item.align : "center",
                        ellipsis: item.ellipsis ? item.ellipsis : true,
                        render: (h, params) => {
                            return h('span', {
                                attrs: {
                                    title: params.row[item.key]
                                }
                            }, params.row[item.key])
                        }
                    };
                    Object.assign(item, obj);
                    arr.push(item);
                });
                if(this.showEdit){
                    arr.push({
                        title: 'Action',
                        key: 'action',
                        width: 150,
                        align: 'center',
                        render: (h, params) => {
                            return h('div', [
                                h('Button', {
                                    props: {
                                        type: 'primary',
                                        size: 'small'
                                    },
                                    style: {
                                        marginRight: '5px'
                                    },
                                    on: {
                                        click: () => {
                                            this.editObj(params.row.id);
                                        },
                                    },
                                }, '编辑'),
                                h('Poptip', {
                                    props: {
                                        confirm:true,
                                        width:'150',
                                        title: '确认删除此条记录'
                                    },
                                    style: {
                                        marginLeft: '5px'
                                    },
                                    on: {
                                        'on-ok':()=>{
                                            this.deleteObj(params.row.id)
                                        }
                                    }
                                }, [
                                    h('Button', {
                                        props: {
                                            type: 'error',
                                            size: 'small'
                                        }
                                    }, '删除')
                                ])
                            ]);
                        }
                    });
                }
                this.columns = arr;
                this.bool = true;
            },
            /*新建信息*/
            newObj() {
                this.$emit('newObj');
            },
            /*编辑信息*/
            editObj(index) {
                this.$emit('editObj', index);
            },
            /*删除信息*/
            deleteObj(index) {
                console.log(index);
                this.$emit('deleteObj', index);
            },
            /*点击页码更换数据*/
            goPage(val) {
                this.$emit('getPageData', val);
            },
            /*单击*/
            rowClick(val) {
                this.$emit('singleClick', val);
            },
        }
    }
</script>
