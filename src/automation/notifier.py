from utils.logger import log_info


def notify_soc_team(responses):
    """
    Simulate sending notifications to the SOC team.

    Args:
        responses (list): Incident response recommendations.

    Returns:
        list: Notification results.
    """

    log_info("Sending SOC notifications...")

    notifications = []

    for response in responses:

        notification = {
            "Attack": response["Attack"],
            "Source_IP": response["Source_IP"],
            "Recipient": "SOC Team",
            "Channel": "Email",
            "Status": "Sent"
        }

        notifications.append(notification)

    log_info(f"Sent {len(notifications)} SOC notifications.")

    return notifications