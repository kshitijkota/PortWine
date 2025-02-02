## **Port Wine: CTF Challenge**
A Capture The Flag (CTF) challenge focused on **network security**, where participants exploit vulnerabilities in a **Flask web application running on multiple ports** to retrieve hidden flags.  

### **Creators**
Kshitij Koushik Kota - https://github.com/kshitijkota <br/>
Sampriti Saha - https://github.com/Sampriti2803 <br/>

---

### **Challenge Overview**
- **Challenge Name:** Port Wine
- **Category:** Network Security  
- **Difficulty Level:** Medium  
- **Description:** Participants will utilize network scanning and exploitation techniques to identify and extract hidden flags from multiple Flask applications running on different ports.  

---

## **Objective**
The goal is to **retrieve the flag** hidden within the Flask web application by:
- Identifying **open ports** and **running services**.
- Understanding **application behavior** and **potential vulnerabilities**.
- Extracting **hidden flags** using various techniques, including **Brainfuck decoding**.  

---

## **Setup Instructions**
### **1. Environment Preparation**
- **Server Setup:** Deploy the Flask application on a **virtual machine (VM)** or **cloud server**.  
- **Operating System:** Recommended **Linux (Ubuntu)** environment.  
- **Install Dependencies:**
  ```sh
  sudo apt update && sudo apt install python3 python3-pip
  pip install flask
  ```

### **2. Running the Flask Application**
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/port-wine-ctf.git
   cd port-wine-ctf
   ```
2. Start the Flask applications:
   ```sh
   python3 index.py
   ```
3. The applications will run on the following **ports**:
   - **8000**  
   - **5001**  
   - **8080**  
   - **4000**  

### **3. Understanding the Web Application**
- The **homepage** (`/`) serves an `index.html` file from the **public directory** (on port **8000**).  
- The `/flag` route on different ports **reveals different clues** to retrieve the final flag.

---

## **Challenge Walkthrough**
### **1. Scan for Open Ports**
Use **Nmap** to identify active services:  
```sh
nmap [Server_IP]
```
For more detailed version detection:
```sh
nmap -sV [Server_IP]
```
Expected open ports: `8000, 5001, 8080, 4000`

---

### **2. Retrieving the Flags**
1. **Port 5001**  
   - Access:  
     ```sh
     curl http://[Server_IP]:5001/flag
     ```
   - Returns a **Google Drive link** containing an encrypted `flag.pdf`.

2. **Port 8080**  
   - Access:  
     ```sh
     curl http://[Server_IP]:8080/flag
     ```
   - Returns an **encoded password**: `Flag4_Txt_Op3n#`

3. **Port 8000 & 4000**  
   - No useful flags are found.

---

### **3. Decoding the Password & Extracting the Flag**
1. The password retrieved from **port 8080** is **Brainfuck-encoded**.  
2. Decode it using a Brainfuck interpreter.
3. Use the **decoded password** to unlock `flag.pdf`.

---

## **Flag Format**
- The final flag should be in the format:  
  ```sh
  CTF{hidden_flag}
  ```
- Ensure the flags **are not exposed in the source code**.

---

## **License**
This project is licensed under the [MIT License](LICENSE).
