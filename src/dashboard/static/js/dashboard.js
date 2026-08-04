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

// -----------------------------
// Live Clock
// -----------------------------

function updateClock() {

    const now = new Date();

    document.getElementById("currentTime").innerHTML =
        now.toLocaleTimeString();

    document.getElementById("currentDate").innerHTML =
        now.toDateString();

}

updateClock();

setInterval(updateClock, 1000);

// ======================================
// Animated Counters
// ======================================

const counters = document.querySelectorAll(".counter");

counters.forEach(counter => {

    const updateCounter = () => {

        const target = Number(counter.dataset.target);

        const current = Number(counter.innerText);

        const increment = Math.ceil(target / 40);

        if (current < target) {

            counter.innerText = current + increment;

            setTimeout(updateCounter, 40);

        }

        else{

            counter.innerText = target;

        }

    };

    updateCounter();

});

// ======================================
// Run AI Pipeline (AJAX)
// ======================================

const runBtn = document.getElementById("runPipelineBtn");

if (runBtn) {

    runBtn.addEventListener("click", async function () {

        const modal = new bootstrap.Modal(
            document.getElementById("loadingModal")
        );

        modal.show();

        try {

            const response = await fetch("/run-analysis");

            const result = await response.json();

            modal.hide();

            if (result.success) {

                alert(result.message);

                location.reload();

            } else {

                alert(result.message);

            }

        }

        catch (error) {

            modal.hide();

            alert("Unable to connect to AI Pipeline.");

        }

    });

}