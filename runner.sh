#!/bin/bash

uvicorn src:app --reload --proxy-headers --limit-concurrency 100 --workers 5 --host 0.0.0.0 --port 8000