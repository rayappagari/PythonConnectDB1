import teradata
udaExec = teradata.UdaExec (appName="PrintTableRows", version="1.0",logConsole=False) 
with udaExec.connect("${dataSourceName}") as session: 
    for row in session.execute("SELECT * FROM ${table}"):
        print(row)