<style lang="less">

</style>
<template>
    <new-table :columnsList="columnsList" :dataTable="dataTable" :title="title"
               :showNew="showNew" :showEdit="showEdit" :showDelete="showDelete" :showDownload="showDownload"
               @getPageData="getPageData" @newObj="newObj" @editObj="editObj" >
    </new-table>
</template>
<script>
    import newTable from '../../components/appsys-table';

    export default {
        data() {
            return {
                title: '应用系统列表',
                showNew: true,
                showEdit: true,
                showDelete: true,
                showDownload: true,
                dataTable: {},
                columnsList: [
                    {title: '应用系统名称', key: 'app_name', sortable: true},
                    {title: 'ip地址', key: 'app_ip', sortable: true},
                    {title: '端口', key: 'app_port', sortable: true},
                    {title: '所属地市', key: 'city_code', sortable: true},
                    {title: '添加日期', key: 'add_time', sortable: true},
                ]
            };
        },
        props: {
            form: {},
        },
        mounted() {
            this.initAjax();
            this.dataTable = {};
        },
        methods: {
            initAjax() {
                let data = {
                    action: 'appsys_list'
                }
                if (this.form) {
                    Object.assign(data, this.form);
                }
                this.$axios.apipost(data, (response) => {
                    this.dataTable = response.data.data;
                }, (err) => {
                    console.log(err);
                })
            },
            getPageData(index) {
                this.form.curPage = index;
                this.initAjax();
            },
            /*新建对象 */
            newObj() {
                this.$router.push({name: 'appsysEdit', params: {app_code: 0}});
            },
            /*编辑对象 */
            editObj(app_code) {
                this.$router.push({name: 'appsysEdit', params: {app_code: app_code}});
            },
            /*删除对象
            deleteObj(ids) {
                let data = {
                    action: 'role_delete',
                    ids: ids
                }
                this.$axios.apipost(data, (response) => {
                    this.initAjax();
                }, (err) => {
                    console.log(err);
                })
            } */
        },
        components: {
            newTable
        }
    };
</script>