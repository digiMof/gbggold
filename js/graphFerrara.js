google.charts.load('current', {
    packages: ['corechart', 'line']
});
google.charts.setOnLoadCallback(drawLineColors);

function drawLineColors() {
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Chapter');
    data.addColumn('number', 'Center');
    data.addColumn('number', 'Periphery');
    data.addColumn({
        type: 'string',
        role: 'annotation'
    });
    data.addColumn({
        type: 'string',
        role: 'annotationText'
    });

    data.addRows([
        ["Chap. 1", 100, 0, null, null],
        ["Chap. 2", 100, 0, null, null],
        ["Chap. 3", 100, 0, "Outing", "At the end of the chapter, Fadigati's sexual orientation is discovered. Chapp. 8-13 are set either on the train Ferrara - Bologna or at the Adriatic Sea"],
        ["Chap. 13", 91.66666667, 8.333333333, "Back to Ferrara", "After the summer, the outing and marginalisation of the protagonist (and, in part, also of the narrator) is reflected by the description of setting"],
        ["Chap. 14", 57.14285714, 42.85714286, null, null],
        ["Chap. 15", 50, 50, null, null],
        ["Chap. 16", 42.85714286, 57.14285714, null, null],
        ["Chap. 17", 50, 50, null, null],
        ["Chap. 18", 50, 50, null, null]
    ]);

    var options = {
        responsive: true,
        hAxis: {
            title: 'Chapter'
        },
        vAxis: {
            title: 'Centre vs Periphery (in %)',
            maxValue: 75
        },
        colors: ['#000249', '#DD1717'],
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

    var chart = new google.visualization.LineChart(document.getElementById('chart_divFE'));
    chart.draw(data, options);
}

$(window).resize(function(){
    drawLineColors();
  });