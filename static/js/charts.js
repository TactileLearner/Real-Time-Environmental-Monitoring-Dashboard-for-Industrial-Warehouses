
// static/js/charts.js

function createChart(ctx, label) {
    return new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: label,
                borderColor: 'rgba(75,192,192,1)',
                data: [],
            }],
        },
        options: {
            animation: false,
            responsive: true,
            scales: {
                x: { display: true },
                y: { beginAtZero: true }
            }
        }
    });
}