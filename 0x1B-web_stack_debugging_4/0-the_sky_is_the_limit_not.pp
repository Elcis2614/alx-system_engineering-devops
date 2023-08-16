#Increasing the request load
exec {'inc_load':
  command => "sed -i 's/^worker_processes.*/worker_processes 8/' nginx.conf",
  cwd => "/etc/ngninx/",
  provider => shell
}
exec {'restart_nginx':
  command => "service nginx restart",
  provider => shell
}
