# `tryst`
CLI support package.

[tryst on Github](https://github.com/WholesomeNecromancer/tryst)

[GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0-standalone.html)

The [7 fundamental tenets](https://thesatanictemple.com/blogs/the-satanic-temple-tenets/there-are-seven-fundamental-tenets) of the [Satanic Temple](https://thesatanictemple.com/pages/about-us).
1. One should strive to act with compassion and empathy toward all creatures in accordance with reason.
2. The struggle for justice is an ongoing and necessary pursuit that should prevail over laws and institutions.
3. One's body is inviolable, subject to one's own will alone.
4. The freedom of others should be respected, including the freedom to offend. To willfully and unjustly encroach upon the freedoms of another is to forgo one's own.
5. Beliefs should conform to one's best scientific understanding of the world. One should take care never to distort scientific facts to fit one's beliefs.
6. People are fallible. If one makes a mistake, one should do one's best to rectify it and resolve any harm that might have been caused.
7. Every tenet is a guiding principle designed to inspire nobility in action and thought. The spirit of compassion, wisdom, and justice should always prevail over the written or spoken word.

# What `tryst` is:
A lightweight interface and context package for basic cli features intended for rapid atomic problem-solving and chaining of small building-blocks for greater automation potential.

`tryst` attempts to follow SOLID design principles where possible and is a learning experience in action to build a better understanding of Python, CLI development, unit testing, deployment, and more.

Ultimately, apps built with `tryst` are intended to be frozen with `PyInstaller` or an equivalent to be deployed/installed and used as shell apps via Windows PowerShell or Linux bash.

# What `tryst` is not:
`tryst` is not fancy or comprehensive. It is not intended to be flawless, nor to replace more fully-functional and well-established CLI support packages such as [argparse](https://docs.python.org/3/library/argparse.html) or [getopt](https://docs.python.org/3/library/getopt.html). It is a project for learning and for rapid development of workflow enhancements and automation.

This is evidenced by very little validation, leaving the burden of understanding on the implementing developer. For example, options and option-arguments are not duplicate-checked; undefined behavior will occur if you define more than one option object with the same brief or verbose tokens. Additionally, most of `tryst`'s methods are public rather than private; this is by design, to provide maximum flexibility to the implementer.

# Features
- Options and Option-Arguments specifiable via verbose (e.g. `--debug`) and brief (e.g. `-d`) tokens
- Configuration via `config.json` file and `get_config*` API
- Decoupled output; easily avoid unnecessary spew to `stdout` or `stderr`
    - `write*` api allows easy *to-file* functionality
- Procedural usage instructions (with room for manual input)
- Secrets (e.g. credentials) Support via `get_secret` API (TODO: needs encryption)

# Usage
Your app should have a single-module entrypoint:

`def main(mytryst=Tryst(), inputs=None):`

`mytryst` will be the tryst object your app uses to hold its `options` and `optionarguments`, and it will `consort()` with the given `inputs` to produce output and context; `useroptions`, `useroptionarguments`, and `userargs`.

>Initializing `mytryst` in this way provides simpler chaining between apps, empowering rapid growth.

1. Initialize `tryst` to establish necessary metadata.
`tryst.initialize(appname, authors, summary, version)`

2. Specify your `options` and `optionarguments`, establishing the rules of engagement for your tryst:
```
myoption = Option("my-option", "does something in my app", "m")
mytryst.add_option(myoption)

myoptionargument = Option("my-option-argument", "does something in my app", "a")
mytryst.add_option_argument(myoptionargument)
```

3. Consort; engage your tryst with the rules specified:
`mytryst.consort(inputs)`

4. Govern your app behavior based on the options the user specified:
```
if myoption in mytryst.useroptions:
    # Act on myoption

myoptargval = mytryst.useroptionarguments.get(myoptionargument)
if myoptargval:
    # Act on myoptionargument
```

5. Provide usage instructions based on your app and your tryst's rules:
`mytryst.show_usage()`
>Note: this may be appropriate in your app if the user specified no arguments, or no options, or some other criteria; because every app is different, the burden of making the call to provide this usage is on the developer. The `show_usage()` method creates procedural instructions based on your tryst's specified `options` and `optionarguments`.

6. Keep your output decoupled:
Use `mytryst.output(message)` for result output and `mytryst.error(message)` for error output.
If you are working to diagnose your app while developing, use `mytryst.debug(message)` to only display output when `--debug` is specified.

>*Keep in mind that `mytryst.output` and `mytryst.error` both buffer output to `mytryst.outputbuffer` and `mytryst.errorbuffer` respectively, which are written/flushed via `mytryst.write_stdout()` and `mytryst.write_stderr()`.*

7. Write your output:
`mytryst.write_stdout()`
`mytryst.write_stderr()`
>Using tryst's write APIs enables other developers to easily control your app's output to better suit their needs.

# CLI Conventions
- short options can be stacked
    - e.g. `tryst -e2` is equivalent to `tryst -e -2` and `tryst --error --two` respectively
- option-arguments only allow `=`, not spaces; complex values should be quoted at the shell
    - e.g. `--debug=true`, not `--debug true`
    - e.g. `--name="Wholesome Necromancer"`, not `--name=Wholesome Necromancer`
- order of options, option-arguments, and arguments does not matter in usage
    - e.g. `tryst.py --debug -e2 arg1`, `tryst.py -2e arg1 --debug`, and `tryst.py -e arg1 -2 --debug` are equivalent

# Best Practices
- Get configuration data *after* `consort()` is called to ensure the correct configuration file and path are loaded.

# Examples
Trivial example of app chaining:

```
# tryster.py
from tryst import Tryst
from tryst import Option
from tryst import main as trystmain

#--------------------------------------------------------------------------------
def main(mytryst=Tryst(), inputs=None):
    appname = "tryster"
    authors = "wholesomenecromancer"
    summary = "Tryster demonstrates calling one toolshed app from another at code-time."
    version = "0.0.1"
    mytryst.initialize(appname, authors, summary, version)

    silent_option = Option("silent", "Silence output from code-time-called tool.", "s")
    mytryst.add_option(silent_option)

    mytryst.consort(inputs)

    # Construct a separate tryst object for the other app we'll call
    theirtryst = Tryst()

    trystargs = ["tryst.py"]

    if silent_option in mytryst.useroptions:
        theirtryst.silence()

    for trysterarg in mytryst.userargs:
        trystargs.append(trysterarg)

    mytryst.debug("trystargs prior to call: " + str(trystargs))

    trystmain(theirtryst, trystargs)

    # Access tryst's output via theirtryst.outputbuffer

    mytryst.write_stdout()
    mytryst.write_stderr()
#--------------------------------------------------------------------------------

#------------------------------
if __name__ == "__main__":
    main()
#------------------------------
```

# Tests
Tests can be run from `src/tryst/` via `python -m unittest`.

# Documentation
Documentation is intended for use with `pdoc`:

`pdoc tryst.py`
`pdoc -o <destdir> tryst.py`

# Support
`tryst` intends to be platform-agnostic but has only been tested in Windows 10 environments with PowerShell 5.x and WSL 2.0's Ubuntu 20.x bash.
