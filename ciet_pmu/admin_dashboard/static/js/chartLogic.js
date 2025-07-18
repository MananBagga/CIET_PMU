const ctx = document.getElementById("barChart");

const labels = JSON.parse(ctx.dataset.labels);
const chartData = JSON.parse(ctx.dataset.values);

const data = {
  labels: labels,
  datasets: [
    {
      label: "Monthly Data",
      data: chartData,
      backgroundColor: "rgba(54, 162, 235, 0.5)",
      borderColor: "rgba(54, 162, 235, 1)",
      borderWidth: 1,
    },
  ],
};

const config = {
  type: "bar",
  data: data,
  options: {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
};

new Chart(ctx, config);

function showSection(sectionId) {
  const sections = document.getElementsByClassName("section");
  for (let section of sections) {
    section.classList.remove("active");
  }
  document.getElementById(sectionId).classList.add("active");
}
