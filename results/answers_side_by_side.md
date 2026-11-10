# Baseline vs optimized answers

## q01: My VPN connection fails with error 2041. What does that mean?
Expected: timeout (sources: vpn_access)

**Baseline** (ok=True, 965 tokens): Error 2041 indicates an MFA timeout – you didn’t approve the push notification within the 60‑second window. Connect again and approve the notification faster. [vpn_access]

**Optimized** (ok=True, 688 tokens): Error 2041 means the MFA push notification timed out because you did not approve it within 60 seconds. [vpn_access]

## q02: How far in advance do I need to book a cleanroom slot?
Expected: 48 hours (sources: cleanroom_booking)

**Baseline** (ok=True, 753 tokens): You must book a cleanroom slot at least **48 hours in advance**. [cleanroom_booking]

**Optimized** (ok=True, 513 tokens): You must book at least 48 hours in advance. [cleanroom_booking]

## q03: What is the longest a single job can run on the GPU cluster?
Expected: 48 hours (sources: gpu_cluster_tutorial)

**Baseline** (ok=True, 976 tokens): The longest a single job can run on the Falcon GPU cluster is **48 hours** (in the `gpu-long` partition). [gpu_cluster_tutorial]

**Optimized** (ok=True, 620 tokens): The longest a single job can run on the Falcon GPU cluster is 48 hours. [gpu_cluster_tutorial]

## q04: How long are files kept on /scratch?
Expected: 30 days (sources: gpu_cluster_tutorial)

**Baseline** (ok=True, 766 tokens): Files on /scratch are automatically deleted after **30 days**. [gpu_cluster_tutorial]

**Optimized** (ok=True, 520 tokens): Files older than 30 days on /scratch are automatically deleted. [gpu_cluster_tutorial]

## q05: What's the phone extension of the IT helpdesk?
Expected: 4412 (sources: it_helpdesk_faq)

**Baseline** (ok=True, 868 tokens): The IT helpdesk can be reached at extension **4412**. [it_helpdesk_faq]

**Optimized** (ok=True, 551 tokens): The IT helpdesk can be reached at extension 4412. [it_helpdesk_faq]

## q06: How often do I have to change my password?
Expected: 180 (sources: it_helpdesk_faq)

**Baseline** (ok=True, 821 tokens): Passwords expire every 180 days. [it_helpdesk_faq]

**Optimized** (ok=True, 558 tokens): Passwords expire every 180 days. [it_helpdesk_faq]

## q07: At what time are the project shares backed up?
Expected: 02:00 (sources: data_storage_policy)

**Baseline** (ok=True, 784 tokens): Project shares are backed up every night at **02:00**. [data_storage_policy]

**Optimized** (ok=True, 539 tokens): Project shares are backed up nightly at 02:00. [data_storage_policy]

## q08: How long do we have to keep research data after a project ends?
Expected: 10 years (sources: data_storage_policy)

**Baseline** (ok=True, 779 tokens): Research data must be kept for at least 10 years after the end of the project, together with a short README file that explains the data. [data_storage_policy]

**Optimized** (ok=True, 531 tokens): Research data must be kept for at least 10 years after the end of the project. [data_storage_policy]

## q09: What is the internal emergency number?
Expected: 5555 (sources: incident_reporting)

**Baseline** (ok=True, 703 tokens): The internal emergency number is **5555** [incident_reporting].

**Optimized** (ok=True, 479 tokens): 5555. [incident_reporting]

## q10: Something almost fell on a colleague in the lab, but nobody was hurt. Do I need to report it, and how?
Expected: safelog / 24 hours (sources: incident_reporting)

**Baseline** (ok=True, 932 tokens): Yes – that’s a *near‑miss* and must be reported.  
Every incident and every near‑miss has to be logged in SafeLog within 24 hours, and a copy is automatically sent to your supervisor. [incident_reporting]

**Optimized** (ok=True, 570 tokens): Yes, you must report it as a near‑miss.  
Report the incident in SafeLog within 24 hours; your supervisor will receive a copy automatically.  
[incident_reporting]

## q11: The printer just beeps and won't release my print jobs when I tap my new badge. What should I do?
Expected: register (sources: chat_printer_badge)

**Baseline** (ok=True, 857 tokens): Tap your new badge on any printer, choose **“Register badge”** and log in with your lab username. Once the badge is registered it will work with the printers. [chat_printer_badge]

**Optimized** (ok=True, 685 tokens): Tap your new badge on the printer, choose “Register badge,” and log in with your lab username. Once registered, the printer will accept your jobs. If it still beeps, contact the facilities desk at extension 4500. [chat_printer_badge]

## q12: Where can I borrow an oscilloscope, and for how long?
Expected: b1.07 / 14 days (sources: chat_equipment_pool)

**Baseline** (ok=True, 962 tokens): You can borrow an oscilloscope from the equipment pool in room B1.07. The maximum loan period is 14 days, and you may extend it once for an additional 7 days if the device is not reserved by someone else.  
[chat_equipment_pool]

**Optimized** (ok=True, 639 tokens): You can borrow an oscilloscope from the equipment pool in room B1.07. The maximum loan period is 14 days, with a single 7‑day extension if the device is not reserved by someone else. [chat_equipment_pool]

## q13: Where do I pick up my badge on my first day?
Expected: reception / building a (sources: onboarding_checklist)

**Baseline** (ok=True, 921 tokens): You pick up your badge at the reception in building A. [onboarding_checklist]

**Optimized** (ok=True, 606 tokens): Pick up your badge at the reception in building A, from 08:30. [onboarding_checklist]

## q14: How should I name a new GitLab repository?
Expected: team-project-topic (sources: gitlab_guide)

**Baseline** (ok=True, 753 tokens): Name the repository in the format **team‑project‑topic**, all in lowercase and separated by hyphens (e.g., *photonics-lidar-calibration*). [gitlab_guide]

**Optimized** (ok=True, 562 tokens): Name the repository as `team-project-topic`, all lowercase with hyphens (e.g., `photonics-lidar-calibration`). [gitlab_guide]

## q15: What is the daily meal allowance when I travel abroad?
Expected: 45 (sources: travel_policy)

**Baseline** (ok=True, 751 tokens): The daily meal allowance for traveling abroad is **45 euros**. [travel_policy]

**Optimized** (ok=True, 438 tokens): The daily meal allowance for business travel abroad is 45 euros. [travel_policy]

## q16: How many seats does the auditorium have?
Expected: 120 (sources: meeting_rooms)

**Baseline** (ok=True, 862 tokens): The auditorium in building B has 120 seats. [meeting_rooms]

**Optimized** (ok=True, 613 tokens): The auditorium in building B has 120 seats. [meeting_rooms]

## q17: Which port does the MATLAB license server use?
Expected: 27000 (sources: software_licenses)

**Baseline** (ok=True, 924 tokens): MATLAB’s license server uses port 27000. [software_licenses]

**Optimized** (ok=True, 648 tokens): MATLAB uses the floating license server on port 27000. [software_licenses]

## q18: What do I do with my used lab coat?
Expected: blue bin / friday (sources: wet_lab_ppe)

**Baseline** (ok=True, 784 tokens): Put your used lab coat in the blue bin at the entrance. The laundry service will wash it, and the bin is collected every Friday. [wet_lab_ppe]

**Optimized** (ok=True, 515 tokens): Put it in the blue bin at the entrance. The bin is collected every Friday. [wet_lab_ppe]

## q19: Is there a budget for setting up my home office?
Expected: 300 (sources: remote_work_faq)

**Baseline** (ok=True, 791 tokens): Yes – new employees are entitled to a one‑time home‑office budget of 300 € for items such as a chair, a screen or a headset. [remote_work_faq]

**Optimized** (ok=True, 555 tokens): Yes, new employees can receive a one‑time home‑office budget of 300 € for a chair, a screen or a headset. [remote_work_faq]

## q20: I booked something in KestrelBook, but it is not in my Outlook calendar yet. Is something wrong?
Expected: 15 minutes (sources: booking_release_notes)

**Baseline** (ok=True, 780 tokens): New bookings can take up to 15 minutes to appear in your Outlook calendar. The booking is valid immediately; only the calendar sync is slow. [booking_release_notes]

**Optimized** (ok=True, 471 tokens): New bookings can take up to 15 minutes to appear in your Outlook calendar. The booking is valid immediately; only the calendar sync is slow. [booking_release_notes]

## q21: I'm working from home today and I need the Falcon GPU cluster. Which VPN server and which cluster address do I connect to?  **<- CHANGED**
Expected: vpn.kestrel-lab.example / falcon.kestrel-lab.example (sources: vpn_access, gpu_cluster_tutorial)

**Baseline** (ok=True, 939 tokens): You should connect to the VPN server at **vpn.kestrel‑lab.example** and then SSH into the cluster at **falcon.kestrel‑lab.example**.  
[ vpn_access ] [ gpu_cluster_tutorial ]

**Optimized** (ok=False, 621 tokens): Use the “Kestrel Remote – Full” VPN profile, which gives access to the Falcon GPU cluster.  
Connect to the cluster at `falcon.kestrel-lab.example` via SSH.  
[remote_work_faq] [vpn_access]

## q22: Can I set up a weekly recurring cleanroom booking? For how many weeks, and which training do I need before I can book at all?
Expected: 8 weeks / cr-101 (sources: booking_release_notes, cleanroom_booking)

**Baseline** (ok=True, 1258 tokens): - Yes, you can set up a weekly recurring cleanroom booking for up to **8 weeks**. [booking_release_notes]  
- To book a cleanroom slot, you must have passed the **cleanroom gowning training (course CR‑101)**. [cleanroom_booking]  
- In addition, you must complete the **general safety training** within the first 5 working days before you can enter any laboratory. [onboarding_checklist]

**Optimized** (ok=True, 575 tokens): Yes – you can create a weekly recurring cleanroom booking for up to 8 weeks. Before you can book at all you must complete the cleanroom gowning training (course CR‑101), which is valid for 12 months. [booking_release_notes] [cleanroom_booking]

## q23: I'm new here. When am I allowed to enter the wet lab, and what do I have to wear there?
Expected: safety training / safety glasses (sources: onboarding_checklist, wet_lab_ppe)

**Baseline** (ok=True, 1251 tokens): You may enter the wet lab only after you have finished the mandatory general safety training, which must be completed within the first five working days. [onboarding_checklist]  

In the wet lab you must wear:

- safety glasses  
- a lab coat  
- closed‑toe shoes  
- long trousers  
- nitrile gloves (change them as soon as they become contaminated) [wet_lab_ppe]  

Contact lenses are only allowed if you also wear closed safety goggles. [wet_lab_ppe]

**Optimized** (ok=True, 591 tokens): You may enter the wet lab only after completing the general safety training within your first five working days.  
In the wet lab you must wear safety glasses, a lab coat, closed shoes, long trousers, and nitrile gloves (and avoid touching door handles, keyboards or phones with gloves on).  
[onboarding_checklist] [wet_lab_ppe]

## q24: How many days a week can I work from home, and which VPN profile do I need to use the file shares from there?
Expected: 2 days / full (sources: remote_work_faq, vpn_access)

**Baseline** (ok=True, 878 tokens): You can work from home up to **2 days per week** if your team lead agrees.  
To access the file shares from home you need to use the **“Kestrel Remote – Full”** VPN profile.  

[remote_work_faq]  
[vpn_access]

**Optimized** (ok=True, 572 tokens): You can work from home up to 2 days per week, if your team lead agrees. To access file shares from home you need the “Kestrel Remote – Full” VPN profile. [remote_work_faq] [vpn_access]

## q25: What is the Wi-Fi password for guests?
Expected: should say it is not in the documents (sources: -)

**Baseline** (ok=True, 883 tokens): I couldn't find this in the documentation.

**Optimized** (ok=True, 500 tokens): I couldn't find this in the documentation.

## q26: How many vacation days do new employees get per year?
Expected: should say it is not in the documents (sources: -)

**Baseline** (ok=True, 727 tokens): I couldn't find this in the documentation.

**Optimized** (ok=True, 443 tokens): I couldn't find this in the documentation.

## q27: Can I bring my dog to the office?
Expected: should say it is not in the documents (sources: -)

**Baseline** (ok=True, 743 tokens): I couldn't find this in the documentation.

**Optimized** (ok=True, 516 tokens): I couldn't find this in the documentation.

## q28: How much does parking cost at the lab?
Expected: should say it is not in the documents (sources: -)

**Baseline** (ok=True, 846 tokens): I couldn't find this in the documentation.

**Optimized** (ok=True, 594 tokens): I couldn't find this in the documentation.

## q29: Who is the head of the IT department?
Expected: should say it is not in the documents (sources: -)

**Baseline** (ok=True, 788 tokens): I couldn't find this in the documentation.

**Optimized** (ok=True, 548 tokens): I couldn't find this in the documentation.

## q30: How do I book the 3D printer?
Expected: should say it is not in the documents (sources: -)

**Baseline** (ok=True, 872 tokens): I couldn't find this in the documentation.

**Optimized** (ok=True, 618 tokens): I couldn't find this in the documentation.

