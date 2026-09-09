"""MCP Server for LUP Factorization Skill."""
import json
import sys
from client import LUPFactorization

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "lup_factorize",
                            "description": "Compute LU decomposition with partial pivoting (PA = LU)",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "matrix": {
                                        "type": "array",
                                        "items": {"type": "array", "items": {"type": "number"}}
                                    }
                                },
                                "required": ["matrix"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                L, U, P = LUPFactorization.factorize(args["matrix"])
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps({"L": L, "U": U, "P": P})}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
