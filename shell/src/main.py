# -*- coding: utf-8 -*-

#   Copyright (c) 2010-2014, MIT Probabilistic Computing Project
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import argparse
import os

import bayeslite
import bayeslite.crosscat
import bayeslite.shell.core as shell
import bayeslite.shell.hook as hook


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('bdbpath', type=str, nargs='?', default=':memory:',
                        help="bayesdb database file")
    parser.add_argument('-j', '--njob', type=int, default=0,
                        help="Max number of jobs (processes) useable.")
    parser.add_argument('-s', '--seed', type=int, default=None,
                        help="Random seed for the default generator.")
    parser.add_argument('-f', '--file', type=str, nargs="+", default=None,
                        help="Path to commands file. May be used to specify a "
                        "project-specific init file.")
    parser.add_argument('--batch', action='store_true',
                        help="Exit after executing file specified with -f.")
    parser.add_argument('--debug', action='store_true', help="For unit tests.")
    parser.add_argument('--no-init-file', action='store_true',
                        help="Do not load ~/.bayesliterc")

    args = parser.parse_args(argv)
    return args


def run(stdin, stdout, stderr, argv):
    args = parse_args(argv[1:])
    bdb = bayeslite.bayesdb_open(pathname=args.bdbpath)

    if args.njob != 1:
        import crosscat.MultiprocessingEngine as ccme
        njob = args.njob if args.njob > 0 else None
        crosscat = ccme.MultiprocessingEngine(seed=args.seed, cpu_count=njob)
    else:
        import crosscat.LocalEngine as ccle
        crosscat = ccle.LocalEngine(seed=args.seed)
    metamodel = bayeslite.crosscat.CrosscatMetamodel(crosscat)
    bayeslite.bayesdb_register_metamodel(bdb, metamodel)
    bdbshell = shell.Shell(bdb, 'crosscat', debug=args.debug)
    with hook.set_current_shell(bdbshell):
        if not args.no_init_file:
            init_file = os.path.join(os.path.expanduser('~/.bayesliterc'))
            if os.path.isfile(init_file):
                bdbshell.dot_read(init_file)

        if args.file is not None:
            for path in args.file:
                if os.path.isfile(path):
                    bdbshell.dot_read(path)
                else:
                    bdbshell.stdout.write('%s is not a file.  Aborting.\n' %
                        (str(path),))
                    break
        bdbshell.cmdloop()
    return 0


def main():
    import sys
    sys.exit(run(sys.stdin, sys.stdout, sys.stderr, sys.argv))

if __name__ == '__main__':
    main()
