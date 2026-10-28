# Network Automation Lab

## Objective
Learn network automation using Python, Ansible and GitHub.

## Topics
- Cisco Routing and Switching
- Python for Network Automation
- Ansible for Network Automation
- Network Device Configuration Backup
- Network Troubleshooting
- Lab Environment: GNS3

## Learning Goals
- Collect show command outputs from Cisco routers and switches.
- Automate configuration backups.
- Save lab files and scripts in GitHub.
- Practice network automation step by step.

## Current lab structure
- `inventory/` contains the device inventory
- `playbooks/` contains Ansible tasks for connectivity and fact collection
- `ansible.cfg` provides default inventory and SSH settings
- `group_vars/all.yml` stores common Ansible variables

## Next lab tasks
1. Verify host reachability with `ping_devices.yml`
2. Collect basic facts with `show_facts.yml`
3. Extend the playbooks for Cisco command output and config backup