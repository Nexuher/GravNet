# Message formats
STANDARD_MSG_FORMAT  = "{0}~{1}~{2}"

def get_server_announcement_message(message_timestamp, message):
    formatted_message = get_standard_message(message_timestamp, "SERVER ANNOUNCEMENT", message)
    return formatted_message

def get_standard_message(message_timestamp, username, message):
    formatted_message = STANDARD_MSG_FORMAT.format(message_timestamp, username, message)
    return formatted_message


def split_standard_message(formatted_message):
    """Returns: message_timestamp, username, message"""
    parts = formatted_message.split("~")

    return parts[0], parts[1], parts[2]


