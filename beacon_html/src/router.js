import Index from './views/index.vue';

const menuConfig = [
    {
        path: '/',
        name: 'index',
        redirect: '/home/sure',
        meta: {
            icon: 'ios-navigate',
            title: '我的任务',
            level: '1',
            num: '1'
        },
        component: Index,
        children: [{
            path: '/home/sure',
            name: 'sure',
            meta: {
                icon: 'ios-navigate',
                title: '确凿事件',
                level: '1',
                num: '1-1',
                pid: 'index',
            },
            component: (resolve) => require(['./views/home.vue'], resolve),
        },{
            path: '/home/really',
            name: 'really',
            meta: {
                icon: 'ios-navigate',
                title: '疑似/风险事件',
                level: '1',
                num: '1-2',
                pid: 'index',
            },
            component: (resolve) => require(['./views/home.vue'], resolve),
        },{
            path: '/home/report',
            name: 'report',
            meta: {
                icon: 'ios-navigate',
                title: '上报事件',
                level: '1',
                num: '1-3',
                pid: 'index',
            },
            component: (resolve) => require(['./views/home.vue'], resolve),
        }]
        },
    {
        path: '/system',
        name: 'system',
        meta: {
            icon: 'settings',
            title: '系统配置',
            level: '1',
            num: '2'
        },
        redirect: '/system/user',
        component: Index,
        children: [
            {
                path: '/system/user',
                name: 'userlist',
                meta: {
                    icon: 'ios-navigate',
                    title: '用户',
                    level: '1',
                    pid: 'system',
                    num: '2-1'
                },
                component: (resolve) => require(['./views/user/user.vue'], resolve),
            },
            {
                path: '/system/user/edit',
                name: 'userEdit',
                meta: {
                    icon: 'ios-navigate',
                    title: '编辑',
                    level: '1',
                    pid: 'userlist',
                    hide:true,
                },
                component: (resolve) => require(['./views/user/user-edit.vue'], resolve),
            },
            {
                path: '/system/role',
                name: 'rolelist',
                meta: {
                    icon: 'ios-navigate',
                    title: '角色',
                    level: '1',
                    pid: 'system',
                    num: '2-1'
                },
                component: (resolve) => require(['./views/role/role.vue'], resolve),
            },
            {
                path: '/system/role/edit',
                name: 'roleEdit',
                meta: {
                    icon: 'ios-navigate',
                    title: '编辑',
                    level: '1',
                    pid: 'rolelist',
                    hide:true,
                },
                component: (resolve) => require(['./views/role/role-edit.vue'], resolve),
            },
            {
                path: '/system/organization',
                name: 'organizationList',
                meta: {
                    icon: 'ios-navigate',
                    title: '组织机构',
                    level: '1',
                    pid: 'system',
                    num: '2-1'
                },
                component: (resolve) => require(['./views/organization/organization.vue'], resolve),
            },
             {
                path: '/system/fileUPload',
                name: 'fileUPload1',
                meta: {
                    icon: 'ios-navigate',
                    title: '文件上传',
                    level: '1',
                    pid: 'system',
                    num: '5-1'
                },
                component: (resolve) => require(['./views/file/fileUPload.vue'], resolve),
            },
            {
                path: '/system/appsys',
                name: 'appsyslist',
                meta: {
                    icon: 'ios-navigate',
                    title: '应用系统',
                    level: '1',
                    pid: 'system',
                    num: '3-1'
                },
                component: (resolve) => require(['./views/appsys/appsys.vue'], resolve),
            },
            {
                path: '/system/appsys/edit',
                name: 'appsysEdit',
                meta: {
                    icon: 'ios-navigate',
                    title: '编辑',
                    level: '1',
                    pid: 'appsyslist',
                    hide:true,
                },
                component: (resolve) => require(['./views/appsys/appsys-edit.vue'], resolve),
            },
        ]
    },
    {
        path: '/test',
        name: 'test',
        meta: {
            icon: 'settings',
            title: '接口测试页',
            level: '1',
            num: '4'
        },
        redirect: '/test/test',
        component: Index,
        children: [
            {
                path: '/test/test',
                name: 'test1',
                meta: {
                    icon: 'ios-navigate',
                    title: '接口测试页',
                    level: '1',
                    pid: 'test',
                    num: '4-1'
                },
                component: (resolve) => require(['./views/api/api.vue'], resolve),
            }
        ]
    }
];


const routers = [...menuConfig, {
    path: '/login',
    name: 'login',
    meta: {
        title: '登录页'
    },
    component: (resolve) => require(['./views/login.vue'], resolve)
}, {
    path: '/ui',
    name: 'ui',
    meta: {
        title: '组件库'
    },
    component: (resolve) => require(['./views/ui.vue'], resolve)
}, {
    path: '*',
    name: '404',
    meta: {
        title: '404'
    },
    component: (resolve) => require(['./views/404.vue'], resolve)
}];

export default routers;
export {menuConfig};