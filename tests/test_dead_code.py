from ora_dead_code import analyze

def test_unused_variable():
    sql="""CREATE OR REPLACE PROCEDURE p AS
  v_used NUMBER;
  v_unused NUMBER;
BEGIN
  v_used := 1;
  DBMS_OUTPUT.PUT_LINE(v_used);
END;"""
    f=analyze(sql)
    assert any(x.rule=="UNUSED_VARIABLE" and x.symbol.lower()=="v_unused" for x in f)
