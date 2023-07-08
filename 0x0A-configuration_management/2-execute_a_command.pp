# kills a process named killmenow using puppet
exec {'pkill killmenow':
  path     => '/alx-system_engineering-devops/0x0A-configuration_management',
  provider => shell
}
