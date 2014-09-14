#AWS snapshot tool

A simple command line tool to for taking and managing AWS volumes and
snapshots.  Used for managing AWS backups and managing the snapshot lifecyle.

###Configurtion

You will need to create a default config in the root of this directory called
`.config` with your AWS account info.

similar to the following:

```
region = us-west-1
aws_access_key_id = xxx
aws_secret_access_key = xxx
owner_id = xxx 
```

Where `region` is the default region to use for this tool, `aws_access_key_id`
is the ID for the specific user that will interface with AWS,
`aws_secret_access_key` is the associated key for the ID and `owner_id` is the associated
AWS account that contains the snapshots and volumes to work with.

This config can be overriden on the command line by passing the `-c` or
`--config` flags to the tool.  By default the config is expected to be placed
in the root of this project in a file called `.config`.

**Note** You can obtain your AWS owner_id by navigating to the AWS management console,
selecting your user account then `My Account`.  Under account settings there
should be an `Account ID` which corresponds to the owner ID.

###Usage


