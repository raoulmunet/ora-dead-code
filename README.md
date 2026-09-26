# ora-dead-code

[![tests](https://github.com/raoulmunet/ora-dead-code/actions/workflows/tests.yml/badge.svg)](https://github.com/raoulmunet/ora-dead-code/actions/workflows/tests.yml) ![Python](https://img.shields.io/badge/Python-3.10--3.13-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Find conservative **dead-code candidates** in Oracle PL/SQL.

> **Oracle compatibility**
>
> | Oracle version | Support |
> |---|---|
> | Oracle Database 19c | ✅ Common PL/SQL syntax |
> | Oracle Database 23ai | ✅ Common PL/SQL syntax |
> | Oracle AI Database 26ai | ✅ Common PL/SQL syntax |
>
> Findings are candidates for review, not compiler-equivalent proofs.

## Checks

- locally declared variables referenced only in their declaration;
- locally declared procedures/functions that appear never to be called;
- obvious statements after an unconditional `RETURN;` or `RAISE;` before the enclosing terminator.

## Usage

```bash
python -m pip install "git+https://github.com/raoulmunet/ora-dead-code.git"

ora-dead-code examples/sample.sql
ora-dead-code examples/sample.sql --format json
```

Example:

```text
line 3 UNUSED_VARIABLE v_unused — declared but no later reference was found
line 8 UNREACHABLE_CANDIDATE — statement follows unconditional RETURN
```

## Why “candidate”?

PL/SQL permits constructs that are difficult to model safely with a tiny offline analyzer. Rather than overclaim, this tool labels findings that deserve human review.

## Oracle Dev Tools family

This repository is part of the **Oracle Dev Tools** suite: small, composable developer utilities designed around Oracle Database 19c, 23ai and 26ai.

| Area | Tools |
|---|---|
| Foundation | [ora-core](https://github.com/raoulmunet/ora-core) |
| SQL analysis | [ora-impact](https://github.com/raoulmunet/ora-impact) · [ora-plan](https://github.com/raoulmunet/ora-plan) · [ora-lineage](https://github.com/raoulmunet/ora-lineage) · [ora-lint](https://github.com/raoulmunet/ora-lint) · [ora-sql-diff](https://github.com/raoulmunet/ora-sql-diff) · [ora-sql-complexity](https://github.com/raoulmunet/ora-sql-complexity) · [ora-join-viz](https://github.com/raoulmunet/ora-join-viz) · [ora-bind](https://github.com/raoulmunet/ora-bind) |
| Data & operations | [ora-doc](https://github.com/raoulmunet/ora-doc) · [ora-data-quality](https://github.com/raoulmunet/ora-data-quality) · [ora-csv-loader](https://github.com/raoulmunet/ora-csv-loader) · [ora-etl-log](https://github.com/raoulmunet/ora-etl-log) · [ora-migration-check](https://github.com/raoulmunet/ora-migration-check) · [ora-errors](https://github.com/raoulmunet/ora-errors) · [ora-schema-explorer](https://github.com/raoulmunet/ora-schema-explorer) |
| PL/SQL analysis | [ora-exception-flow](https://github.com/raoulmunet/ora-exception-flow) · [ora-call-graph](https://github.com/raoulmunet/ora-call-graph) · [ora-dead-code](https://github.com/raoulmunet/ora-dead-code) |

## License

MIT.
