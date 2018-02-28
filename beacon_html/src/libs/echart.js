import echart from 'echarts';

let chart = {};

chart.install = (Vue,options)=>{
    Vue.prototype.$echart = (obj)=>{
        /*传递参数返回实例对象、返回echart对象*/
        if (typeof obj === 'object'){
            let el = obj.el || '',
                opt = obj.options;
            let myChart = echart.init(document.getElementById(el));// 绘制图表
            myChart.setOption(opt);
            return myChart;
        }else{
            return echart;
        }
    }
};

export default chart;