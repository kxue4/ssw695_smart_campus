var dom = document.getElementById("temp_chart");
var myChart = echarts.init(dom);
option = null;
option = {
    title: {
        text: 'Temperature in a week',
        subtext: 'in °F'
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
        min: 70,  // This is the min value of Y-axis
        max: 80,  // This is the max value of Y-axis
    },
    series: [
        {
            name:'°F',
            type:'line',
            data:[73.6, 71.4, 70.3, 74.2, 78.1, 73.3, 72.5],  // This is the value of X-axis
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