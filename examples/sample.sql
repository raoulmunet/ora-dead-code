CREATE OR REPLACE PROCEDURE demo_dead_code AS
  v_used NUMBER;
  v_unused VARCHAR2(20);
BEGIN
  v_used := 10;
  DBMS_OUTPUT.PUT_LINE(v_used);
  RETURN;
  DBMS_OUTPUT.PUT_LINE('candidate unreachable');
END;
/
