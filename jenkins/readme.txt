This is for linux server

This is used to automatically compare cron file with its backup file and send an email notification about the changes using jenkins.

*Place check.sh in jenkins server(which contains sand.txt(ip of servers to ssh and to execute python file))
*Place contents of jenkins_exec_shell.txt in exec_shell of jenkins)
*Place contents of groovy_email_notify.txt in advanced settings of email notification in jenkins) 