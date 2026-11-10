# Connecting from outside the lab (VPN)
Source: IT wiki - last edited 14 Sep 2026

## What you need
- An active Kestrel Lab account (your username, not your e-mail address).
- The Kestrel Authenticator app on your phone, for two-factor approval.
- The KestrelConnect VPN app. It is already installed on lab laptops. On a personal computer, download it from the Software Center page of the intranet.

## Setting up the connection
Create a new connection called "Kestrel Remote" with the server address vpn.kestrel-lab.example and port 443. Log in with your lab username and password. A push notification then appears in the Kestrel Authenticator app: approve it within 60 seconds.

## Which profile should I choose?
There are two profiles. "Kestrel Remote - Lite" only gives access to e-mail, Teams and the intranet. "Kestrel Remote - Full" gives access to everything, including the file shares, GitLab, the license servers and the Falcon GPU cluster. Use Full when you need research systems. Use Lite for normal office work, because it is faster on slow home connections.

## Common errors
- Error 2041 (MFA timeout): you did not approve the push notification within 60 seconds. Connect again and approve faster.
- Error 3010 (account locked): too many wrong passwords. Your account unlocks automatically after 30 minutes, or you can call the IT helpdesk.
- Connected, but GitLab or the cluster does not open: you are probably on the Lite profile. Disconnect and choose Full.
For anything else, contact the IT helpdesk on extension 4412.
