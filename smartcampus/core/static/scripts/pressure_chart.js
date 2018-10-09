var dom = document.getElementById("pres_chart");
var myChart = echarts.init(dom);
option = null;
option = {
    title: {
        text: 'Pressure in a week',
        subtext: 'in hPA'
    },
    tooltip: {
        trigger: 'axis'
    },
    xAxis:  {
        type: 'category',
        boundaryGap: false,
        data: ['10/1','10/2','10/3','10/4','10/5','10/6','10/7']  // This is the tag of X-axis
    },
    yAxis: {
        type: 'value',
        min: 1016,  // This is the min value of Y-axis
        max: 1021,  // This is the max value of Y-axis
    },
    series: [
        {
            name:'hPA',
            type:'line',
            data:[1019.22, 1018.76, 1017.66, 1020.01, 1019.65, 1018.99, 1018.53],  // This is the value of X-axis
            markPoint: {
                data: [
                    {type: 'max', name: 'Max'},
                    {type: 'min', name: 'Min'}
                ]
            },
            markLine: {
                data: [
                    {type: 'average', name: 'average'}
                ]
            }
        },
    ]
};
;
if (option && typeof option === "object") {
    myChart.setOption(option, true);
}
window.onresize = myChart.resize;