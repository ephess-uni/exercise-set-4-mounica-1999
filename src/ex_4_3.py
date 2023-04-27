""" ex_4_3.py """

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation.
    """
    shutdown_events = get_shutdown_events(logfile)
    shutdown_messages = [event['message'] for event in shutdown_events]
    shutdown_datetimes = [logstamp_to_datetime(event['date']) for event in shutdown_events]
    time_diff = max(shutdown_datetimes) - min(shutdown_datetimes)
    return time_diff


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
