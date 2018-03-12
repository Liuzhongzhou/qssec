import Env from './env';

let config = {
    env: Env,
    apiUrl:Env === 'development' ? 'http://localhost:10086/':'http://192.168.12.80:10086',
};
export default config;