#!/usr/bin/env bash
# using Puppet to connect without typing a password
file_line { 'Identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}
file_line { 'disable password login':
    path    => '/etc/ssh/ssh_config',
    line    => 'PasswordAuthentication no',
}
