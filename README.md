# 🌐 Simple Proxy Server

A simple Python-based proxy server that acts as an intermediary between a client and a server. It forwards HTTP requests from the client to the target server and relays the server’s response back to the client. This project demonstrates the core principles of socket programming and is ideal for learning how proxy servers operate in real-world networks.

---

## 📌 Project Overview

This project was developed as part of a Computer Networks course to provide hands-on experience with network socket programming. It highlights how proxy servers can be used to monitor, redirect, or filter traffic between clients and servers.

---

## 🧾 Table of Contents

- [Features](#features)
- [Files Included](#files-included)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Installation & Usage](#installation--usage)
- [Project Report & Presentation](#project-report--presentation)
- [License](#license)

---

## ✅ Features

- Accepts HTTP client requests
- Parses target URLs and connects to web servers
- Forwards requests and returns server responses
- Easily customizable for:
  - Logging traffic
  - Filtering content
  - Caching data

---

## 📂 Files Included

| File Name         | Description                                      |
|-------------------|--------------------------------------------------|
| `proxy_server.py` | Core Python script to run the proxy server       |
| `Final_Report.pdf`| Detailed academic report with system design      |
| `CN_PPT.pdf`      | Presentation slides for demonstration purposes   |

---

## ⚙️ How It Works

1. Client sends a request to the proxy server.
2. The proxy intercepts the request and extracts the destination.
3. It establishes a connection with the actual server.
4. The response is relayed back to the client.
5. (Optional) The traffic can be logged, filtered, or cached.

---

## 💻 Technologies Used

- **Language:** Python 3
- **Libraries:** `socket`, `threading` (if implemented)
- **Concepts:** HTTP, TCP/IP, Client-Server Architecture

---

## 📦 Installation & Usage

### 🔧 Prerequisites
- Python 3.x installed on your system.

### ▶️ Run the Proxy Server

```bash
python proxy_server.py
