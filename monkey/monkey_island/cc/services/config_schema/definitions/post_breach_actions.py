POST_BREACH_ACTIONS = {
    "title": "Post breach actions",
    "description": "Runs scripts/commands on infected machines. These actions safely simulate what an adversary"
                   "might do after breaching a new machine. Used in ATT&CK and Zero trust reports.",
    "type": "string",
    "anyOf": [
        {
            "type": "string",
            "enum": [
                "BackdoorUser"
            ],
            "title": "Back door user",
            "info": "Attempts to create a new user on the system and delete it afterwards.",
            "attack_techniques": ["T1136"]
        },
        {
            "type": "string",
            "enum": [
                "CommunicateAsNewUser"
            ],
            "title": "Communicate as new user",
            "info": "Attempts to create a new user, create HTTPS requests as that user and delete the user "
                    "afterwards.",
            "attack_techniques": ["T1136"]
        },
        {
            "type": "string",
            "enum": [
                "ModifyShellStartupFiles"
            ],
            "title": "Modify shell startup files",
            "info": "Attempts to modify shell startup files, like ~/.profile, ~/.bashrc, ~/.bash_profile "
                    "in linux, and profile.ps1 in windows. Reverts modifications done afterwards.",
            "attack_techniques": ["T1156", "T1504"]
        },
        {
            "type": "string",
            "enum": [
                "HiddenFiles"
            ],
            "title": "Hidden files and directories",
            "info": "Attempts to create a hidden file and remove it afterward.",
            "attack_techniques": ["T1158"]
        },
        {
            "type": "string",
            "enum": [
                "TrapCommand"
            ],
            "title": "Trap",
            "info": "On Linux systems, attempts to trap an interrupt signal in order to execute a command "
                    "upon receiving that signal. Removes the trap afterwards.",
            "attack_techniques": ["T1154"]
        },
        {
            "type": "string",
            "enum": [
                "ChangeSetuidSetgid"
            ],
            "title": "Setuid and Setgid",
            "info": "On Linux systems, attempts to set the setuid and setgid bits of a new file. "
                    "Removes the file afterwards.",
            "attack_techniques": ["T1166"]
        },
        {
            "type": "string",
            "enum": [
                "ScheduleJobs"
            ],
            "title": "Job scheduling",
            "info": "Attempts to create a scheduled job on the system and remove it.",
            "attack_techniques": ["T1168", "T1053"]
        }
    ]
}
