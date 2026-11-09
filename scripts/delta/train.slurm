#!/bin/bash
# ------------------------------------------------------------------
# Generalist Robotics — LeRobot training job template for NCSA Delta
#
# EVERY value marked VERIFY must be checked against current Delta docs:
#   https://docs.ncsa.illinois.edu/systems/delta/
# Never put tokens or passwords in this file. It is committed to git.
#
# Submit:   sbatch scripts/delta/train.slurm
# Status:   squeue -u $USER
# Cancel:   scancel <jobid>
# ------------------------------------------------------------------
#SBATCH --job-name=gr-train
#SBATCH --account=REPLACE_ALLOCATION_ACCOUNT   # VERIFY: our allocation's account name
#SBATCH --partition=REPLACE_GPU_PARTITION      # VERIFY: current GPU partition name
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=1                      # VERIFY: how Delta wants GPUs requested
#SBATCH --cpus-per-task=8                      # VERIFY: sensible for data loading
#SBATCH --mem=64G                              # VERIFY
#SBATCH --time=04:00:00                        # VERIFY: max walltime on the partition
#SBATCH --output=logs/%x-%j.out
#SBATCH --error=logs/%x-%j.err

set -euo pipefail
mkdir -p logs

echo "Job $SLURM_JOB_ID on $(hostname) at $(date)"
nvidia-smi || true

# --- Environment ---------------------------------------------------
# VERIFY: the module names / env activation we actually use on Delta.
# module load REPLACE_MODULES
# source activate REPLACE_ENV   (or: source .venv/bin/activate)

# Hugging Face auth: log in once on Delta beforehand, or export HF_TOKEN
# from a file that is NOT in this repo. Never paste the token here.

# --- Run config (copy these values into the experiment page) -------
EXPERIMENT_ID="EXP-000"                  # matches docs/experiments/
DATASET_ID="REPLACE_ORG/REPLACE_DATASET" # Hugging Face dataset repo
OUTPUT_DIR="REPLACE_OUTPUT_DIR/${EXPERIMENT_ID}"   # VERIFY: scratch vs project storage

echo "Experiment: $EXPERIMENT_ID  Dataset: $DATASET_ID  Output: $OUTPUT_DIR"
python -c "import lerobot, sys; print('lerobot', getattr(lerobot, '__version__', 'unknown'), 'python', sys.version)"

# --- Training -------------------------------------------------------
# INSERT VERIFIED COMMAND: the exact LeRobot training command for our
# pinned version, using $DATASET_ID and $OUTPUT_DIR.
echo "Replace this line with the verified training command." >&2
exit 1

echo "Finished at $(date)"
