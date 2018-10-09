var dom = document.getElementById("humi_chart");
var myChart = echarts.init(dom);
option = null;
option = {
    title: {
        text: 'Humidity in a week',
        subtext: 'in %'
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
        min: 48,  // This is the min value of Y-axis
        max: 52,  // This is the max value of Y-axis
    },
    series: [
        {
            name:'%',
            type:'line',
            data:[48.37, 49.41, 50.12, 48.19, 51.22, 50.13, 48.99],  // This is the value of X-axis
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