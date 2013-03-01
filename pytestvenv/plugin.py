import os, py, pytest


# command line options
def pytest_addoption(parser):
    cwd = os.getcwd()
    group = parser.getgroup(
        "virtualenv", "create a virtual environment to run the tests in")
    group._addoption('--virtualenv',
        action="store_true",
        dest="virtualenv",
        default=False,
        help="use a virtual enviroment. defaults to False.")
    group._addoption('--setup',
        action="store_true",
        dest="setup",
        default=False,
        help="use setup.py to install AUT")
    group._addoption('--setup-file',
        action="store",
        dest="setup_file",
        default=os.path.join(cwd, "setup.py"),
        help="provide a path to setup file (default: setup.py in current directory")
    group._addoption('--pip',
        action="store_true",
        dest="pip",
        default=False,
        help="use pip to install requirements")
    group._addoption('--requirements-file',
        action="store",
        dest="requirements_file",
        default=os.path.join(cwd, "requirements.txt"),
        help="provide a path to requirements file (default: requirements.txt in current directory")


class VirtualEnv:

    def pytest_plugin_registered(self, plugin):
        if self.config.option.traceconfig:
            msg = "PLUGIN registered: %s" %(plugin,)
            # XXX this event may happen during setup/teardown time
            #     which unfortunately captures our output here
            #     which garbles our output if we use self.write_line
            self.write_line(msg)

    # sanity for command line options
    def check_options(config):
        val = config.getvalue
        if not val("collectonly"):
            if config.option.virtualenv:
                if not config.option.setup or config.option.pip:
                    msg = "--virtualenv requires either --setup or --pip to configure the environemnt"
                    raise pytest.UsageError(msg)
                #@@@ add check for xdist here


    # set up virtual environment
    def pytest_configure(config):
        if config.option.virtualenv:
            # create folder for virtual environment
            self.tmpdir = py.path.local.make_numbered_dir(prefix='pytest-env-')
            # create virtual environment
            os.system("virtualenv %s" % self.tmpdir)
            # activate virtual environment
            py.std.sys.path.insert(0, str(self.tmpdir))

            if config.option.setup:
                # run setup
                os.system("python %s install" % config.option.setup_file)

            if config.option.pip:
                # pip install requirements
                os.system("pip install -r %s" % config.option.requirements_file)


    # tear down virtual environment
    def pytest_unconfigure(config):
        if config.option.virtualenv:
            # deactivate environment
            py.std.sys.path.remove(str(self.tmpdir))
            # delete environment folder
            os.path.rmdir(str(self.tmpdir))
