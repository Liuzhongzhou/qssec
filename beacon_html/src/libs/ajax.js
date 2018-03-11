import axios from 'axios';
import config from '../../build/config';

let ajax = {}, baseURL = config.apiUrl + 'api/';
ajax.install = ((Vue, options) => {

    function detailError(error, err) {
        if (typeof error === 'function') {
            error(err);
        } else {
            console.log(err);
        }
    }

    Vue.prototype.$axios = {
        get: (url, success, error) => {
            return axios.get(baseURL + url).then((res) => {
                if (res.data && res.data.return_code == 1) {
                    success(res);
                } else {
                    detailError(error, res.data.message);
                }
            }).catch((err) => {
                detailError(error);
            })
        },
        post: (url, data, success, error) => {
            return axios.post(baseURL + url, data).then((res) => {
                if (res.data && res.data.return_code == 1) {
                    success(res.data);
                } else if(res.data.return_code == '0'){
                    this.$router.push({'name':'login'})
                } else {
                    detailError(error, res.data.message);
                }
            }).catch((err) => {
                detailError(error);
            })
        },
        apipost: (data, success, error) => {
            return axios.post(baseURL, data).then((res) => {
                if (res.data && res.data.return_code == 1) {
                    success(res.data);
                } else if(res.data.return_code == '0'){
                    this.$router.push({'name':'login'})
                } else {
                    detailError(error, res.data.message);
                }
            }).catch((err) => {
                detailError(error);
            })
        }
    }
});

export default ajax;