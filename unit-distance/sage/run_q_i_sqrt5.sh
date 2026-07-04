#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SAGE_BIN="/Users/gpeyre/miniconda3/envs/unit-distance-sage/bin/sage"
SCRIPT="unit-distance/sage/q_i_sqrt5_openai_prototype.sage"

export DOT_SAGE="$ROOT_DIR/unit-distance/.sage"
export IPYTHONDIR="$ROOT_DIR/unit-distance/.ipython"

ARGS_JSON=$(python3 - "$@" <<'PY'
import json
import sys

argv = ["q_i_sqrt5_openai_prototype.sage"] + sys.argv[1:]
print(json.dumps(argv))
PY
)

"$SAGE_BIN" -c "import sys; sys.argv=${ARGS_JSON}; load('${SCRIPT}'); main()"
