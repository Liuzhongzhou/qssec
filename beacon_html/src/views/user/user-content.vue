<style lang="less">

</style>
<template>
    <new-table :columnsList="columnsList" :dataTable="dataTable" :title="title"
               :showNew="showNew" :showEdit="showEdit" :showDelete="showDelete"
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
                dataTable: {},
                columnsList: [
                    {title: '用户名称', key: 'username', sortable: true},
                    {title: '姓名', key: 'chineseName', sortable: true},
                    {title: '地址信息', key: 'addr', sortable: true},
                    {title: '性别', key: 'sex', sortable: true},
                    {title: '电话', key: 'telephone', sortable: true},
                    {title: '手机', key: 'phone', sortable: true},
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
                };
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