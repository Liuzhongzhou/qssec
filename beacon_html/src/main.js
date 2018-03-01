import Vue from 'vue';
import iView from 'iView';
import VueRouter from 'vue-router';
import Routers from './router';
import echart from './libs/echart.js';
import ajax from './libs/ajax.js';
import store from './store';
import Vuex from 'vuex';
import Util from './libs/util';
import App from './app.vue';
import './assets/css/normal.css';
// import 'iview/dist/styles/iview.css';
import './assets/css/index.less';
import './assets/css/animate.css';


Vue.use(VueRouter);
Vue.use(Vuex);
Vue.use(echart);
Vue.use(ajax);
Vue.use(iView);
Vue.use(Util);

// 路由配置
const RouterConfig = {
    mode: 'history',
    routes: Routers
};
const router = new VueRouter(RouterConfig);

router.beforeEach((to, from, next) => {
    iView.LoadingBar.start();
    window.document.title = to.meta.title || '烽火令';
    if(!localStorage.getItem('user_name') && to.meta.level){
        return next({name: "login"});
    };
    next();
});

router.afterEach(() => {
    iView.LoadingBar.finish();
    window.scrollTo(0, 0);
});

new Vue({
    el: '#app',
    router: router,
    store: store,
    render: h => h(App)
});
