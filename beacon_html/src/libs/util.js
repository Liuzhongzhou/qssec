let util = {};

util.install = (Vue,options)=>{
    Vue.prototype.$util = {
        typeof(obj) {
            const toString = Object.prototype.toString;
            const map = {
                '[object Boolean]'  : 'boolean',
                '[object Number]'   : 'number',
                '[object String]'   : 'string',
                '[object Function]' : 'function',
                '[object Array]'    : 'array',
                '[object Date]'     : 'date',
                '[object RegExp]'   : 'regExp',
                '[object Undefined]': 'undefined',
                '[object Null]'     : 'null',
                '[object Object]'   : 'object'
            };
            return map[toString.call(obj)];
        },
        /*
        * 根据不同类型 返回相应时间*/
        getTime(type) {
            let time = new Date(),
                YY = time.getFullYear(),
                MM = time.getMonth(),
                DD = time.getDate(),
                WW = time.getDay(),
                hh = time.getHours(),
                mm = time.getMinutes(),
                ss = time.getSeconds(),
                CHWW = ['日','一','二','三','四','五','六'],
                apm = '',hhItem = '';
                if(hh > 12){
                    hhItem = hh - 12;
                    apm = '下午';
                }else{
                    hhItem = hh;
                    apm = '上午';
                }
            if(type == 'yearMonth'){
                return YY+'-'+MM+'-'+DD;
            }
            return {
                date:MM+'月'+DD+'日',
                week:'星期'+CHWW[WW],
                am:apm,
                hms:hhItem+':'+mm+':'+ss
            }
        },
    }
};


export default util;