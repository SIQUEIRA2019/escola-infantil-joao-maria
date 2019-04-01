
Highcharts.chart('container', {
    chart: {
      plotBackgroundColo:null,
      plotBorderWidth: null,
      plotShadow: false,
      type: 'pie'
    },
    title: {
      text: 'Consumidores'
    },
    tooltip: {
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    plotOptions: {
      pie: {
        allowPointSelect: true,
        cursor: 'pointer',
        dataLabels: {
          enabled: true,
          format: '<b>{point.name}</b>: {point.percentage:.1f} %',
          style: {
            color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
          }
        }
      }
    },
    series: [{
      name: 'Brands',
      colorByPoint: true,
      data: [{
        name: 'Patrícia',
        y: 61.41,
        sliced: true,
        selected: true
      }, {
        name: 'Agatha ',
        y: 11.84
      }, {
        name: 'Sara',
        y: 10.85
      }, {
        name: 'Arthur',
        y: 4.67
      }, {
        name: 'Carlos',
        y: 4.18
      }, {
        name: 'Kaio',
        y: 1.64
      }, {
        name: 'Luciana',
        y: 1.6
      }, {
        name: 'Sabe Deus',
        y: 1.2
      }, {
        name: 'Os demais',
        y: 2.61
      }]
    }]
  });