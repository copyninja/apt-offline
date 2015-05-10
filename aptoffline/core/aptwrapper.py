import os
from subprocess import check_output, CalledProcessError

PYTHON_APT = True

try:
    import apt
    import apt_pkg
except ImportError:
    PYTHON_APT = False

SUPPORTED_PLATFORM = ['Linux', 'GNU/kFreeBSD', 'GNU']
APT_UPDATE_PARTIAL_PATH = '/var/lib/apt/lists/partial'
APT_UPDATE_LIST_PATH = '/var/lib/apt/lists'
APT_PACKAGE_ARCHIVE_PATH = '/var/cache/apt/archives'

APT_LIST_LOCK = os.path.join(APT_UPDATE_LIST_PATH, 'lock')
APT_PACKAGE_LOCK = os.path.join(APT_PACKAGE_ARCHIVE_PATH, 'lock')

UPDATE_PROCESS = ['update', 'upgrade', 'dist-upgrade',
                  'dselect-upgrade']


class AptCmdWrapper(object):
    '''
       Wrapper around the apt routines. This class tries to use
       python-apt package where  possible, in other places it relies
       on apt-get or aptitude.

       :param outfile:
       :param simulate: Set this to true if you just want to simulate
       the operation
       :param type: Possible values are python-apt, apt-get or
       aptitude. Tells the class to use selected tool for doing its
       operation on APT database.
    '''

    def __int__(self, outfile, simulate=False, type='python-apt'):
        self.outfile = outfile
        self.simulate = simulate
        self.type = type
        self.aptcmd = ['apt-get', '-q', '--print-urls']

    def _check_release(self, release):
        cmd = self.aptcmd
        if release:
            cmd.append(' '.join(['-t', release]))

        return cmd

    def _apt_get(self, operation, release=None, build_dep=False, packages=[]):
        if self.simulate:
            return

        cmd = self._check_release(release)
        if operation in UPDATE_PROCESS:
            # Setting -t release doesn't sound sensible for
            # update/upgrade/dist-upgrade and dselect-upgrade process.
            cmd = self._check_release(None)
            try:
                cmd.append(operation)
                op = check_output(cmd)
                with open(self.outfile, 'ab') as fd:
                    fd.write(op)
            except CalledProcessError:
                # TODO: write whatever needs to be done on command
                #      failure
                pass
        elif operation == 'install':
            cmd.append(operation)
            try:
                op = check_output(cmd)
                with open(self.outfile, 'ab') as fd:
                    fd.write(op)
            except CalledProcessError:
                # TODO: do error processing here
                pass
        elif operation == 'source':
            cmd.append(operation)
            try:
                op = check_output(cmd)
                with open(self.outfile, 'ab') as fd:
                    fd.write(op)
            except CalledProcessError:
                # TODO: Add error handing here
                pass

            if build_dep:
                try:
                    op = check_output(self._check_release(release).append(
                        'build-dep'))
                    with open(self.outfile, 'ab') as fd:
                        fd.write(op)
                except CalledProcessError:
                    # TODO: Add error handling here
                    pass


class PythonAptWrapper(object):
    '''
       Wrapper class around python-apt
    '''

    def __init__(self, release='stable', ):
        # Shall we set the release information here and will it work?
        apt_pkg.config.set('APT::Default-Release', release)
        self._cache = apt.Cache()

    def update(self):
        pass
