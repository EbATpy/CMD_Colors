
import ctypes

#Console Terminate
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)



def set_color(color, handle=std_out_handle):
	bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
	return bool

if 1 == 1:
	for i in range (255):
		for A in range (255):
			set_color(i|A)
			print ("#",A, i,"#")
			set_color(i|A)
time.sleep(11100)
