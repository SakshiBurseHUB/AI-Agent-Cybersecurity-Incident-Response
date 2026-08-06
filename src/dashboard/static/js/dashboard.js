document.addEventListener("DOMContentLoaded", function () {

    // ==========================================
    // Incident Severity Chart
    // ==========================================

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

                        backgroundColor: [

                            "#2563EB",
                            "#F59E0B",
                            "#EF4444"

                        ],

                        borderRadius: 10,

                        borderSkipped: false

                    }

                ]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                animation: {

                    duration: 1500

                },

                plugins: {

                    legend: {

                        display: false

                    }

                },

                scales: {

                    y: {

                        beginAtZero: true,

                        ticks: {

                            stepSize: 1

                        }

                    }

                }

            }

        });

    }

    // ==========================================
    // Attack Distribution Chart
    // ==========================================

    const attackCanvas = document.getElementById("attackChart");

    if (attackCanvas) {

        const labels = JSON.parse(
            attackCanvas.dataset.labels
        );

        const values = JSON.parse(
            attackCanvas.dataset.values
        );

        new Chart(attackCanvas, {

            type: "doughnut",

            data: {

                labels: labels,

                datasets: [

                    {

                        data: values,

                        backgroundColor: [

                            "#2563EB",
                            "#EF4444",
                            "#F59E0B",
                            "#22C55E",
                            "#8B5CF6"

                        ],

                        borderWidth: 0

                    }

                ]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                cutout: "70%",

                animation: {

                    duration: 1500

                },

                plugins: {

                    legend: {

                        position: "bottom"

                    }

                }

            }

        });

    }

});


// ==========================================
// Live Clock
// ==========================================

function updateClock() {

    const now = new Date();

    const time = document.getElementById("currentTime");

    const date = document.getElementById("currentDate");

    if (time) {

        time.innerHTML = now.toLocaleTimeString();

    }

    if (date) {

        date.innerHTML = now.toDateString();

    }

}

updateClock();

setInterval(updateClock, 1000);


// ==========================================
// Animated Dashboard Counters
// ==========================================

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

        else {

            counter.innerText = target;

        }

    };

    updateCounter();

});


// ==========================================
// Run AI Pipeline
// ==========================================

const runBtn = document.getElementById("runPipelineBtn");

if (runBtn) {

    runBtn.addEventListener("click", async function () {

        const modal = new bootstrap.Modal(

            document.getElementById("loadingModal")

        );

        modal.show();

        const progress = document.getElementById("pipelineProgress");

        progress.innerHTML = "";

        const steps = [

            "Collecting Security Logs",

            "Detecting Threats",

            "Classifying Threats",

            "Analyzing Threats",

            "Saving Incidents",

            "Generating Responses",

            "Executing Playbooks",

            "Sending SOC Notifications"

        ];

        for (const step of steps) {

            progress.innerHTML += `

                <div class="pipeline-current mb-2">

                    <i class="bi bi-arrow-repeat"></i>

                    ${step}

                </div>

            `;

            await new Promise(resolve => setTimeout(resolve, 500));

        }

        try {

            const response = await fetch("/run-analysis");

            const result = await response.json();

            if (result.success) {

                progress.innerHTML += `

                    <div class="pipeline-success mt-3">

                        <i class="bi bi-check-circle-fill"></i>

                        Pipeline Completed Successfully

                    </div>

                `;

                setTimeout(() => {

                    modal.hide();

                    location.reload();

                }, 1200);

            }

            else {

                progress.innerHTML += `

                    <div class="text-danger mt-3">

                        ${result.message}

                    </div>

                `;

            }

        }

        catch (error) {

            progress.innerHTML += `

                <div class="text-danger mt-3">

                    Connection Error

                </div>

            `;

        }

    });

}


// ==========================================
// Live Dashboard Refresh
// ==========================================

async function refreshDashboard() {

    try {

        const response = await fetch("/dashboard-data");

        const data = await response.json();

        // Dashboard Cards

        const total = document.getElementById("totalIncidents");
        const open = document.getElementById("openIncidents");
        const high = document.getElementById("highSeverity");
        const critical = document.getElementById("criticalRisk");

        if (total) total.innerText = data.stats.total_incidents;

        if (open) open.innerText = data.stats.open_incidents;

        if (high) high.innerText = data.stats.high_severity;

        if (critical) critical.innerText = data.stats.critical_risk;

        // Incident Table

        const table = document.getElementById("incidentTableBody");

        if (!table) return;

        table.innerHTML = "";

        data.incidents.forEach(incident => {

            const severityBadge = incident[3] === "High"

                ? '<span class="badge bg-danger">High</span>'

                : incident[3] === "Medium"

                ? '<span class="badge bg-warning text-dark">Medium</span>'

                : '<span class="badge bg-success">Low</span>';

            const statusBadge = incident[7] === "Open"

                ? '<span class="badge bg-primary">Open</span>'

                : incident[7] === "Resolved"

                ? '<span class="badge bg-success">Resolved</span>'

                : `<span class="badge bg-secondary">${incident[7]}</span>`;

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

    catch (error) {

        console.log("Dashboard refresh failed.");

    }

}

// Refresh dashboard every 30 seconds

setInterval(refreshDashboard, 30000);

// ======================================
// Incident Search & Filtering
// ======================================

const attackSearch = document.getElementById("searchAttack");
const ipSearch = document.getElementById("searchIP");
const severityFilter = document.getElementById("severityFilter");
const statusFilter = document.getElementById("statusFilter");
const clearFilters = document.getElementById("clearFilters");

function filterIncidents() {

    const attack = attackSearch.value.toLowerCase();
    const ip = ipSearch.value.toLowerCase();
    const severity = severityFilter.value;
    const status = statusFilter.value;

    const rows = document.querySelectorAll(".incident-row");

    rows.forEach(row => {

        const attackText =
            row.querySelector(".attack-column").innerText.toLowerCase();

        const ipText =
            row.querySelector(".ip-column").innerText.toLowerCase();

        const severityText =
            row.querySelector(".severity-column").innerText.trim();

        const statusText =
            row.querySelector(".status-column").innerText.trim();

        const matchAttack = attackText.includes(attack);
        const matchIP = ipText.includes(ip);
        const matchSeverity =
            severity === "" || severityText.includes(severity);

        const matchStatus =
            status === "" || statusText.includes(status);

        if (
            matchAttack &&
            matchIP &&
            matchSeverity &&
            matchStatus
        ) {

            row.style.display = "";

        } else {

            row.style.display = "none";

        }

    });

}

if (attackSearch) {

    attackSearch.addEventListener("keyup", filterIncidents);
    ipSearch.addEventListener("keyup", filterIncidents);

    severityFilter.addEventListener("change", filterIncidents);
    statusFilter.addEventListener("change", filterIncidents);

    clearFilters.addEventListener("click", () => {

        attackSearch.value = "";
        ipSearch.value = "";
        severityFilter.value = "";
        statusFilter.value = "";

        filterIncidents();

    });

}