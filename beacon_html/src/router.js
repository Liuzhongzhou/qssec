import Index from './views/index.vue';

const menuConfig = [
    {
        path: '/',
        name: 'index',
        redirect: '/home',
        meta: {
            icon: 'ios-navigate',
            title: '首页',
            level: '1',
            num: '1'
        },
        component: Index,
        children: [{
            path: '/home',
            name: 'home',
            meta: {
                icon: 'ios-navigate',
                title: '首页',
                level: '1',
                num: '1'
            },
            component: (resolve) => require(['./views/home.vue'], resolve),
        },
            {
                path: '/home/user',
                name: 'usr',
                meta: {
                    icon: 'ios-navigate',
                    title: '个人资料',
                    level: '1',
                    pid: 'home',
                    num: '1-1'
                },
                component: (resolve) => require(['./views/home.vue'], resolve),
            },
            {
                path: '/login',
                name: 'exit',
                meta: {
                    icon: 'ios-navigate',
                    title: '退出',
                    level: '1',
                    pid: 'home',
            }
        },]
    },
    {
        path: '/user',
        name: 'user',
        meta: {
            icon: 'settings',
            title: '用户页',
            level: '1',
            num: '2'
        },
        redirect: '/user/user',
        component: Index,
        children: [
            {
                path: '/user/user',
                name: 'userlist',
                meta: {
                    icon: 'ios-navigate',
                    title: '用户',
                    level: '1',
                    pid: 'user',
                    num: '2-1'
                },
                component: (resolve) => require(['./views/user/user.vue'], resolve),
            },
            {
                path: '/user/edit',
                name: 'userEdit',
                meta: {
                    icon: 'ios-navigate',
                    title: '编辑',
                    level: '1',
                    pid: 'user'
                },
                component: (resolve) => require(['./views/user/user-edit.vue'], resolve),
            }
        ]
    },
    {
        path: '/role',
        name: 'role',
        meta: {
            icon: 'settings',
            title: '角色页',
            level: '1',
            num: '2'
        },
        redirect: '/role/role',
        component: Index,
        children: [
            {
                path: '/role/role',
                name: 'rolelist',
                meta: {
                    icon: 'ios-navigate',
                    title: '角色',
                    level: '1',
                    pid: 'role',
                    num: '2-1'
                },
                component: (resolve) => require(['./views/role/role.vue'], resolve),
            },
            {
                path: '/role/edit',
                name: 'roleEdit',
                meta: {
                    icon: 'ios-navigate',
                    title: '编辑',
                    level: '1',
                    pid: 'role'
                },
                component: (resolve) => require(['./views/role/role-edit.vue'], resolve),
            }
        ]
    },
    {
    path: '/organization',
    name: 'organization',
    meta: {
        icon: 'settings',
        title: '组织机构',
        level: '1',
        num: '2'
    },
    redirect: '/organization/organization',
    component: Index,
    children: [
        {
            path: '/organization/organization',
            name: 'organizationList',
            meta: {
                icon: 'ios-navigate',
                title: '组织机构',
                level: '1',
                pid: 'organization',
                num: '2-1'
            },
            component: (resolve) => require(['./views/organization/organization.vue'], resolve),
        },
        {
            path: '/organization/edit',
            name: 'organizationEdit',
            meta: {
                icon: 'ios-navigate',
                title: '编辑',
                level: '1',
                pid: 'organization'
            },
            component: (resolve) => require(['./views/organization/organization-edit.vue'], resolve),
        }
     ]
    },
    {
        path: '/test',
        name: 'test',
        meta: {
            icon: 'settings',
            title: '接口测试页',
            level: '1',
            num: '2'
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
                    num: '2-1'
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