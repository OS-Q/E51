from os.path import join
from SCons.Script import (AlwaysBuild, Default, DefaultEnvironment)
from colorama import Fore

env = DefaultEnvironment()
print( Fore.GREEN + '<<<<<<<<<<<< ' + env.BoardConfig().get("name").upper() + " >>>>>>>>>>>>" + Fore.BLACK )
elf = env.BuildProgram()
src = env.PackImage( join("$BUILD_DIR", "${PROGNAME}"), elf )
AlwaysBuild( src )
upload = env.Alias("upload", src, [ env.VerboseAction("$UPLOADCMD", "\n"), env.VerboseAction("", "\n") ] )
AlwaysBuild( upload )
Default( src )
