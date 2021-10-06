# YADRO OpenBmc Ansible Collection

## Modules tree

```yml
yadro:
  obmc:
    bmc:
      - yadro.obmc.bmc_user
      - yadro.obmc.bmc_time
      - yadro.obmc.bmc_reset
      - yadro.obmc.bmc_reset_to_defaults
      network:
        - yadro.obmc.bmc_network_interfaces
        interface:
          - yadro.obmc.bmc_network_interface_info
          - yadro.obmc.bmc_network_interface
      firmware:
        - yadro.obmc.bmc_firmware_info
        - yadro.obmc.bmc_firmware
    bios:
      - yadro.obmc.bios_reset_to_defaults
      firmware:
        - yadro.obmc.bios_firmware_info
        - yadro.obmc.bios_firmware
    system:
      - yadro.obmc.system_info
      power:
        - yadro.obmc.system_power_info
        - yadro.obmc.system_power_state
      thermal:
        - yadro.obmc.system_thermal_info
      boot:
        - yadro.obmc.system_boot_info
```
