class Incident:
    """
    Represents a detected cybersecurity incident.
    """

    def __init__(
        self,
        attack,
        source_ip,
        severity,
        priority,
        risk_score,
        recommendation,
        status="Open"
    ):
        self.attack = attack
        self.source_ip = source_ip
        self.severity = severity
        self.priority = priority
        self.risk_score = risk_score
        self.recommendation = recommendation
        self.status = status

    def to_dict(self):
        """
        Convert Incident object to dictionary.
        """

        return {
            "attack": self.attack,
            "source_ip": self.source_ip,
            "severity": self.severity,
            "priority": self.priority,
            "risk_score": self.risk_score,
            "recommendation": self.recommendation,
            "status": self.status,
        }

    def __str__(self):
        """
        String representation of the Incident.
        """

        return (
            f"Incident("
            f"attack={self.attack}, "
            f"source_ip={self.source_ip}, "
            f"severity={self.severity}, "
            f"priority={self.priority}, "
            f"risk_score={self.risk_score}, "
            f"status={self.status})"
        )