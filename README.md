place the folder gitlabbackupper in /opt so it becomes
/opt/gitlabbackupper/backup.py and reown the directory recursively for your user
chown -R /opt/gitlabbackupper user:user
copy the cron line to your crontab (crontab -e)
a user does not need to be logged on for a cron to execute.
you can at all times check what projects are being backed up by reading the projectslugs.txt file.
please note, you need to replace the token every so often, first of all because of best practice.
Secundary because when the token expires, the projectslugs.txt file will truncate to size 0b.
shortly, it won't backup your git

then a more interesting feature, all your repo's main branches will be mirrored to the clones dir. this allows for easy migration from one gitlab to another instance, or in case of disaster recovery, the same instance, and only requires the right base url, and ssh key for the user that will perform the migration.

I know there are native solututions for this built in to gitlab, but I do not rock certificates, so they refused to work for me.
Before you ask, yeah some AI assistance was used in reviewing the code.
