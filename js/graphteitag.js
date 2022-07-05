google.charts.load('current', {
    packages: ['corechart', 'line']
});
google.charts.setOnLoadCallback(drawLineColors);

function drawLineColors() {
    var data = new google.visualization.DataTable();
    data.addColumn('number', 'Chapter');
    data.addColumn('number', 'placeName');
    data.addColumn('number', 'persName');

    data.addRows([
        [1, 20, 15],
        [2, 27, 8],
        [3, 13, 28],
        [4, 25, 18],
        [5, 13, 21],
        [6, 17, 25],
        [7, 21, 49],
        [8, 26, 40],
        [9, 16, 68],
        [10, 14, 25],
        [11, 4, 53],
        [12, 6, 22],
        [13, 26, 35],
        [14, 14, 25],
        [15, 6, 17],
        [16, 5, 8],
        [17, 15, 18],
        [18, 7, 26]
    ]);

    var options = {
        hAxis: {
            title: 'Chapter'
        },
        vAxis: {
            title: 'Frequency'
        },
        colors: ['#b87333', '#CFA240']
    };

    var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
    chart.draw(data, options);
}