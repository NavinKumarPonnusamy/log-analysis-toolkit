# Log Analysis & Network Detection Toolkit

A set of small Python security tools built while learning log parsing, detection logic and packet analysis on a Kali Linux lab VM. Each tool was written from scratch to undertsand *how* detection works under the hood, the same per-source, per-time-window logic that SIEMs and tools like fail2ban use.

All testing was done against my own lab VM and legal practice targets (e.g. zonetransfer.me). Nothing here is intended for use against for use against system without authorisation.

## Tools

| Script | What it does |
|---|---|
| `failed_login.py` | Parses SSH `auth.log`, counts failed logins per IP and per username. |
| `outside_hours.py` | Flags successful SSH logins that occur outside working hours (nights/weekends), using timestamp parsing. |
| `bruteforce.py` | Detects SSH brute-force: flags an IP with 5+ failures inside a 2-minute window (sliding window), not just a high total. |
| `weblog.py` | Summarises an nginx access log: top IPs, top paths, status-code breakdown, scanner user-agents (sqlmap/nikto/etc.), and IPs with many 404s (probing). |
| `live_monitor.py` | Follows a live log file (`tail -f` style) and prints new lines as they arrive. |
| `dns_detector.py` | Reads a packet capture with Scapy and flags DNS reconnaissance: a source sending too many queries too fast. |
| `make_test_pcap.py` | Crafts synthetic DNS packets (Scapy) from a chosen source IP, for testing the detector. |
| `dns_detector_multi.py` | Runs the DNS detector across multiple captures, proving it groups and flags each source IP independently. |

## Key Concepts Demonstrated
- Log parsing with string methods and **regex** (capture groups for messy nginx lines)
- **Timestamp parsing** with 'datetime' (handling year-less syslog timestamps).
- **Sliding-window detection** - the same core logic reused across SSH, web, and DNS.
- **Packet analysis & crafting** with Scapy ('rdpcap' / 'wrpcap' reading and building layered packets).

## Usage 
Each script reads a local data file (log or '.pcap') and prints its findings.
Example:
```bash
python3 bruteforce.py 		# expects auth.log in the same folder
python3 weblog.py     		# expects access.log
python3 dns_detector.py		# expects dns_capture.pcap
```
Sample data files are not included (see '.gitignore'); generate your own from a lab VM.

## Note
Built as a learning project, defensive/detection focused, with every tool written and debugged by hand to understand the mechanics rather than rely on existing tools.
