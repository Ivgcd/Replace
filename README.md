This script demonstrates an HTTP file replacement attack using NetfilterQueue and Scapy. It intercepts executable download requests, tracks TCP acknowledgments, and modifies the server response to redirect the victim to a malicious payload. This project helped me understand packet manipulation, TCP sequencing, and MITM attack techniques.
for HTTPS interception we need to download "mitmproxy" tool and we need to create another file and write the script
and we neet to download MITM certificate on victim computer to decrypt-modify-re-encrypt the traffic oh https.
