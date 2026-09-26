# ora-dead-code

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

## License

MIT.
