class web_static_setup {
    # Ensure /data/ directory exists
    file { '/data':
        ensure => directory,
        owner  => 'ubuntu',
        group  => 'ubuntu',
        mode   => '0755',
    }

    # Ensure /data/web_static/ exists
    file { '/data/web_static':
        ensure => directory,
        owner  => 'ubuntu',
        group  => 'ubuntu',
        mode   => '0755',
        require => File['/data'],
    }

    # Ensure /data/web_static/releases/ exists
    file { '/data/web_static/releases':
        ensure => directory,
        owner  => 'ubuntu',
        group  => 'ubuntu',
        mode   => '0755',
        require => File['/data/web_static'],
    }

    # Ensure /data/web_static/shared/ exists
    file { '/data/web_static/shared':
        ensure => directory,
        owner  => 'ubuntu',
        group  => 'ubuntu',
        mode   => '0755',
        require => File['/data/web_static'],
    }

    # Ensure /data/web_static/releases/test/ exists
    file { '/data/web_static/releases/test':
        ensure => directory,
        owner  => 'ubuntu',
        group  => 'ubuntu',
        mode   => '0755',
        require => File['/data/web_static/releases'],
    }

    # Create a test index.html file
    file { '/data/web_static/releases/test/index.html':
        ensure  => file,
        content => "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n",
        owner   => 'ubuntu',
        group   => 'ubuntu',
        mode    => '0644',
        require => File['/data/web_static/releases/test'],
    }

    # Ensure the symbolic link /data/web_static/current exists
    file { '/data/web_static/current':
        ensure => link,
        target => '/data/web_static/releases/test',
        require => File['/data/web_static/releases/test'],
    }
}

include web_static_setup
