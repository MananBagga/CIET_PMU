document.addEventListener("DOMContentLoaded", function () {
  // === Function to create a chart ===
  function createBarChart(elementId, chartLabel) {
    const chartElement = document.getElementById(elementId);
    if (!chartElement) return;

    const labels = JSON.parse(chartElement.dataset.labels);
    const data = JSON.parse(chartElement.dataset.values);
    const ctx = chartElement.getContext("2d");

    new Chart(ctx, {
      type: "bar",
      data: {
        labels: labels,
        datasets: [
          {
            label: chartLabel,
            data: data,
            backgroundColor: [
              "rgba(75, 192, 192, 0.6)",
              "rgba(255, 205, 86, 0.6)",
              "rgba(255, 99, 132, 0.6)",
              "rgba(54, 162, 235, 0.6)",
              "rgba(153, 102, 255, 0.6)",
              "rgba(255, 159, 64, 0.6)",
            ],
            borderColor: [
              "rgba(75, 192, 192, 1)",
              "rgba(255, 205, 86, 1)",
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
            ],
            borderWidth: 1,
            // ✅ Make bars thinner only for myChart
            ...(elementId === "myChart" && { barPercentage: 0.4, categoryPercentage: 0.6 })
          },
        ],
      },
      options: {
        responsive: true,
        plugins: {
          legend: { display: true },
          tooltip: { enabled: true },
        },
        scales: {
          y: { beginAtZero: true },
        },
      },
    });
  }

  // === Initialize both charts ===
  createBarChart("myChart", "Yearly Budget");
  createBarChart("monthChart", "Month-wise Budget");
});


