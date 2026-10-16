# Remediation for TASK-b609ab0df93e

## Context
Listener event ingested encrypted SNS FIFO topic `testqa-10.fifo`
(`arn:aws:sns:us-east-1:036376663423:testqa-10.fifo`).

Investigation TASK-b609ab0df93e also reviewed memory-space SNS inventory
and found **16 of 26** topics unencrypted.

## Required action
Enable AWS SNS server-side encryption (`KmsMasterKeyId`) on every
unencrypted topic listed below. Prefer a customer-managed CMK with
rotation enabled.

### Unencrypted topics (16)
- DataFetch-staging (us-east-2 / 480805696776)
- dynamodb (us-east-1 / 480805696776)
- billing-alert (us-east-1 / 480805696776)
- TestInsufficiant (us-east-1 / 480805696776)
- DataFetch (us-east-1 / 480805696776)
- dynamodb (eu-west-1 / 480805696776)
- dynamodb (eu-west-2 / 480805696776)
- user-updates-topic.fifo (ap-south-1 / 480805696776)
- testing-inspector (ap-south-1 / 480805696776)
- VFTraining (ap-south-1 / 480805696776)
- autobotAI-Notifications-live-testqa-autoboti-buil (ap-south-1 / 003678937483)
- autobotAI-Notifications (us-east-1 / 023425967463)
- NotificationsTopic (ap-south-1 / 023425967463)
- autobotai-workshop-guardduty-topic (ap-south-1 / 654654241291)
- autobotAI-Notifications-test-ugradeworkspce (ap-south-1 / 654654241291)
- autobotAI-Notifications-live-testqa-aug18-change (ap-south-1 / 654654241291)

## Additional findings
- AbuseIPDB 2.2.2.2: score 10, US, Oracle America Inc., 2 reports, not whitelisted.
- employeeinformation: 90 rows, 6 duplicate names.
- CISA KEV: 1,524 CVEs; ransomware Known 310 / Unknown 1,214; Microsoft 361.

## Linked ticket
https://github.com/testintern89/delete/issues/33
