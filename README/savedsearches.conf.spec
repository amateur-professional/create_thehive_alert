# create_thehive_alert alert settings

action.create_thehive_alert = [0|1]
* Enable thehive_create_case notification

action.create_thehive_alert.param.URL = <string>
* URL of theHive instance. 
* (required)

action.create_thehive_alert.param.caseTemplate = <string>
* The case template to use for imported alerts.
* Defaults to "default"
* (required)

action.create_thehive_alert.param.type = <string>
* Alert type. Defaults to "alert"
* (required)

action.create_thehive_alert.param.source = <string>
* Alert source. Defaults to "Splunk"
* (required)

action.create_thehive_alert.param.sourceRefField = <string>
* Field name that contains a unique identifier specific to the source event.
* (required)

action.create_thehive_alert.param.dateField = <string>
* Field name that contains an epochtime for the alert time. 
* (required)

action.create_thehive_alert.param.ignoredFields = <string>
* List of field names to not include in the alerts.
* (optional)

action.create_thehive_alert.param.title = <string>
* Alert Title to use in theHive. 
* (required)

action.create_thehive_alert.param.description = <string>
* The description of the alert to send to theHive.
* (required)

action.create_thehive_alert.param.tags = <string>
* The tags to put on the alert. Use a single, comma-separated string (ex. "badIP,trojan").
* (optional)

action.create_thehive_alert.param.severity = [0|1|2|3]
* The severity of the new alert. 1 = low, 2 = medium, 3 = high
* Default is "2" (medium)
* (optional)

action.create_thehive_alert.param.tlp = [-1|0|1|2|3]
* Traffic Light Protocol for this alert. 0 = White, 1 = Green, 2 = Amber, 3 = Red
* TLP affects releasability of information. Some analyzers will not be available on higher TLP settings.
* Defaults to "-1" (unset)
* (optional)