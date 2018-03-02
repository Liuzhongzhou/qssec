<style lang="less">

</style>
<template>
    <Tree :data="organization" ></Tree>
</template>
<script>
    export default {
        data () {

        },
        mounted() {
            this.initAjax()
        },
        methods: {
            initAjax() {
                let data = {
                    action: 'organization_list',
                    name : ''
                }
                this.$axios.apipost(data, (response) => {
                    //console.log(response.data.namelist);
                    let a=this.toTreeData(response.data.namelist);
                    console.log(a);
                    //this.children = response.data.data.namelist;
                }, (err) => {
                    console.log(err);
                })
            },
            toTreeData(data) {
    let resData = data;
    let tree = [];

    for (let i = 0; i < resData.length; i++) {
        if (resData[i].pid === 0) {
            let obj = {
                id: resData[i].id,
                text: resData[i].name,
                children: []
            };
            tree.push(obj);
            resData.splice(i, 1);
            i--;
        }
    }
    run(tree);

    function run(chiArr) {
        if (resData.length !== 0) {
            for (let i = 0; i < chiArr.length; i++) {
                for (let j = 0; j < resData.length; j++) {
                    if (chiArr[i].id === resData[j].pid) {

                        let obj = {
                            id: resData[j].id,
                            text: resData[j].name,
                            children: []
                        };
                        chiArr[i].children.push(obj);
                        resData.splice(j, 1);
                        j--;
                    }
                }
                // console.log(chiArr[i].children);
                run(chiArr[i].children);
            }
        }
    }
    return tree;
}
        }
    }
</script>