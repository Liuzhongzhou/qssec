<style scoped>
    #tableList {
        width: 100%;
        height: 100%;
        min-height: 500px;
        position: relative;
    }

    .table-titile {
        line-height: 40px;
        height: 40px;
        overflow: hidden;
    }

    .table-title-left {
        float: left;
        color: #d1d8e3;
        margin-left: 19px;
    }

    .table-bottom {
        position: absolute;
        height: 40px;
        bottom: 0px;
        left: 0px;
        padding-right: 20px;
        width: 100%;
        overflow: hidden;
    }

    .table-btmLeft {
        float: right;
        overflow: hidden;
        padding-right: 10px;
        padding-top: 5px;
    }

    .table-down {
        width: 70px;
        height: 30px;
        border-radius: 2px;
        border: solid 1px #1b232b;
        text-align: center;
        line-height: 30px;
        color: #4686bc;
        cursor: pointer;
        float: left;
        margin-left: 10px;
    }

    .table-down:hover {
        color: #2dc0ff;
    }

    .table-down {
        font-size: 14px;
    }

    .table-down span {
        font-size: 12px;
        margin-left: 5px;
    }

    .table-btmRight {
        float: right;
    }
</style>
<template>
    <div id="tableList" class="font12">
        <!--表格公用组件模板-->
        <div v-if="bool">
            <div class="table-titile" v-if="title">
                <div class="table-title-left">{{title}}</div>
                <div class="table-btmLeft">
                    <div class="table-down" @click="newObj" v-if="showNew">
                        <Icon type="android-add"></Icon>
                        <span>新建</span>
                    </div>
                    <div class="table-down" @click="editObj" v-if="showEdit">
                        <Icon type="android-edit"></Icon>
                        <span>编辑</span>
                    </div>
                    <div class="table-down" @click="deleteObj" v-if="showDelete">
                        <Icon type="ios-trash-outline"></Icon>
                        <span>删除</span>
                    </div>
                    <div class="table-down" @click="download" v-if="showDownload">
                        <Icon type="ios-download-outline"></Icon>
                        <span>下载</span>
                    </div>
                </div>
            </div>
            <Table highlight-row stripe size="small"
                   :columns="columns" :data="dataTable.list"
                   @on-select="selectionOne"
                   @on-select-all="selectionAll"
                   @on-selection-change="selectionChange"
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
        * param showDownload 显示下载按钮
        * */
        props: {
            'columnsList': {
                type: [Array],
            },
            'dataTable': {
                type: [Object],
            },
            'checkboxColumns': {
                type: [Array, Object],
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
            'showDownload': {
                type: [String, Boolean],
                default: false
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
                ids: '',
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
                                    title: params.row[item.title]
                                }
                            }, params.row[item.key])
                        }
                    };
                    Object.assign(item, obj);
                    arr.push(item);
                });

                this.columns = arr;
                this.bool = true;
            },
            /*新建信息*/
            newObj() {
                this.$emit('newObj');
            },
            /*编辑信息*/
            editObj() {
                if (!this.ids) {
                    this.$Message.warning('请选择一条记录修改!');
                } else {
                    let id = this.ids.split(',');
                    if (id.length != 1) {
                        this.$Message.warning('请最多选择一条记录修改!');
                    } else {
                        this.$emit('editObj', this.ids);
                    }
                }
            },
            /*删除信息*/
            deleteObj() {
                if (!this.ids) {
                    this.$Message.warning('请至少选择一条记录删除!');
                } else {
                    this.$Modal.confirm({
                        title: '警告',
                        content: '确定删除吗?',
                        onOk: () => {
                            this.$emit('deleteObj', this.ids);
                        }
                    });
                }
            },
            /*下载*/
            download() {
                this.$emit('downloadExcel');
            },
            /*点击页码更换数据*/
            goPage(val) {
                this.$emit('getPageData', val);
            },
            selectionOne(val) {
                //this.getSelectionIds(val);
            },
            selectionAll(val) {
                //this.getSelectionIds(val);
            },
            selectionChange(val) {
                this.ids = this.getSelectionIds(val);
            },
            /*单击*/
            rowClick(val) {
                this.$emit('singleClick', val);
            },
            /* 获取被选中列表主键 */
            getSelectionIds(val) {
                let key = '', ids = '';
                this.columns.forEach((item, index) => {
                    if (item.type == 'selection') {
                        key = item.key;
                        return false;
                    }
                });
                if (key) {
                    val.forEach((item, index) => {
                        ids += ((index == 0 ? '' : ',') + item[key])
                    });
                }
                return ids;
            }
        }
    }
</script>
