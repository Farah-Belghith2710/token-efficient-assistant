# Tutorial: running jobs on the Falcon GPU cluster
Source: Research Computing tutorials - last edited 21 Aug 2026

## Logging in
Falcon can only be reached from inside the lab network, or through the VPN with the Full profile. Log in with:
ssh your-username@falcon.kestrel-lab.example

## Partitions and time limits
Jobs are submitted with SLURM. There are two GPU partitions:
- gpu-short: for jobs up to 4 hours. This is the default partition.
- gpu-long: for jobs up to 48 hours. Longer jobs are stopped automatically, so save checkpoints.
Each user can use at most 2 GPUs at the same time.

## A minimal job script
Save these lines as job.sh and submit the file with "sbatch job.sh":
#SBATCH --partition=gpu-short
#SBATCH --gres=gpu:1
#SBATCH --time=02:00:00
python train.py

## Where to store files
Your home folder has 50 GB and is backed up. Each project also gets 2 TB on /scratch, which is fast but not backed up: files older than 30 days are deleted automatically. Copy the results you want to keep to the project share.
