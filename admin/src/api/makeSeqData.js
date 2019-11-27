function makeEmpty(start,end,data){
    let result=[];
    //不包含start
    start.setMonth(start.getMonth()+1);
    while(start<end){
        let yearstr=start.getFullYear().toString();
        let monthstr=(start.getMonth()+1).toString();
        //前面补0
        monthstr=monthstr.length==1 ? "0"+monthstr:monthstr;
        result.push({"日期":yearstr+"-"+monthstr,"标准值":data["标准值"],"实际值":data["实际值"]})
        start.setMonth(start.getMonth()+1);
    }
    return result;
}

export default function makeSeqData(datalist){
    if(datalist.length==0 || datalist[0]["日期"]==undefined){
        return datalist;
    }
    let result=[];
    for(let i=0;i<datalist.length;i++){
        let real=datalist[i];
        if(i==0){
            result.push(real);
        }else if(i==datalist.length-1){
            //做前插
            let startdate=new Date(datalist[i-1]["日期"]);
            let enddate=new Date(datalist[i]["日期"]);
            let emptydata=makeEmpty(startdate,enddate,datalist[i-1]);
            result=result.concat(emptydata);
            //插自己
            result.push(datalist[i]);
            //做后插
            startdate=new Date(datalist[i]["日期"]);
            enddate=new Date(new Date());
            emptydata=makeEmpty(startdate,enddate,datalist[i]);
            result=result.concat(emptydata);
        }else{
            let startdate=new Date(datalist[i-1]["日期"]);
            let enddate=new Date(datalist[i]["日期"]);
            let emptydata=makeEmpty(startdate,enddate,datalist[i-1]);
            result=result.concat(emptydata);
            result.push(datalist[i]);
        }
    }
    return result;
}

// test=[
//     {"日期":"2018-06","标准值":90,"实际值":65},
//     {"日期":"2018-12","标准值":90,"实际值":78},
//     {"日期":"2019-05","标准值":100,"实际值":98},
//     {"日期":"2019-08","标准值":100,"实际值":102}
// ]

// console.table(makeSeqData(test));

