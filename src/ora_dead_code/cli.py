from __future__ import annotations
import argparse,json
from pathlib import Path
from .core import analyze

def main(argv=None):
    p=argparse.ArgumentParser(description="Find PL/SQL dead-code candidates.")
    p.add_argument("source")
    p.add_argument("--format",choices=("text","json"),default="text")
    a=p.parse_args(argv)
    f=analyze(Path(a.source).read_text(encoding="utf-8"))
    if a.format=="json": print(json.dumps([x.to_dict() for x in f],indent=2))
    else:
        for x in f: print(f"line {x.line} {x.rule} {x.symbol or ''} — {x.message}")
    return 1 if f else 0
if __name__=="__main__": raise SystemExit(main())
