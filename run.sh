#!/bin/bash
TF_CPP_MIN_LOG_LEVEL=3 python3 predict_reimbursement.py "$@" 2>/dev/null
