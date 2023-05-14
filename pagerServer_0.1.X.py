import os
address = "1016269"
frequency = "152175000"
baudRate = "512"
message = "Hello World OwO"

os.system('echo -e "'address':'message'" | sudo ./pocsag -f "'frequency'" -r 'baudRate' -t 1')