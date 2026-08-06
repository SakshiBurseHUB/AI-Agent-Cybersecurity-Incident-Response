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
// AI Pipeline Progress
// ======================================

const runBtn = document.getElementById("runPipelineBtn");

if(runBtn){

    runBtn.addEventListener("click", async function(){

        const modal = new bootstrap.Modal(
            document.getElementById("loadingModal")
        );

        modal.show();

        const progress = document.getElementById("pipelineProgress");

        const steps = [

            "Collecting Security Logs",

            "Detecting Threats",

            "Classifying Threats",

            "Analyzing Threats",

            "Saving Incidents",

            "Generating Responses",

            "Executing Playbooks",

            "Sending Notifications"

        ];

        progress.innerHTML = "";

        for(let i=0;i<steps.length;i++){

            progress.innerHTML +=
                `<div class="pipeline-current">
                     ${steps[i]}
                </div>`;

            await new Promise(r=>setTimeout(r,500));

        }

        try{

            const response = await fetch("/run-analysis");

            const result = await response.json();

            if(result.success){

                progress.innerHTML +=
                    `<div class="pipeline-success mt-3">
                         Pipeline Completed Successfully
                    </div>`;

                setTimeout(function(){

                    modal.hide();

                    location.reload();

                },1000);

            }

            else{

                progress.innerHTML +=
                    `<div class="text-danger mt-3">
                        ${result.message}
                    </div>`;

            }

        }

        catch(error){

            progress.innerHTML +=
                `<div class="text-danger mt-3">

                    Connection Error

                </div>`;

        }

    });

}

// ======================================
// Live Dashboard Refresh
// ======================================

async function refreshDashboard(){

    try{

        const response = await fetch("/dashboard-data");

        const data = await response.json();

        // -----------------------------
        // Update Dashboard Cards
        // -----------------------------

        document.getElementById("totalIncidents").innerText =
            data.stats.total_incidents;

        document.getElementById("openIncidents").innerText =
            data.stats.open_incidents;

        document.getElementById("highSeverity").innerText =
            data.stats.high_severity;

        document.getElementById("criticalRisk").innerText =
            data.stats.critical_risk;

        // -----------------------------
        // Update Incident Table
        // -----------------------------

        const table =
            document.getElementById("incidentTableBody");

        table.innerHTML = "";

        data.incidents.forEach(incident => {

            let severityBadge = "";
            let statusBadge = "";

            if(incident[3] === "High"){

                severityBadge =
                    '<span class="badge bg-danger">High</span>';

            }

            else if(incident[3] === "Medium"){

                severityBadge =
                    '<span class="badge bg-warning text-dark">Medium</span>';

            }

            else{

                severityBadge =
                    '<span class="badge bg-success">Low</span>';

            }

            if(incident[7] === "Open"){

                statusBadge =
                    '<span class="badge bg-primary">Open</span>';

            }

            else if(incident[7] === "Resolved"){

                statusBadge =
                    '<span class="badge bg-success">Resolved</span>';

            }

            else{

                statusBadge =
                    `<span class="badge bg-secondary">
                        ${incident[7]}
                    </span>`;

            }

            table.innerHTML += `

            <tr>

                <td>${incident[0]}</td>

                <td>${incident[1]}</td>

                <td>${incident[2]}</td>

                <td>${severityBadge}</td>

                <td>${incident[4]}</td>

                <td>${incident[5]}</td>

                <td>${statusBadge}</td>

            </tr>

            `;

        });

    }

    catch(error){

        console.log("Dashboard refresh failed.");

    }

}

// Refresh every 30 seconds

setInterval(refreshDashboard,30000);