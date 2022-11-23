# SHARED
import json
import os
import signal
import sys
# SHARED

os.chdir(sys.path[0])
os.chdir("../..")

# CLASSES
from class_battery          import C_Battery
from class_websocketServer  import C_WebSocketServer
# CLASSES

class Server:
    c_battery=False
    c_websocketserver=False
    config=False
    
    def __init__(self):
        # print(f"SERVER START")
        
        # Get the config.
        with open('public/shared/config.json', 'r') as myfile:
            self.config = json.load( myfile )

        # Instantiate classes.
        self.c_battery         = C_Battery(self)
        self.c_websocketserver = C_WebSocketServer(self)

        # Start servers/services. (The rest of the program is just responses from services.)
        if self.config['toggles']['isActive_pythonWsServer']:
            signal.signal(signal.SIGINT, self.signal_handler)

            # Start the server.
            self.c_websocketserver.startServer()
            
            # Send the init string.
            print(self.config['python']['initString'], flush=True)

            # Serve forever.
            self.c_websocketserver.serverInstance.serve_forever()

    def signal_handler(self, sig, frame):
        # print('You pressed Ctrl+C!')
        # self.c_websocketserver.serverInstance.server_close()
        print(f"Python server closed")
        sys.exit(0)

# Start
server = Server()
