#!/bin/bash

# 激活conda环境

conda activate lf-multi-node

# v2.0.0
# single-node training
#CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 nohup llamafactory-cli train examples/train_lora/v2_0_4.yaml > logs/v2.0.4 2>&1 &

# single-node dpo
# CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 nohup llamafactory-cli train examples/train_lora/qwen2_lora_dpo.yaml > logs/v2.0.3.10_dpo 2>&1 &

# multi-node training
# CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 FORCE_TORCHRUN=1 NNODES=2 RANK=1 MASTER_ADDR=172.19.0.111 MASTER_PORT=29500 nohup llamafactory-cli train examples/train_lora/v2_0_0.yaml > logs/v2.0.0 2>&1 &

# anti-hallucination dpo training - 旧版本（有问题）
# WANDB_DISABLED=true \
# PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:128,expandable_segments:True \
# CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
# FORCE_TORCHRUN=1 \
# NPROC_PER_NODE=8 \
# nohup llamafactory-cli train examples/train_lora/anti_hallucination_dpo.yaml > logs/qwen2.5_32B_anti_hallucination_dpo_debug 2>&1 &

# anti-hallucination dpo training - 成功版本（解决了DeepSpeed CPU Adam问题）
CUDA_HOME=/usr/local/cuda-12.4 \
LD_LIBRARY_PATH=/usr/local/cuda-12.4/lib64:$LD_LIBRARY_PATH \
LIBRARY_PATH=/usr/local/cuda-12.4/lib64:$LIBRARY_PATH \
DS_BUILD_CPU_ADAM=0 \
DS_BUILD_FUSED_ADAM=0 \
WANDB_DISABLED=true \
PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:128,expandable_segments:True \
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
FORCE_TORCHRUN=1 \
NPROC_PER_NODE=8 \
nohup llamafactory-cli train examples/train_lora/anti_hallucination_dpo.yaml > logs/qwen2.5_32B_anti_hallucination_dpo_success 2>&1 &

