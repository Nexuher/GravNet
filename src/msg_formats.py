import constants

# Message formats
STANDARD_MSG_FORMAT  = "{0}~{1}~{2}"
PRIVATE_MSG_FORMAT  = "{0}~PRIV FROM: {1}~{2}"

def get_server_announcement_message(message_timestamp, message):
    formatted_message = get_standard_message(message_timestamp, "SERVER ANNOUNCEMENT", message)
    return formatted_message


def get_standard_message(message_timestamp, username, message):
    formatted_message = STANDARD_MSG_FORMAT.format(message_timestamp, username, message)
    return formatted_message


def get_private_message(message_timestamp, username, message):
    formatted_message = PRIVATE_MSG_FORMAT.format(message_timestamp, username, message)
    return formatted_message


def split_standard_message(formatted_message):
    """Returns: message_timestamp, username, message"""
    parts = formatted_message.split("~")

    return parts[0], parts[1], parts[2]


def is_private_message(message_content):
    return message_content[0] == constants.PRIVATE_MESSAGE_PREFIX_SIGN


def get_priv_receiver_and_message(message_content):
    receiver_username = ""
    start_of_message = 0

    for letter in range(1, len(message_content)):
        if message_content[letter] != " ":
            start_of_message += 1
            receiver_username += message_content[letter]
        else:
            start_of_message += 1
            break

    message = message_content[start_of_message + 1:]

    return receiver_username, message
