<style lang="less">

</style>
<template>
    <new-table :columnsList="columnsList" :dataTable="dataTable" :title="title"
               :showNew="showNew" :showEdit="showEdit" :showDelete="showDelete" :showDownload="showDownload"
               @getPageData="getPageData" @newObj="newObj" @editObj="editObj" @deleteObj="deleteObj">
    </new-table>
</template>
<script>
    import newTable from '../../components/zzui-table.vue';

    export default {
        data() {
            return {
                title: '用户列表',
                showNew: true,
                showEdit: true,
                showDelete: true,
                showDownload: true,
                dataTable: {},
                columnsList: [
                    {type: 'selection', width: 80, align: 'center', key: 'id'},
                    {title: '用户名称', key: 'username', sortable: true},
                    {title: '手机', key: 'phone', sortable: true},
                    {title: '邮箱', key: 'email', sortable: true},
                    {title: '角色', key: 'role', sortable: true},
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
                    action: 'user_list'
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
                this.$router.push({name: 'userEdit', params: {id: 0}});
            },
            /*编辑对象 */
            editObj(id) {
                this.$router.push({name: 'userEdit', params: {id: id}});
            },
            /*删除对象 */
            deleteObj(ids) {
                let data = {
                    action: 'user_delete',
                    ids: ids
                }
                this.$axios.apipost(data, (response) => {
                    this.initAjax();
                }, (err) => {
                    console.log(err);
                })
            }
        },
        components: {
            newTable
        }
    };
</script>