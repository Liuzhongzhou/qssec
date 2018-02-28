import Vue from 'vue';
import Vuex from 'vuex';

import app from './modules/app';
import user from './modules/user';

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        historyRouter:''
    },
    mutations: {
        rePlace(param){
           state.historyRouter = param
        }
    },
    actions: {

    },
    modules: {
        app,
        user
    }
});

export default store;
