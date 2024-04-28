import os
import subprocess

IGNORE_SERVICES_UPDATE = [
    'nextcloud',
    'cloudflared'
]

def main() -> None:
    services = os.listdir('src')

    running_from_host = os.getenv('SSH_TTY') is None

    for service in services:
        service_path  = os.path.join('src', service, 'compose.yaml')

        allow_service_update = service not in IGNORE_SERVICES_UPDATE and running_from_host

        if allow_service_update:
            subprocess.call(['docker', 'compose', '-f', service_path, 'pull'])

        subprocess.call(['docker', 'compose', '-f', service_path, 'up', '-d'])

if __name__ == '__main__':
    main()
