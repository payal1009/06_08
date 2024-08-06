import os
import time
import psutil
import asyncio
from datetime import  datetime
#for i in range(2,10):
start_p= time.time()
async def start():
        os.system(f'start /B python process_id2.py')
        print("process started")
        await asyncio.sleep(20)
        f=open("file2.txt",'r')
        x=int(f.read().strip())
        f.close()
        await asyncio.sleep(60)
        print(f'Started process_id2.py : {x}')
        print("terminating process_id2.py")
        try:
            child_process = psutil.Process(x)
            child_process.terminate()
            print("Process terminated")
        except psutil.NoSuchProcess:
            print(f"No such process: {x}")
        except psutil.AccessDenied:
            print(f"Access denied when trying to kill process: {x}")
        except psutil.Error as e:
            print(f"An error occurred: {x}")
        print('process_id.py end')
asyncio.run(start())
end_p = time.time()
print(f' Total time for parent process- {(end_p-start_p)}')