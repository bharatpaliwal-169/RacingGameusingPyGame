import cx_Freeze
#setUp
executables = [cx_Freeze.Executable('ABitRacey.py')]

cx_Freeze.setup(
    name = 'A Bit Racey',
    options = {"build_exe" : {"packages":["pygame"],
                                "include_files":["car.jpeg","crashSound.wav"]
                            }},
    executables = executables
)
#end