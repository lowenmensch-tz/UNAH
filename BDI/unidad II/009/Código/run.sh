clear 
mysql -t -v -uadmin -padmin < 0_tables.sql
mysql -t -v -uadmin -padmin < 1_storeProcedures.sql
mysql -t -v -uadmin -padmin < 2_triggers.sql
mysql -t -v -uadmin -padmin < 3_run.sql