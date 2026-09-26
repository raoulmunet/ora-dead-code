from __future__ import annotations
from dataclasses import dataclass,asdict
import re

@dataclass(frozen=True)
class Finding:
    rule:str
    line:int
    symbol:str|None
    message:str
    confidence:str="candidate"
    def to_dict(self): return asdict(self)

def analyze(plsql:str)->list[Finding]:
    out=[]
    decl=re.search(r"\b(?:IS|AS)\b(.*?)\bBEGIN\b",plsql,re.I|re.S)
    if decl:
        start=decl.start(1)
        for m in re.finditer(r"^\s*([A-Za-z][\w$#]*)\s+(?:CONSTANT\s+)?(?:NUMBER|VARCHAR2|CHAR|DATE|TIMESTAMP|BOOLEAN|PLS_INTEGER|BINARY_INTEGER)\b",decl.group(1),re.I|re.M):
            name=m.group(1)
            total=len(re.findall(rf"\b{re.escape(name)}\b",plsql,re.I))
            if total==1:
                pos=start+m.start(1)
                out.append(Finding("UNUSED_VARIABLE",plsql.count("\n",0,pos)+1,name,"Declared variable has no other textual reference."))
    local=[]
    for m in re.finditer(r"\b(?:PROCEDURE|FUNCTION)\s+([A-Za-z][\w$#]*)\b",plsql,re.I):
        local.append((m.group(1),m.start(1)))
    for name,pos in local:
        uses=len(re.findall(rf"\b{re.escape(name)}\b",plsql,re.I))
        if uses==1:
            out.append(Finding("UNUSED_LOCAL_ROUTINE",plsql.count("\n",0,pos)+1,name,"Local routine declaration has no other textual reference."))
    for m in re.finditer(r"\b(RETURN|RAISE)\s*;([^\n;]*(?:;|\n))",plsql,re.I):
        tail=m.group(2).strip()
        if tail and not re.match(r"^(END|EXCEPTION|ELSE|ELSIF|WHEN)\b",tail,re.I):
            pos=m.start(2)
            out.append(Finding("UNREACHABLE_CANDIDATE",plsql.count("\n",0,pos)+1,None,f"Text follows unconditional {m.group(1).upper()}; review reachability."))
    return sorted(out,key=lambda x:(x.line,x.rule))
