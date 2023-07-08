#creates the file school in /tmp with the given specifications

file {'school' :
  ensure  => present,
  path    => '/tmp/school',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data'
}
