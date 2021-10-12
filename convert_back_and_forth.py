import dataprocessing.test as test
import dataprocessing.transformback as transformback

try:
    #test.convert_file("midi_filer/FFIII_Edgar_And_Sabin_Piano.mid","test.h5")
    test.convert_file("midi_filer/ff4-town.mid","test.h5")
    #test.convert_file("midi_filer/costadsol.mid","test.h5")
except:
    pass
for i in range(1):
    transformback.mido_transform_back("test.h5")
    try:
        pass
    except Exception as e:
        print(e)
    try:
        test.convert_file("test_output.mid","test.h5")
    except:
        pass
