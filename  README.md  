Offensive Security Tool
This project is a multi-purpose offensive security tool designed for various tasks such as file exfiltration, reverse shells, and privilege escalation on both macOS and Windows platforms.

Features
File Exfiltration: Transfer files from the target machine to a remote server (supports macOS and Windows).
Reverse Shells: Execute reverse shells to connect and control the target machine remotely.
Privilege Escalation: Exploit vulnerabilities to gain higher-level permissions on the target machine.

Directory Structure

offensive_security_tool/
│
├── .venv/                     # Virtual environment folder 
│
├── modules/
│   ├── exploits/
│   │   ├── mac_file_exfiltration.py        # macOS file exfiltration script
│   │   ├── mac_privilege_escalation.py     # macOS privilege escalation exploit
│   │   ├── mac_python_reverse_shell.py     # macOS reverse shell (Python)
│   │   ├── mac_reverse_shell.py            # macOS reverse shell script
│   │   ├── windows_file_exfiltration.py    # Windows file exfiltration script
│   │   ├── windows_privilege_escalation.py # Windows privilege escalation exploit
│   │   ├── windows_reverse_shell.py        # Windows reverse shell script
│   │   └── reverse_shell.py                # Generic reverse shell for various OS
│   │
│   └── utils/
│       ├── logging_setup.py                # Centralized logging configuration
│
├── uploads/                   # Store exfiltrated files here
│   ├── example.encrypted        # Example of an encrypted file
│
├── logs/                      # Centralized logs folder
│   ├── server.log             # Server-side logs
│   ├── exfiltration.log       # Exfiltration logs
│
├── README.md                  # Project documentation (this file)
│
├── server.py                  # Flask server script to receive exfiltrated files
├── main.py                    # Main entry point for the tool (menu-driven interface)
└── requirements.txt           # Python dependencies for the project

*Installation

Clone the repository:
git clone https://github.com/your-repo/offensive_security_tool.git
cd offensive_security_tool

Set up the virtual environment:
python3 -m venv .venv
source .venv/bin/activate

Install the required Python packages:
pip install -r requirements.txt


*Usage
1. Run the Server
The server needs to be running to receive files during the exfiltration process.
python server.py
Logs will be stored in logs/server.log.

2. File Exfiltration (macOS)
Run the macOS file exfiltration script:
python modules/exploits/mac_file_exfiltration.py
Provide the path to the file you wish to exfiltrate and the server URL (e.g., http://127.0.0.1:5001/exfiltrate).

Logs for the exfiltration will be stored in logs/exfiltration.log.

3. Reverse Shell (macOS/Windows)
Run the reverse shell for macOS or Windows:
macOS:
python modules/exploits/mac_reverse_shell.py

Windows:
python modules/exploits/windows_reverse_shell.py
Once executed, the reverse shell will connect back to your server. Set up a listener on your server to receive connections.

4. Privilege Escalation (macOS/Windows)
Run the privilege escalation exploit:

macOS:
python modules/exploits/mac_privilege_escalation.py

Windows:
python modules/exploits/windows_privilege_escalation.py

5. Using the Menu-Driven Interface (Main Script)
Run the tool's main script to select and execute exploits through an interactive menu:
python main.py
You can choose from the available exploits for file exfiltration, reverse shells, and privilege escalation.

*Logging
Server Logs: All server-related logs (including exfiltrated data) are stored in logs/server.log.
Exfiltration Logs: File exfiltration-related activities are logged in logs/exfiltration.log.
The logging_setup.py in the utils folder centralizes the logging configuration for all modules, ensuring consistent log formatting and output.

**Contributing**
Fork the repository.
Create a feature branch.
Commit your changes.
Push to your branch.
Create a pull request.


*License
This project is licensed under the MIT License.

