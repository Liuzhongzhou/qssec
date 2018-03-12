<style lang="less">

</style>
<template>
    <div>
         <div>
             <Tree :data="organization" :render="renderContent"></Tree>
         </div>
        <div>
           <Modal v-model="modal1" :title="title" @on-ok="ok()" @on-cancel="cancel()">
                <span  v-show="add" class="W80 displayIB">组织机构名称</span>
                <Input v-show="add" v-model="form.name" placeholder="Enter something..." clearable class="W240"></Input>
                <Cascader v-show="add" :data="city" @on-change="change" clearable class="W240"></Cascader>
                <Input v-show="false" v-model="form.pid"></Input>
                <Input v-show="false" v-model="form.id"></Input>
               <span  v-show="del" class="W80 displayIB">确定删除么？</span>
           </Modal>
        </div>
    </div>

</template>
<script>
    export default {
        data () {
            return {
                organization: [
                    {
                        title: '组织机构',
                        id:0,
                        expand: true,
                        render: (h, { root, node, data }) => {
                            return h('span', {
                                style: {
                                    display: 'inline-block',
                                    width: '100%'
                                }
                            }, [
                                h('span', [
                                    h('Icon', {
                                        props: {
                                            type: 'ios-folder-outline'
                                        },
                                        style: {
                                            marginRight: '8px'
                                        }
                                    }),
                                    h('span', data.title)
                                ]),
                                h('span', {
                                    style: {
                                        display: 'inline-block',
                                        float: 'right',
                                        marginRight: '32px'
                                    }
                                }, [
                                    h('Button', {
                                        props: Object.assign({}, this.buttonProps, {
                                            icon: 'ios-plus-empty',
                                            type: 'primary'
                                        }),
                                        style: {
                                            width: '52px'
                                        },
                                        on: {
                                            click: () => {
                                               this.form.pid = this.organization[0].id;
                                               this.modal1=true;
                                               this.title = '添加组织机构';
                                               this.add = true;
                                               this.del = false;
                                               this.cityData();
                                            }
                                        }
                                    })
                                ])
                            ]);
                        },
                         children: [
                        ]
                    }
                ],
                buttonProps: {
                    type: 'ghost',
                    size: 'small',
                },
                modal1: false,
                title:'',
                add:false,
                del:false,
                form: {
                    name: '',
                    pid:'',
                    id:'',
                    citycode:''
                },
                city: []
            }
        },
        mounted() {
            this.initAjax();
        },
        methods: {
            renderContent (h, { root, node, data }) {
                return h('span', {
                    style: {
                        display: 'inline-block',
                        width: '100%'
                    }
                }, [
                    h('span', [
                        h('Icon', {
                            props: {
                                type: 'ios-paper-outline'
                            },
                            style: {
                                marginRight: '8px'
                            }
                        }),
                        h('span', data.title)
                    ]),
                    h('span', {
                        style: {
                            display: 'inline-block',
                            float: 'right',
                            marginRight: '32px'
                        }
                    }, [
                        h('Button', {
                            props: Object.assign({}, this.buttonProps, {
                                icon: 'ios-plus-empty'
                            }),
                            style: {
                                marginRight: '8px'
                            },
                            on: {
                                click: () => {
                                this.form.pid =data.id;
                                this.modal1=true;
                                this.title = '添加组织机构';
                                this.add = true;
                                this.del = false;
                                this.cityData();
                                }
                            }
                        }),
                        h('Button', {
                            props: Object.assign({}, this.buttonProps, {
                                icon: 'ios-minus-empty'
                            }),
                            on: {
                                click: () => {
                                    this.form.id = data.id;
                                    this.modal1=true;
                                    this.title = '删除组织机构';
                                    this.del = true;
                                    this.add = false;
                                }
                            }
                        })
                    ])
                ]);
            },
            initAjax() {
                let data = {
                    action: 'organization_list',
                    name : '',
                    city : ''
                };
                this.$axios.apipost(data, (response) => {
                                         console.log(response.data.namelist);

                    let data = response.data.namelist;
                    // 属性配置信息
                    let attributes = {
                        id: 'id',
                        parentId: 'pid',
                        name: 'name',
                        rootId: 0
                    };
                    let treeData = toTreeData(data, attributes);
                    this.organization[0].children = treeData;
                }, (err) => {
                    console.log(err);
                })
            },
            ok () {
                if(this.add){
                   let data = {
                      action: 'organization_save',
                      name : this.form.name,
                      pid : this.form.pid,
                      citycode: this.form.citycode
                   };
                   this.$axios.apipost(data, (response) => {
                       this.$Message.success('保存成功!');
                       this.initAjax();
                   }, (err) => {
                     console.log(err);
                   });
                } else {
                    let data = {
                        action: 'organization_delete',
                        id : this.form.id
                    };
                    this.$axios.apipost(data, (response) => {
                    this.$Message.success('删除成功!');
                    this.initAjax();
                }, (err) => {
                    console.log(err);
                });
                }

            },
            cancel () {
            },
            cityData(){
                let data = {
                    action: 'city_list'
                };
                this.$axios.apipost(data, (response) => {
                    let data = response.data.citylist;
                    // 属性配置信息
                    let attributes = {
                        id: 'value',
                        parentId: 'pcode',
                        name: 'label',
                        rootId: '990001'
                    };
                    let treeData = toCityData(data, attributes);
                    this.city = treeData;
                }, (err) => {
                    console.log(err);
                })
            },
            change (labels, selectedData) {
                let number = selectedData.length;
                this.form.citycode = selectedData[--number].value;
            }
        }
    }

 function toTreeData (data, attributes) {
  let resData = data;
  let tree = [];

  for (let i = 0; i < resData.length; i++) {
    if (resData[i][attributes.parentId] === attributes.rootId) {
      let obj = {
          id: resData[i][attributes.id],
          title: resData[i][attributes.name],
          expand:true,
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
          if (chiArr[i].id === resData[j][attributes.parentId]) {
            let obj = {
                id: resData[j][attributes.id],
                title: resData[j][attributes.name],
                expand:true,
                children: []
            };
            chiArr[i].children.push(obj);
            resData.splice(j, 1);
            j--;
          }
        }
        run(chiArr[i].children);
      }
    }
  }
  return tree;
}
 function toCityData (data, attributes) {
  let resData = data;
  let tree = [];

  for (let i = 0; i < resData.length; i++) {
    if (resData[i][attributes.parentId] === attributes.rootId) {
      let obj = {
        value: resData[i][attributes.id],
        label: resData[i][attributes.name],
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
          if (chiArr[i].value === resData[j][attributes.parentId]) {
            let obj = {
              value: resData[j][attributes.id],
              label: resData[j][attributes.name],
              children: []
            };
            chiArr[i].children.push(obj);
            resData.splice(j, 1);
            j--;
          }
        }
        run(chiArr[i].children);
      }
    }
  }
  return tree;
}
</script>
