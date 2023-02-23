import os
import os as sys

sys.chdir('C:/Users/durge/OneDrive/Desktop/Desktop Wallpaper')
print(sys.getcwd())

for f in sys.listdir():
    # print(sys.path.splitext(f))
    f_name,i_type=sys.path.splitext(f)
    t=f_name.split('-')
    f_Main=t[0].strip()
    f_second=t[1].strip()
    print(f_second)
    new_name='{}-{}{}'.format(f_Main,f_second,i_type)
    print(new_name)
    try:
        os.rename(f, new_name)
    except Exception as e:
        print("Renaming didn't work because " + str(e))