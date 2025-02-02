# Port Wine: CTF Challenge Documentation

## Overview
- **Challenge Name:** PortWine
- **Category:** Network Security
- **Difficulty Level:** Medium
- **Description:**  
  This challenge requires participants to exploit vulnerabilities in a Flask web application running on multiple ports to retrieve hidden flags. Participants will utilize network scanning and exploitation techniques to solve the challenge.

## Objective
The main objective is to find and retrieve the flag hidden in the Flask application. Participants must understand the application’s routing and vulnerabilities to successfully capture the flag.

## Setup Instructions

### 1. Environment Preparation
- **Server Setup:** Deploy a Flask application on a virtual machine (VM) or a cloud server.
- **Operating System:** Use a Linux distribution like Ubuntu.
- **Install Necessary Software:**
  - Python 3
  - Flask
  - Additional libraries (if required for your application)

### 2. Flask Application Configuration
- Create the Flask application.

### 3. Port Configuration
- The application is set to run on four different ports: **3000, 4000, 5000, and 8080**.
- Ensure static files (like `index.html` and `style.css`) are placed in the public directory.

### 4. Testing the Challenge
- Use Nmap to scan the server for open ports:
  ```sh
  nmap [Server_IP]
  ```
  **Description:** Performs a basic scan to list open ports.
  
  ```sh
  nmap -sV [Server_IP]
  ```
  **Description:** Identifies open ports and detects the service versions.
- Check that the expected open ports (3000, 4000, 5000, 8080) are accessible.
- Test flag retrieval by accessing the `/flag` route on the appropriate ports.

## Challenge Walkthrough

### 1. Scan for Open Ports
- Use Nmap to discover available ports.

### 2. Accessing the Web Applications
- Use a browser or `curl`:
  ```sh
  curl http://[Server_IP]:3000
  curl http://[Server_IP]:4000
  curl http://[Server_IP]:5000
  curl http://[Server_IP]:8080
  ```

## Retrieving the Flags

### Steps to Retrieve the Flag
1. Access `/flag` on **port 5000** to get the encrypted `flag.pdf`.
2. Access `/flag` on **port 8080** to retrieve the encoded password.
3. Decode the password using **Brainfuck** and use it to decrypt `flag.pdf`.

```sh
curl http://[Server_IP]:5000/flag
curl http://[Server_IP]:8080/flag
```

### Additional Notes
- Accessing `/flag` on ports **3000 and 4000** will not return a flag.

## Flag Format
- The flag should be formatted as:  
  ```
  CTF{hidden_flag}
  ```
- Ensure flags are securely stored and not exposed in the application's source code.

## License
This challenge is created for educational purposes. Feel free to use it for CTF events and learning exercises.
