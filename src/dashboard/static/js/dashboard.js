document.addEventListener("DOMContentLoaded", function () {

    // Incident Trend

    const incidentCanvas = document.getElementById("incidentChart");

    if (incidentCanvas) {

        new Chart(incidentCanvas, {

            type: "line",

            data: {

                labels: [
                    "Mon",
                    "Tue",
                    "Wed",
                    "Thu",
                    "Fri",
                    "Sat",
                    "Sun"
                ],

                datasets: [

                    {

                        label: "Incidents",

                        data: [2, 5, 3, 7, 6, 8, 4],

                        borderWidth: 3,

                        fill: false

                    }

                ]

            }

        });

    }

    // Attack Distribution

    const attackCanvas = document.getElementById("attackChart");

    if (attackCanvas) {

        new Chart(attackCanvas, {

            type: "pie",

            data: {

                labels: [

                    "Brute Force",
                    "SQL Injection",
                    "Malware",
                    "DDoS"

                ],

                datasets: [

                    {

                        data: [45, 20, 15, 20]

                    }

                ]

            }

        });

    }

});