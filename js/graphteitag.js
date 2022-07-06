google.charts.load('current', {
    packages: ['corechart', 'line']
});
google.charts.setOnLoadCallback(drawLineColors);

function drawLineColors() {
    var data = new google.visualization.DataTable();
    data.addColumn('number', 'Chapter');
    data.addColumn('number', 'placeName');
    data.addColumn('number', 'persName');
    data.addColumn({
        type: 'string',
        role: 'annotation'
    });
    data.addColumn({
        type: 'string',
        role: 'annotationText'
    });

    data.addRows([
        [1, 20, 15, "Ferrara", "Ferrara, the main setting"],
        [2, 27, 8, null, null],
        [3, 13, 28, null, null],
        [4, 25, 18, "Bologna", "Commute and university life in Bologna"],
        [5, 13, 21, null, null],
        [6, 17, 25, null, null],
        [7, 21, 49, null, null],
        [8, 26, 40, "Riccione", "Riccione and the summer at the Adriatic Sea"],
        [9, 16, 68, null, null],
        [10, 14, 25, null, null],
        [11, 4, 53, null, null],
        [12, 6, 22, null, null],
        [13, 26, 35, "Ferrara", "Ferrara, back to an endangered routine"],
        [14, 14, 25, null, null],
        [15, 6, 17, null, null],
        [16, 7, 8, null, null],
        [17, 15, 18, null, null],
        [18, 7, 26, null, null]
    ]);

    var options = {
        height: 400,
        hAxis: {
            title: 'Chapter'
        },
        vAxis: {
            title: 'Frequency',
            maxValue: 75
        },
        colors: ['#b87333', '#CFA240'],
        annotations: {
            alwaysOutside: true,
            style: 'line',
            datum: {
                stem: {
                    color: 'black',
                    length: 75
                }
            },
            textStyle: {
                color: 'black'
            }
        }
    };

    var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
    chart.draw(data, options);
}