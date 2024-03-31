# zalozenie:
# uruchomienie testera powoduje:\
# - wlaczenie serwera
# - wlaczenie kilku klientow (z argumentami typu nick)

import time
from subprocess import Popen, CREATE_NEW_CONSOLE
import constants

cmd_run_server = 'python server.py'
cmd_run_client = 'python client.py '

if __name__ == "__main__":

    client_instances = []

    serv_instance = Popen(cmd_run_server, creationflags=CREATE_NEW_CONSOLE)
    time.sleep(1)

    # Spawn client and server instances
    for x in range(5):
        cmd_with_name = cmd_run_client + constants.get_random_name()
        client_instances.append(Popen(cmd_with_name, creationflags=CREATE_NEW_CONSOLE))

    input("Press a key to kill all spawned instances of server and clients")

    # Kill all instances
    serv_instance.kill()
    for x in client_instances:
        x.kill()
