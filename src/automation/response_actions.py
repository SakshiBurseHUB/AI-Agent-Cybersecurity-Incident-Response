from utils.logger import log_info


def execute_response_actions(responses):
    """
    Simulate execution of incident response actions.

    Args:
        responses (list): Incident response recommendations.

    Returns:
        list: Execution results.
    """

    log_info("Executing automated response actions...")

    execution_results = []

    for response in responses:

        attack = response["Attack"]
        source_ip = response["Source_IP"]

        executed_actions = []

        for action in response["Actions"]:

            executed_actions.append({
                "Action": action,
                "Status": "Success"
            })

        execution_results.append({
            "Attack": attack,
            "Source_IP": source_ip,
            "Execution_Status": "Completed",
            "Executed_Actions": executed_actions
        })

    log_info(f"Executed response actions for {len(execution_results)} incidents.")

    return execution_results