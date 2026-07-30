document.addEventListener("DOMContentLoaded", function () {

    // -----------------------------
    // Severity Chart
    // -----------------------------

    const severityCanvas = document.getElementById("incidentChart");

    if (severityCanvas) {

        const labels = JSON.parse(
            severityCanvas.dataset.labels
        );

        const values = JSON.parse(
            severityCanvas.dataset.values
        );

        new Chart(severityCanvas, {

            type: "bar",

            data: {

                labels: labels,

                datasets: [

                    {

                        label: "Incidents",

                        data: values,

                        borderWidth: 1

                    }

                ]

            }

        });

    }

    // -----------------------------
    // Attack Distribution
    // -----------------------------

    const attackCanvas = document.getElementById("attackChart");

    if (attackCanvas) {

        const labels = JSON.parse(
            attackCanvas.dataset.labels
        );

        const values = JSON.parse(
            attackCanvas.dataset.values
        );

        new Chart(attackCanvas, {

            type: "pie",

            data: {

                labels: labels,

                datasets: [

                    {

                        data: values

                    }

                ]

            }

        });

    }

});