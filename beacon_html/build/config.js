import Env from './env';

let config = {
    env: Env,
    apiUrl:Env === 'development' ? 'http://localhost:8888/':'http://192.168.12.80:8888',
};
export default config;