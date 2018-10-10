var dom = document.getElementById("air_chart");
var myChart = echarts.init(dom);
option = null;
option = {
    title: {
        text: 'Air Quality in a week',
        subtext: 'in a million'
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
        min: 12.5,  // This is the min value of Y-axis
        max: 13.5,  // This is the max value of Y-axis
    },
    series: [
        {
            name:'in a million',
            type:'line',
            data:[12.91, 12.91, 12.91, 12.91, 12.91, 12.91, 12.91],  // This is the value of X-axis
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