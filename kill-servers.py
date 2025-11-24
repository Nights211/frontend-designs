#!/usr/bin/env python3
import subprocess
import sys

def kill_servers():
    """Kill all running servers on ports 8000 and 8001"""
    ports = [8000, 8001]
    killed = False
    
    for port in ports:
        try:
            result = subprocess.run(
                ['lsof', '-ti', f':{port}'],
                capture_output=True,
                text=True
            )
            pids = result.stdout.strip().split('\n')
            
            for pid in pids:
                if pid:
                    subprocess.run(['kill', '-9', pid])
                    print(f"✅ Killed process {pid} on port {port}")
                    killed = True
        except Exception as e:
            pass
    
    if not killed:
        print("ℹ️  No servers running on ports 8000 or 8001")

if __name__ == '__main__':
    kill_servers()
