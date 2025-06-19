

# SuricataMCP 🚀

[![smithery badge](https://smithery.ai/badge/@Medinios/SuricataMCP)](https://smithery.ai/server/@Medinios/SuricataMCP)
[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/medinios-suricatamcp-badge.png)](https://mseep.ai/app/medinios-suricatamcp)


SuricataMCP is a Model Context Protocol Server that allows MCP clients to autonomously use suricata for network traffic analysis. It enables programmatic interaction with Suricata through tools like get_suricata_version, get_suricata_help, and get_alerts_from_pcap_file.

[![Watch the demo](https://img.youtube.com/vi/QnIT_DnSMTI/hqdefault.jpg)](https://youtu.be/QnIT_DnSMTI)

## 📰 Full Guide on Medium

For your convenience, we created a full Medium article that walks you through how to install and use SuricataMCP with Cursor step by step.
[Supercharging Cursor with SuricataMCP: Network Security at Your Fingertips](https://medium.com/@mediniosam/supercharging-cursor-with-suricatamcp-network-security-at-your-fingertips-e8f7e2db4094)

---

## 📦 Features

- 🔡 Easily get Suricata version and help info.
- 📁 Parse .pcap files and retrieve alerts using a simple tool interface.
- 🧠 Built with the MCP protocol for seamless integration with AI coding tools like Cursor.

---

## ⬇️ Downloading Suricata

To use this project, you'll need to download and install Suricata:

Go to the official Suricata site: https://suricata.io/download/

Follow installation instructions for your OS (Linux, macOS, or Windows)

On Linux, you can also install via package manager, e.g.:

bash
sudo apt install suricata

After installation, locate the Suricata binary and configuration files so you can set the correct paths in config.py.

---

## ⚙️ Installation Guide

### Installing via Smithery

To install Suricata Network Traffic Analysis Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@Medinios/SuricataMCP):

```bash
npx -y @smithery/cli install @Medinios/SuricataMCP --client claude
```

Follow these steps to set up **SuricataMCP** on your system:

---

### 1. Clone the Repository

Open your terminal and run:

    git clone https://github.com/medinios/SuricataMCP.git
    cd SuricataMCP

### 2. Install dependencies (e.g., if using a virtual environment)

    pip install -r requirements.txt

### 3. Edit the config.py file to specify your Suricata installation path:

    SURICATA_DIR = "/path/to/suricata"
    SURICATA_EXE_FILE = "suricata"  # or "suricata.exe" on Windows

### 4. Add SuricataMCP to your AI platform with:

      {
        "mcpServers": {
          "SuricataMcp": {
            "command": "cmd",
            "args": ["/c", "mcp", "run", "[YourPath]\\SuricataMcp\\suricata-mcp.py"]
          }
        }
      }

---

## 🚀 Usage

Run the MCP server locally from your AI platform (like Cursor)

When running, the server exposes the following MCP tools:

- get_suricata_version(): Returns Suricata's version string.
- get_suricata_help(): Returns Suricata CLI help output.
- get_alerts_from_pcap_file(pcap_destination: str, destination_folder_results: str): Runs Suricata on the given .pcap file and returns the content of fast.log.

---

## 📄 Adding Custom Rules

To extend Suricata with your own detection rules:

1. Add your custom rule files (e.g., custom.rules) to the suricata/rules directory.

---

## ⚠️ Disclaimer

We are not affiliated with the official Suricata project or the OISF (Open Information Security Foundation). SuricataMCP is an independent integration built for personal use inside Cursor.
Example pcap was taken from [PCAP-ATTACK](https://github.com/sbousseaden/PCAP-ATTACK)

---

## 🤝 Contributors

This project was built by two developers passionate about security, context-aware systems, and building useful tools for the community. Every line of code, every CLI command, and every integration was a product of focused collaboration and shared curiosity.

[Sam Med](https://www.linkedin.com/in/sam-medina-4b0823164/),
[Raz Tel-Vered](https://www.linkedin.com/in/raz-tel-vered/)

## 🤝 Contributing

PRs and suggestions are welcome! Let's make SuricataMCP more accessible and programmable together.
