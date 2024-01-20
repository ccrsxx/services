import os
import subprocess

def main() -> None:
    services = os.listdir('src')

    for service in services:
        service_path  = os.path.join('src', service, 'compose.yaml')
        subprocess.call(['docker', 'compose', '-f', service_path, 'up', '-d'])

if __name__ == '__main__':
    main()
