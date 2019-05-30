from pydub import AudioSegment
from pydub.utils import ratio_to_db


path = "..\\" + "audio_files" + "\\"
filename = "ashioto1"
fullpath =  path + filename + ".wav"
# 保存間隔
save_second = 0.2 * 1000
sound = AudioSegment.from_file(fullpath, format="wav")

# delta = ratio_to_db(1.5)
# sound_quiet = sound + delta
l_sound = len(sound)

print(l_sound)
# 音の平均値(db)
print(sound.max, sound.rms)
count = 0

for i in range(l_sound // int(save_second)):
    save_sound = sound[save_second * i:save_second * ( i + 1)]
    if save_sound.rms < 55 and save_sound.max < 100:
        pass
    
    else:
        save_sound.export("..\\" + "splitsounds" + "\\" + (filename[:-1]) + str(count) + ".wav")
        count += 1
