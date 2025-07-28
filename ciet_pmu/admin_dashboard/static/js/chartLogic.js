document.addEventListener("DOMContentLoaded", function () {
  const chartElement = document.getElementById("myChart");

  const labels = JSON.parse(chartElement.dataset.labels.replace(/'/g, '"'));
  const data = JSON.parse(chartElement.dataset.values.replace(/'/g, '"'));

  const ctx = chartElement.getContext("2d");

  new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Yearly Budget",
          data: data,
          backgroundColor: [
            "rgba(75, 192, 192, 0.6)",
            "rgba(255, 205, 86, 0.6)",
            "rgba(255, 99, 132, 0.6)",
            "rgba(54, 162, 235, 0.6)",
          ],
          borderColor: [
            "rgba(75, 192, 192, 1)",
            "rgba(255, 205, 86, 1)",
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
});


