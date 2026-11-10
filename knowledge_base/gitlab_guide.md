# Using the internal GitLab
Source: Developer documentation repository - last edited 9 Sep 2026

## Access
GitLab runs at gitlab.kestrel-lab.example and can only be reached from the lab network or through the VPN with the Full profile. Log in with your lab account.

## SSH keys
Add an SSH key under Preferences > SSH Keys. We recommend ed25519 keys.

## Naming and branches
Name repositories as team-project-topic, in lowercase with hyphens, for example photonics-lidar-calibration. The main branch is protected: changes go through a merge request, which needs one approval from another person and a passing CI pipeline.

## Large files
Do not commit files larger than 100 MB directly. Use Git LFS for large files, and keep datasets on the project share instead of in Git.
