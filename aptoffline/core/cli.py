import click


VERSION = '1.5'


@click.group()
@click.option('--verbose', '-v', is_flag=True, help="Enable Verbosity")
@click.version_option(VERSION, prog_name='apt-offline')
def cli(verbose):
    if verbose:
        click.echo('Verbosity selected')


@cli.command('set',
             help='''generates a signature file with the data required to
             install on or update the disconnected machine''')
@click.option('--install-packages', nargs='*', type=click.STRING,
              help='Packages that need to be installed', required=False,
              metavar="SRC_PKG")
@click.option('--install-src-packages', nargs='*', type=click.STRING,
              help='Source packages that need to be insalled', required=False,
              metavar='PKG')
@click.option('--src-build-dep', is_flag=True,
              help='''
              Download Build Dependency packages for the
              source packages requested''', required=False)
@click.option('--release',
              type=click.Choice(['stable', 'testing', 'unstable']),
              required=False, help='Release target to install packages')
@click.option('--update', is_flag=True, required=False,
              help='''Generate APT database signature for an update,
              equivalanet of running apt-get update''')
@click.option('--update', is_flag=True, required=False,
              help='''Generate APT Database signature for package upgrade,
              equivalanet of running apt-get upgrade''')
@click.option('--upgrade-type', required=False,
              type=click.Choice(['upgrade', 'dist-upgrade',
                                 'dselect-upgrade']),
              help='Type of upgrade you would like to perform,\
              default is upgrade.', default='upgrade')
@click.argument('filename', type=click.File('wb'), required=True)
def setter(install_packages, install_src_packages, src_build_dep, rlease,
           update, upgrade, upgrade_type, filename):
    pass


@cli.command('get')
@click.option('--download-dir', '-d', type=click.Path(exists=True,
                                                      writable=True),
              required=False, help='''Directory for downloading
              the packages''', metavar='DIR_NAME')
@click.option('--cache-dir', '-s', type=click.Path(exists=True),
              required=False,
              help='Package cache directory to look for before downloading',
              metavar='DIR_NAME')
@click.option('--socket-timeout', help='Set socket timeout', default=30)
@click.option('--no-checksum', required=False, is_flag=True,
              help='Disable checksum verification of each download file\
              (discouraged)')
@click.option('--threads', '-t', required=False, default=1, type=click.INT,
              help='Number of threads to spawn for downloading')
@click.option('--bundle', required=False, type=click.File('rb'),
              help='Create an archive file in zip format', metavar='FILENAME')
@click.option('--bug-report', is_flag=True, required=False,
              help='Download the bug reports for packages being downloaded')
@click.option('--proxy-host', required=False, help='Proxy Host',
              metavar='PROXY_HOST')
@click.option('--proxy-port', required=False, help='Proxy Port',
              metavar='PROXY_PORT')
@click.argument('filename', type=click.Path(exists=True), required=True)
def fetcher():
    pass


@cli.command('install')
@click.option('--skip-bug-reports', required=False, is_flag=True,
              help='Skip listing downloaded bug reports if any')
@click.option('--install-src-path', required=False,
              type=click.Path(exists=True, writable=True),
              help='Path for installing source packages downloaded')
@click.option('--allow-unauthenticated', required=False, is_flag=True,
              help='Do not verify GPG signature on packages to be\
              installed to APT (discouraged)')
@click.argument('archive', type=click.Path(exists=True), required=True)
def installer(skip_bug_reports, install_src_path, allow_unauthenticated,
              archive):
    pass
